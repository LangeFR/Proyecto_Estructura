import os
import json
from tkinter import Canvas

class AVLNode:
    def __init__(self, valor, libro_id=None):
        self.valor = valor  # Año de publicación
        self.libros = [libro_id] if libro_id else []  # Lista de libros con este año
        self.left = None
        self.right = None
        self.height = 1  # Altura del nodo para el balanceo en un árbol AVL

    def add_title(self, libro_id):
        """Agrega un ID de libro al nodo (si el libro no existe ya)."""
        if libro_id not in self.libros:
            self.libros.append(libro_id)


class BalancedTree:
    def __init__(self):
        self.root = None

    def insert(self, valor, nodo):
        """Inserta un valor en el árbol equilibrado (AVL)."""
        if self.root is None:
            self.root = nodo
        else:
            self.root = self._insert_recursive(self.root, valor, nodo)

    def _insert_recursive(self, node, valor, nodo):
        """Inserta de manera recursiva y balancea el árbol."""
        if node is None:
            return nodo
        if valor < node.valor:
            node.left = self._insert_recursive(node.left, valor, nodo)
        elif valor > node.valor:
            node.right = self._insert_recursive(node.right, valor, nodo)
        else:
            # Si el valor es igual, no hacemos nada (no repetimos el año)
            return node

        # Actualiza la altura del nodo actual
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        # Balancear el nodo si es necesario
        balance = self._get_balance(node)

        # Casos de desbalanceo y rotación
        if balance > 1 and valor < node.left.valor:
            return self._rotate_right(node)
        if balance < -1 and valor > node.right.valor:
            return self._rotate_left(node)
        if balance > 1 and valor > node.left.valor:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and valor < node.right.valor:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _get_height(self, node):
        """Devuelve la altura de un nodo."""
        if node is None:
            return 0
        return node.height

    def _get_balance(self, node):
        """Calcula el factor de balance de un nodo."""
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_left(self, z):
        """Realiza una rotación hacia la izquierda."""
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _rotate_right(self, z):
        """Realiza una rotación hacia la derecha."""
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y


class VisualizarAnioAdapter:
    def __init__(self, canvas: Canvas):
        self.canvas = canvas
        # Determina la ruta raíz del proyecto
        current_dir = os.path.dirname(__file__)  # Directorio actual del archivo
        project_root = os.path.abspath(os.path.join(current_dir, '..'))  # Directorio de Proyecto_Estructura
        # Define las rutas de los archivos
        self.ruta_books = os.path.join(project_root, 'base_de_datos', 'books.json')

    def cargar_libros(self):
        """Carga los libros desde el archivo JSON."""
        if not os.path.exists(self.ruta_books):
            raise FileNotFoundError(f"El archivo books.json no se encontró en la ruta: {self.ruta_books}")
        with open(self.ruta_books, 'r', encoding='utf-8') as file:
            return json.load(file)

    def construir_arbol_por_anio(self):
        """Construye el árbol basado en años de publicación."""
        books = self.cargar_libros()

        year_tree = BalancedTree()
        year_tree.insert("Biblioteca", None)  # Nodo raíz del árbol

        # Crear un diccionario para mapear años a nodos
        anio_nodos = {"Biblioteca": year_tree.root}

        # Agrupar libros por año de publicación
        for book in books:
            anio_publicacion = book["anio_publicacion"]
            libro_id = book["id"]  # Usar el ID del libro

            # Si el nodo del año no existe, crearlo
            if anio_publicacion not in anio_nodos:
                anio_nodo = AVLNode(anio_publicacion, None)
                anio_nodos[anio_publicacion] = anio_nodo
                # Aquí se debe usar el método de insertar en el árbol
                year_tree.insert(anio_publicacion, anio_nodo)

            # Agregar el libro al nodo del año
            anio_nodos[anio_publicacion].add_title(libro_id)

        return year_tree

    def dibujar_arbol(self, nodo, x, y, dx, dy):
        if nodo is None:
            return

        # Verificar que nodo es una instancia de AVLNode
        if not isinstance(nodo, AVLNode):
            print(f"Error: El nodo no es una instancia de AVLNode. Es: {type(nodo)}")
            return

        # Dibujar el nodo
        self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="lightblue", outline="black")
        self.canvas.create_text(x, y, text=nodo.valor)  # Usar anio_publicacion en lugar de valor

        # Dibujar las conexiones con los nodos hijos
        if nodo.left:
            child_x = x - dx
            child_y = y + dy
            self.canvas.create_line(x, y, child_x, child_y)
            self.dibujar_arbol(nodo.left, child_x, child_y, dx / 2, dy)

        if nodo.right:
            child_x = x + dx
            child_y = y + dy
            self.canvas.create_line(x, y, child_x, child_y)
            self.dibujar_arbol(nodo.right, child_x, child_y, dx / 2, dy)




    def calcular_ancho_subarbol(self, node):
        """Calcula el ancho del subárbol en términos de número de hojas."""
        if not node.libros:
            return 1  # Es una hoja
        return sum(self.calcular_ancho_subarbol(child) for child in node.libros)

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
        print("  " * nivel + f"{node.valor}: {[child.valor for child in node.libros]}")
        for child in node.libros:
            self.imprimir_arbol(child, nivel + 1)
