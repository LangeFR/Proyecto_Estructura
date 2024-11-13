import tkinter as tk
import tkinter.ttk as ttk
import json
from models.n_ary_tree import NAryTree
from tkinter import Canvas

# Rutas a los archivos de datos
ruta_books = r"C:\Users\DellInspiron5570\Documents\Universidad\Semestres\Semestre 4\Estructura\Corte 3\Proyecto_Estructura\base_de_datos\books.json"
ruta_generos = r"C:\Users\DellInspiron5570\Documents\Universidad\Semestres\Semestre 4\Estructura\Corte 3\Proyecto_Estructura\base_de_datos\generos.json"

class VisualizarGenerosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualización de Géneros")
        
        # Crear Combobox para selección de género
        self.combobox = ttk.Combobox(root, values=["Género"], state="readonly")
        self.combobox.set("Seleccione una opción")
        self.combobox.pack(pady=10)
        
        # Asociar el evento de selección al método de visualización
        self.combobox.bind("<<ComboboxSelected>>", self.on_combobox_select)
        
        # Crear Canvas para la visualización del árbol
        self.canvas = Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack(pady=10)
        
    def on_combobox_select(self, event):
        # Verificar si se seleccionó "Género"
        if self.combobox.get() == "Género":
            # Construir el árbol de géneros
            genre_tree = self.construir_arbol_por_genero()
            # Limpiar el canvas
            self.canvas.delete("all")
            # Dibujar el árbol en el canvas
            self.dibujar_arbol(self.canvas, genre_tree.root, 300, 20, 150)

    def cargar_libros(self):
        # Cargar los libros desde books.json
        with open(ruta_books, 'r') as file:
            return json.load(file)

    def cargar_generos(self):
        # Cargar los géneros desde generos.json
        with open(ruta_generos, 'r') as file:
            generos = json.load(file)
        # Crear un diccionario para mapear generoId a nombre
        return {genero['id']: genero['nombre'] for genero in generos}

    def construir_arbol_por_genero(self):
        # Cargar datos de libros y géneros
        books = self.cargar_libros()
        generos = self.cargar_generos()
        
        # Crear el árbol n-ario
        genre_tree = NAryTree()
        genre_tree.insert("Biblioteca")  # Nodo raíz
        
        # Insertar cada libro en el árbol según su género
        for book in books:
            genero_id = book['generoId']
            book_id = book['id']
            genero_nombre = generos.get(genero_id, "Género desconocido")
            
            # Buscar o insertar el nodo de género
            genre_node = genre_tree.search(genero_nombre)
            if not genre_node:
                genre_tree.insert(genero_nombre)
                genre_node = genre_tree.search(genero_nombre)
                
            # Añadir el ID del libro al nodo de género
            genre_node.add_title(book_id)
        
        return genre_tree

    def dibujar_arbol(self, canvas, node, x, y, x_offset):
        """Dibuja recursivamente el árbol en el canvas."""
        if not node:
            return
        
        # Dibujar el nodo actual
        canvas.create_text(x, y, text=f"{node.value}\nIDs: {', '.join(node.book_titles)}", anchor="center")
        
        # Dibujar cada hijo del nodo
        child_y = y + 80  # Espaciado vertical entre niveles
        for i, child in enumerate(node.children):
            # Calcular posición x para cada hijo
            child_x = x - x_offset + (i * (x_offset * 2 // max(1, len(node.children))))
            # Dibujar línea entre el nodo actual y el hijo
            canvas.create_line(x, y + 10, child_x, child_y - 10)
            # Dibujar el hijo
            self.dibujar_arbol(canvas, child, child_x, child_y, x_offset // 2)

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = VisualizarGenerosApp(root)
    root.mainloop()
