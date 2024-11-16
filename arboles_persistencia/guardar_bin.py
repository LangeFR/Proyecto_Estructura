# scripts/build_title_tree.py

import json
import sys
import os

# Obtener el directorio actual (scripts/)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Navegar al directorio padre (Proyecto_Estructura/)
project_root = os.path.abspath(os.path.join(current_dir, '..'))

# Agregar el directorio 'models' al sys.path
models_dir = os.path.join(project_root, 'models')
if models_dir not in sys.path:
    sys.path.append(models_dir)

# Importar BinaryTree desde binary_tree.py
from binary_search_tree import BinaryTree

# Rutas de archivos
ruta_books = os.path.join(project_root, 'base_de_datos', 'books.json')
ruta_arbol = os.path.join(project_root, 'arboles_persistencia', 'title_tree.json')

# Función para cargar datos JSON
def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

# Función para convertir el árbol a un diccionario para guardarlo en JSON
def tree_to_dict(node):
    if node is None:
        return {}
    return {
        "titulo": node.titulo,
        "id": node.id,
        "left": tree_to_dict(node.left),
        "right": tree_to_dict(node.right)
    }

# Función principal
def main():
    print("Cargando libros...")

    # Cargar los libros desde el archivo JSON
    books = load_json(ruta_books)

    # Crear una instancia del árbol binario con nodo raíz 'Biblioteca'
    title_tree = BinaryTree()

    # Insertar cada libro en el árbol
    for book in books:
        book_id = book['id']
        titulo = book['titulo']
        title_tree.insert(book_id, titulo)

    # Convertir el árbol a un diccionario serializable en JSON
    tree_dict = title_tree.to_dict()

    # Guardar el árbol en un archivo JSON
    with open(ruta_arbol, 'w', encoding='utf-8') as file:
        json.dump(tree_dict, file, ensure_ascii=False, indent=4)

    print(f"Árbol de títulos guardado exitosamente en {ruta_arbol}")

if __name__ == "__main__":
    main()
