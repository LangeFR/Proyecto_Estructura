import os
import json
import tkinter as tk
from tkinter import Canvas

# Importar las clases Node y BinaryTree desde models/binary_tree.py
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
models_dir = os.path.join(project_root, 'models')
if models_dir not in os.sys.path:
    os.sys.path.append(models_dir)

from binary_search_tree import BinaryTree, Node


class Tooltip:
    """
    Clase para gestionar tooltips como Label en una posición fija.
    """
    def __init__(self, parent):
        """
        Inicializa el Tooltip creando un Label en una posición fija.
        :param parent: El widget padre donde se colocará el tooltip.
        """
        self.parent = parent
        self.tooltip_label = tk.Label(
            parent,
            text="",
            bg="#b14ee9",
            fg="#FFFFFF",
            bd=2,
            relief="solid",
            font=("Verdana", 10, "bold"),
        )

        # Posicionar el tooltip en la parte inferior central
        self.tooltip_label.place(relx=0.5, rely=0.95, anchor='s')  # Centrado horizontalmente
        self.tooltip_label.lower()  # Inicialmente oculto

    def show(self, text):
        """Muestra el tooltip con el texto proporcionado."""
        self.tooltip_label.config(text=text)
        self.tooltip_label.lift()  # Asegurar que el tooltip esté visible

    def hide(self):
        """Oculta el tooltip."""
        self.tooltip_label.config(text="")  # Limpia el texto
        self.tooltip_label.lower()  # Envía el tooltip al fondo

class VisualizarTituloAdapter:
    def __init__(self, canvas):
        self.canvas = canvas
        self.tooltip = Tooltip(self.canvas.master)  # Inicializar el Tooltip
        # Define las rutas de los archivos
        self.ruta_books = os.path.join(project_root, 'base_de_datos', 'books.json')
        self.libros = self.cargar_libros()  # Cargar libros al inicializar el adaptador

    def cargar_libros(self):
        """Carga los libros desde el archivo JSON."""
        if not os.path.exists(self.ruta_books):
            raise FileNotFoundError(f"El archivo books.json no se encontró en la ruta: {self.ruta_books}")
        with open(self.ruta_books, 'r', encoding='utf-8') as file:
            return json.load(file)

    def construir_arbol_por_titulo(self):
        books = self.libros
        # Crear una instancia del árbol binario
        title_tree = BinaryTree()
        # Insertar cada libro en el árbol
        for book in books:
            title_tree.insert(book['id'], book['titulo'])
        return title_tree

    def calcular_hojas(self, nodo):
        """Calcula y asigna el número de hojas en cada subárbol."""
        if nodo is None:
            return 0
        if nodo.left is None and nodo.right is None:
            nodo.hojas = 1
        else:
            hojas_izquierda = self.calcular_hojas(nodo.left)
            hojas_derecha = self.calcular_hojas(nodo.right)
            nodo.hojas = hojas_izquierda + hojas_derecha
        return nodo.hojas

    def assign_positions(self, nodo, x_min, x_max, y):
        """Asigna posiciones x e y a cada nodo basadas en el número de hojas."""
        if nodo is None:
            return

        # Calcular la posición x del nodo como el punto medio entre x_min y x_max
        nodo.x = (x_min + x_max) / 2
        nodo.y = y

        # Calcular los límites para los hijos
        if nodo.left:
            self.assign_positions(nodo.left, x_min, nodo.x, y + 1)
        if nodo.right:
            self.assign_positions(nodo.right, nodo.x, x_max, y + 1)

    def dibujar_arbol(self, root):
        """Dibuja el árbol en el Canvas."""
        # Calcular el número total de hojas para definir el ancho del árbol
        total_hojas = self.calcular_hojas(root)

        # Asignar posiciones x e y a los nodos
        self.assign_positions(root, x_min=0, x_max=total_hojas, y=0)

        # Escala para convertir las posiciones lógicas en coordenadas del Canvas
        x_scale = 80 *2  
        y_scale = 100 *2 

        # Ajustar el tamaño del Canvas en función del ancho del árbol
        canvas_width = total_hojas * x_scale + 200
        self.canvas.config(scrollregion=(0, 0, canvas_width, (root.y + 2) * y_scale))

        # Dibujar los nodos en el Canvas
        self.draw_node(root, x_scale, y_scale)

    def draw_node(self, nodo, x_scale, y_scale):
        """Dibuja un nodo y sus hijos en el Canvas."""
        if nodo is None:
            return

        x = nodo.x * x_scale + 100  # Desplazamiento para centrar
        y = nodo.y * y_scale + 50

        # Dibujar el óvalo (nodo) y el texto
        tag = f"node_{nodo.id}"

        self.canvas.create_oval(x - 30, y - 20, x + 30, y + 20, fill="#ffa5e5", outline="black", width=2, tags=tag)

        # Vincular eventos de ratón para mostrar información en el tooltip
        self.canvas.tag_bind(tag, "<Enter>", lambda event, t=nodo.titulo: self.tooltip.show(t))
        self.canvas.tag_bind(tag, "<Leave>", lambda event: self.tooltip.hide())

        # Dibujar líneas a los hijos
        if nodo.left:
            child_x = nodo.left.x * x_scale + 100
            child_y = nodo.left.y * y_scale + 50
            self.canvas.create_line(x, y + 20, child_x, child_y - 20, width=1, fill="#666666")
            self.draw_node(nodo.left, x_scale, y_scale)
        if nodo.right:
            child_x = nodo.right.x * x_scale + 100
            child_y = nodo.right.y * y_scale + 50
            self.canvas.create_line(x, y + 20, child_x, child_y - 20, width=1, fill="#666666")
            self.draw_node(nodo.right, x_scale, y_scale)



def main():
    # Crear la ventana principal de Tkinter
    ventana = tk.Tk()
    ventana.title("Visualización del Árbol Binario")
    ventana.geometry("1200x800")

    # Crear el Canvas donde se dibujará el árbol
    canvas = Canvas(ventana, width=1200, height=600, bg="#ffefa5")
    canvas.pack(fill=tk.BOTH, expand=True)  # Expandir para llenar el espacio disponible

    # Crear una instancia del adaptador de visualización
    visualizador = VisualizarTituloAdapter(canvas)

    # Construir el árbol binario
    title_tree = visualizador.construir_arbol_por_titulo()

    # Dibujar el árbol en el canvas
    visualizador.dibujar_arbol(title_tree.root)

    # Ejecutar el bucle principal de Tkinter
    ventana.mainloop()

if __name__ == "__main__":
    main()

