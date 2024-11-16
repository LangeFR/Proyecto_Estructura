import json

import sys
import os

# Agregar la ruta del directorio 'models' al sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')  # Navegar al directorio padre
models_dir = os.path.join(parent_dir, 'models')
sys.path.append(models_dir)

# Importar NAryTree desde n_ary_tree.py
from models.n_ary_tree import NAryTree

# Determina la ruta al directorio raíz del proyecto
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))

# Rutas de archivos
ruta_books = os.path.join(project_root, 'base_de_datos', 'books.json')
ruta_generos = os.path.join(project_root, 'base_de_datos', 'generos.json')



# Función para cargar los libros desde el archivo JSON
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


# Rutas de archivos
ruta_books = r"C:\Users\DellInspiron5570\Documents\Universidad\Semestres\Semestre 4\Estructura\Corte 3\Proyecto_Estructura\base_de_datos\books.json"
ruta_generos = r"C:\Users\DellInspiron5570\Documents\Universidad\Semestres\Semestre 4\Estructura\Corte 3\Proyecto_Estructura\base_de_datos\generos.json"
ruta_arbol = r"C:\Users\DellInspiron5570\Documents\Universidad\Semestres\Semestre 4\Estructura\Corte 3\Proyecto_Estructura\arboles_persistencia\genre_tree.json"

# Función para cargar datos JSON
def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Crear un diccionario para mapear generoId a nombre de género
def crear_mapa_generos(generos):
    return {genero['id']: genero['nombre'] for genero in generos}

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
    print("Cargando libros y géneros...")

    # Cargar los libros y géneros desde los archivos JSON
    books = load_json(ruta_books)
    generos = load_json(ruta_generos)

    # Crear el mapa de generos {id: nombre}
    mapa_generos = crear_mapa_generos(generos)

    # Crear el árbol n-ario con "Biblioteca" como nodo raíz
    genre_tree = NAryTree()
    genre_tree.insert("Biblioteca")

    # Insertar libros en el árbol de acuerdo a su género
    for book in books:
        genero_id = book['generoId']
        book_id = book['id']

        # Obtener el nombre del género a partir del generoId
        genero_nombre = mapa_generos.get(genero_id)
        if not genero_nombre:
            print(f"Género con ID {genero_id} no encontrado en generos.json.")
            continue

        # Insertar o buscar el nodo del género por nombre
        genre_node = genre_tree.search(genero_nombre)
        if not genre_node:
            genre_tree.insert(genero_nombre)
            genre_node = genre_tree.search(genero_nombre)
        
        # Añadir el ID del libro al nodo correspondiente
        genre_node.add_title(book_id)

    # Guardar el árbol n-ario en un archivo JSON
    with open(ruta_arbol, 'w') as file:
        json.dump(tree_to_dict(genre_tree.root), file, indent=4)

    print(f"Árbol de géneros guardado exitosamente en {ruta_arbol}")

if __name__ == "__main__":
    main()