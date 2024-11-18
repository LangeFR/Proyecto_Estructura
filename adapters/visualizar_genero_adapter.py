import os
import json
from models.n_ary_tree import NAryTree, NAryNode
import tkinter as tk  # Asegúrate de importar tkinter si es necesario para Tooltip

class Tooltip:
    """
    Clase para gestionar tooltips como Label en una posición fija.
    """
    def __init__(self, parent):
        """
        Inicializa el Tooltip creando un Label en la posición fija.
        
        :param parent: El widget padre donde se colocará el tooltip.
        """
        self.parent = parent
        self.tooltip_label = tk.Label(parent, text="", bg="yellow", fg="black", bd=1, relief="solid", font=("Arial", 10, "bold"))
        # Posicionar el tooltip en la parte inferior central del frame
        self.tooltip_label.place(relx=0.5, rely=0.95, anchor='s')  # 95% de la altura, centrado horizontalmente
        self.tooltip_label.lower()  # Ocultar inicialmente

    def show(self, text):
        """
        Muestra el tooltip con el texto proporcionado.
        
        :param text: El texto que se mostrará en el tooltip.
        """
        self.tooltip_label.config(text=text)
        self.tooltip_label.lift()  # Llevar el tooltip al frente

    def hide(self):
        """
        Oculta el tooltip.
        """
        self.tooltip_label.config(text="")
        self.tooltip_label.lower()  # Enviar el tooltip al fondo


class VisualizarGeneroAdapter:
    def __init__(self, canvas):
        self.canvas = canvas
        # Determina la ruta raíz del proyecto
        current_dir = os.path.dirname(__file__)  # Directorio actual del archivo
        project_root = os.path.abspath(os.path.join(current_dir, '..'))  # Directorio de Proyecto_Estructura
        # Define las rutas de los archivos
        self.ruta_books = os.path.join(project_root, 'base_de_datos', 'books.json')
        self.ruta_generos = os.path.join(project_root, 'base_de_datos', 'generos.json')
        self.generos = self.cargar_generos()  # Cargar géneros al inicializar el adaptador

        # Inicializar el objeto Tooltip
        self.tooltip = Tooltip(self.canvas.master)

    def cargar_libros(self):
        """Carga los libros desde el archivo JSON."""
        if not os.path.exists(self.ruta_books):
            raise FileNotFoundError(f"El archivo books.json no se encontró en la ruta: {self.ruta_books}")
        with open(self.ruta_books, 'r', encoding='utf-8') as file:
            return json.load(file)

    def cargar_generos(self):
        """Carga los géneros desde el archivo JSON."""
        if not os.path.exists(self.ruta_generos):
            raise FileNotFoundError(f"El archivo generos.json no se encontró en la ruta: {self.ruta_generos}")
        with open(self.ruta_generos, 'r', encoding='utf-8') as file:
            return json.load(file)

    def construir_arbol_por_genero(self):
        """Construye el árbol n-ario basado en IDs de géneros."""
        books = self.cargar_libros()
        generos = self.generos

        genre_tree = NAryTree()
        genre_tree.insert("Biblioteca")  # Nodo raíz del árbol

        # Crear un diccionario para mapear IDs de géneros a nodos
        genero_nodos = {"Biblioteca": genre_tree.root}

        # Insertar géneros usando su ID
        for genero in generos:
            genero_id = genero["id"]
            genero_padre_id = genero.get("generoPadreId")

            # Crea el nodo si no existe
            if genero_id not in genero_nodos:
                genero_nodos[genero_id] = NAryNode(genero_id)

            # Relacionar con su padre
            if genero_padre_id:
                if genero_padre_id not in genero_nodos:
                    genero_nodos[genero_padre_id] = NAryNode(genero_padre_id)
                parent_node = genero_nodos[genero_padre_id]
                if genero_nodos[genero_id] not in parent_node.children:
                    parent_node.children.append(genero_nodos[genero_id])
            else:
                # Sin padre, vincular al nodo raíz
                root_node = genero_nodos["Biblioteca"]
                if genero_nodos[genero_id] not in root_node.children:
                    root_node.children.append(genero_nodos[genero_id])

        # Asignar libros a sus géneros
        for book in books:
            genero_id = book["generoId"]
            genero_node = genero_nodos.get(genero_id)
            if genero_node:
                genero_node.add_title(book["id"])

        return genre_tree

    def obtener_iniciales(self, genero_id):
        """Obtiene las iniciales del nombre del género dado su ID."""
        if genero_id == "Biblioteca":
            return "Biblioteca"
        for genero in self.generos:
            if genero["id"] == genero_id:
                nombre = genero["nombre"]
                # Generar las iniciales del nombre (e.g., "Romance Histórico" -> "R. H.")
                return ". ".join([palabra[0].upper() for palabra in nombre.split()]) + "."
        return "N/A"  # En caso de que no se encuentre el nombre
    
    def dibujar_arbol(self, node, x, y, x_offset=100):
        """Dibuja el árbol en el canvas mostrando las iniciales de los géneros con ajuste en la disposición horizontal."""
        if not node:
            return
        
        # Determinar si el nodo es "Biblioteca" y ajustar el tamaño
        if node.value == "Biblioteca":
            radius_x, radius_y = 67, 20  # Radio más grande para el nodo de "Biblioteca"
            font_size = "Arial 12 bold"  # Fuente más grande para el texto del nodo de "Biblioteca"
        else:
            radius_x, radius_y = 30, 20
            font_size = "Arial 10 bold"

        iniciales = self.obtener_iniciales(node.value)
        texto = self.ajustar_texto(iniciales, 15)  # Ajustar texto a un máximo de 15 caracteres
        tag = f"node_{node.value}"

        # Crear el fondo ovalado del nodo
        self.canvas.create_oval(x - radius_x, y - radius_y, x + radius_x, y + radius_y, fill="#ec8bff", outline="black", width=2, tags=tag)
        self.canvas.create_text(x, y, text=texto, anchor="center", font=font_size, tags=(tag,))


        self.agregar_eventos_nodo(tag, node.value)

        if not node.children:
            return

        y_hijos = y + 120
        ancho_total = self.calcular_ancho_subarbol(node)
        current_x = x - ancho_total / 2

        posiciones_hijos = []
        for child in node.children:
            child_ancho = self.calcular_ancho_subarbol(child)
            child_x = current_x + child_ancho / 2
            posiciones_hijos.append(child_x)
            self.dibujar_arbol(child, child_x, y_hijos, x_offset)
            current_x += child_ancho

        if posiciones_hijos:
            x_centrado = (posiciones_hijos[0] + posiciones_hijos[-1]) / 2
            self.canvas.move(tag, x_centrado - x, 0)

        for child_x in posiciones_hijos:
            self.canvas.create_line(x_centrado, y + 20, child_x, y_hijos - 20, fill="#4caf50", width=2)





    def calcular_ancho_subarbol(self, node):
        """Calcula el ancho del subárbol basado en el tamaño del nodo (ovalo) y no solo en la cantidad de hojas."""
        if not node.children:
            return 70  # Ancho del nodo (ovalo) en píxeles
        return sum(self.calcular_ancho_subarbol(child) for child in node.children)

    def ajustar_texto(self, texto, max_length):
        """Divide el texto en múltiples líneas si excede el máximo de caracteres por línea."""
        words = str(texto).split()
        lines = []
        current_line = ""
        for word in words:
            if len(current_line) + len(word) + 1 > max_length:
                lines.append(current_line)
                current_line = word
            else:
                current_line += " " + word if current_line else word
        if current_line:
            lines.append(current_line)
        return "\n".join(lines)

    def imprimir_arbol(self, node, nivel=0):
        """Imprime el árbol en consola para validar la jerarquía."""
        if not node:
            return
        print("  " * nivel + f"{node.value}: {[child.value for child in node.children]}")
        for child in node.children:
            self.imprimir_arbol(child, nivel + 1)

    def agregar_eventos_nodo(self, tag, genero_id):
        """Asocia eventos de mouse a un nodo en el Canvas."""
        # Vincula el evento para mostrar el tooltip
        self.canvas.tag_bind(tag, "<Enter>", lambda event, gid=genero_id: self.mostrar_tooltip(gid))
        # Vincula el evento para ocultar el tooltip
        self.canvas.tag_bind(tag, "<Leave>", self.ocultar_tooltip)

    def mostrar_tooltip(self, genero_id):
        """Muestra un tooltip con información del nodo en una posición fija."""
        try:
            # Obtener el nombre completo del género
            nombre_completo = next((genero["nombre"] for genero in self.generos if genero["id"] == genero_id), "N/A")

            # Mostrar el tooltip en la posición fija
            self.tooltip.show(nombre_completo)
        except Exception as e:
            print(f"Error en mostrar_tooltip: {e}")

    def ocultar_tooltip(self, event=None):
        """Elimina cualquier tooltip existente del Canvas."""
        try:
            self.tooltip.hide()
        except Exception as e:
            print(f"Error en ocultar_tooltip: {e}")
