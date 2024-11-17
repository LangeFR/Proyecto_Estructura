# scripts/guardar_grafo.py

import json
import sys
import os
import networkx as nx

# Obtener el directorio actual (scripts/)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Navegar al directorio padre (Proyecto_Estructura/)
project_root = os.path.abspath(os.path.join(current_dir, '..'))

# Agregar el directorio 'models' al sys.path
models_dir = os.path.join(project_root, 'models')
if models_dir not in sys.path:
    sys.path.append(models_dir)

# Importar la clase Grafo desde grafos.py
from grafos import Grafo

# Rutas de archivos
ruta_books = os.path.join(project_root, 'base_de_datos', 'books.json')
ruta_grafo = os.path.join(project_root, 'grafos_persistencia', 'grafo_libros.json')

# Función para cargar datos JSON
def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

# Función para guardar el grafo en JSON
def save_graph_to_json(graph, filename):
    data = nx.node_link_data(graph)
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Función principal
def main():
    print("Cargando libros...")

    # Cargar los libros desde el archivo JSON
    books = load_json(ruta_books)

    # Crear una instancia del grafo
    grafo = Grafo()

    # Crear los nodos y las relaciones
    for book in books:
        titulo = book['titulo']
        autor = f"Autor_{book['autorId']}"
        genero = f"Género_{book['generoId']}"
        anio = f"Año_{book['anio_publicacion']}"

        # Agregar nodos con atributos de tipo
        grafo.agregar_nodo(titulo, tipo='libro')
        grafo.agregar_nodo(autor, tipo='autor')
        grafo.agregar_nodo(genero, tipo='género')
        grafo.agregar_nodo(anio, tipo='año')

        # Agregar aristas
        grafo.agregar_arista(titulo, autor)
        grafo.agregar_arista(titulo, genero)
        grafo.agregar_arista(titulo, anio)

    # Verificar si el directorio existe, si no, crearlo
    if not os.path.exists(os.path.dirname(ruta_grafo)):
        os.makedirs(os.path.dirname(ruta_grafo))

    # Guardar el grafo en un archivo JSON
    save_graph_to_json(grafo.grafo, ruta_grafo)

    print(f"Grafo de libros guardado exitosamente en {ruta_grafo}")

if __name__ == "__main__":
    main()
