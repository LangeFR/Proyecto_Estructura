import json
import os
from models.n_ary_tree import NAryTree  # Importamos la clase NAryTree

# Definimos las rutas para cargar los libros y guardar el árbol
ruta_base_datos = r"C:\Users\DellInspiron5570\Documents\Universidad\Semestres\Semestre 4\Estructura\Corte 3\Proyecto_Estructura\base_de_datos\books.json"
ruta_arbol = r"C:\Users\DellInspiron5570\Documents\Universidad\Semestres\Semestre 4\Estructura\Corte 3\Proyecto_Estructura\base_de_datos\genre_tree.json"

# Función para cargar libros desde el archivo JSON
def load_books(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Convertir el árbol a un diccionario para guardarlo en JSON
def tree_to_dict(node):
    if node is None:
        return {}
    return {
        "value": node.value,
        "book_ids": node.book_titles,
        "children": [tree_to_dict(child) for child in node.children]
    }

# Función principal
def main():
    # Cargar los libros del archivo JSON
    books = load_books(ruta_base_datos)

    # Crear el árbol n-ario
    genre_tree = NAryTree()

    # Insertar libros en el árbol por género
    for book in books:
        genero = book['genero']
        book_id = book['id']
        
        # Insertar el género si no existe
        genre_tree.insert(genero)
        
        # Buscar el nodo del género e insertar el ID del libro
        genre_node = genre_tree.search(genero)
        if genre_node:
            genre_node.add_title(book_id)

    # Guardar el árbol n-ario en un archivo JSON
    with open(ruta_arbol, 'w') as file:
        json.dump(tree_to_dict(genre_tree.root), file, indent=4)

    print(f"Árbol de géneros guardado exitosamente en {ruta_arbol}")

if __name__ == "__main__":
    main()