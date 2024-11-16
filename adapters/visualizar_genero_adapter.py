import os
import json
from models.n_ary_tree import NAryTree, NAryNode

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
        BFlag = False
        """Obtiene las iniciales del nombre del género dado su ID."""
        for genero in self.generos:
            if genero["id"] == genero_id:
                nombre = genero["nombre"]
                # Generar las iniciales del nombre (e.g., "Romance Historico" -> "R. H.")
                return ". ".join([palabra[0].upper() for palabra in nombre.split()]) + "."
        if BFlag == False:
            BFlag = True
            return "Biblioteca"
        return "N/A"  # En caso de que no se encuentre el nombre

    def dibujar_arbol(self, node, x, y, x_offset):
        """Dibuja el árbol en el canvas mostrando las iniciales de los géneros."""
        if not node:
            return

        # Obtener las iniciales del género
        iniciales = self.obtener_iniciales(node.value)
        texto = self.ajustar_texto(iniciales, 15)  # Ajustar texto a un máximo de 15 caracteres

        # Crear el texto en el canvas y asociar un tag único basado en el valor del nodo
        tag = f"node_{node.value}"
        self.canvas.create_text(x, y, text=texto, anchor="center", tags=(tag,))

        # Si el nodo no tiene hijos, simplemente dibuja
        if not node.children:
            return

        # Calcular las posiciones de los hijos
        y_hijos = y + 80
        ancho_total = self.calcular_ancho_subarbol(node) * 50  # Determina el rango total de ancho
        current_x = x - ancho_total // 2  # Empieza desde la posición inicial del rango

        posiciones_hijos = []  # Lista para almacenar las posiciones de los hijos
        for child in node.children:
            child_ancho = self.calcular_ancho_subarbol(child) * 50
            child_x = current_x + child_ancho // 2  # Centra el hijo dentro de su rango
            posiciones_hijos.append(child_x)
            self.dibujar_arbol(child, child_x, y_hijos, x_offset)
            current_x += child_ancho  # Avanza al siguiente hijo

        # Recalcular la posición del nodo actual basado en los hijos
        if posiciones_hijos:
            x_centrado = (posiciones_hijos[0] + posiciones_hijos[-1]) // 2
            # Mover el texto del nodo actual al nuevo centro
            self.canvas.move(tag, x_centrado - x, 0)

        # Dibuja líneas entre el nodo y sus hijos
        for child_x in posiciones_hijos:
            self.canvas.create_line(x_centrado, y + 20, child_x, y_hijos - 20)


    def calcular_ancho_subarbol(self, node):
        """Calcula el ancho del subárbol en términos de número de hojas."""
        if not node.children:
            return 1  # Es una hoja
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
