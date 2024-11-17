import json
import os
import sys

# Obtener el directorio actual (scripts/)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Navegar al directorio padre (Proyecto_Estructura/)
project_root = os.path.abspath(os.path.join(current_dir, '..'))

# Agregar el directorio 'models' al sys.path
models_dir = os.path.join(project_root, 'models')
if models_dir not in sys.path:
    sys.path.append(models_dir)

# Importar la clase Grafo desde el archivo correspondiente
from models.GRAFOS import Grafo

# Rutas de archivos
ruta_books = os.path.join(project_root, 'base_de_datos', 'books.json')
ruta_grafo = os.path.join(project_root, 'arboles_persistencia', 'relations_graph.json')

# Función para cargar datos JSON
def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

# Función para convertir el grafo a un formato serializable
def graph_to_dict(grafo):
    graph_dict = {"nodes": [], "edges": []}
    for node in grafo.grafo.nodes:
        graph_dict["nodes"].append({"id": node, "label": node})
    for edge in grafo.grafo.edges:
        graph_dict["edges"].append({"source": edge[0], "target": edge[1]})
    return graph_dict

# Función principal
def main():
    print("Cargando datos de libros...")

    # Cargar los datos desde el archivo JSON
    books = load_json(ruta_books)

    # Crear una instancia del grafo
    relations_graph = Grafo()

    # Construir el grafo con los datos
    for book in books:
        book_title = book["titulo"]
        author_id = f"Autor_{book['autorId']}"
        genre_id = f"Género_{book['generoId']}"
        editorial_id = f"Editorial_{book['editorialId']}"

        # Agregar nodos
        relations_graph.agregar_nodo(book_title)
        relations_graph.agregar_nodo(author_id)
        relations_graph.agregar_nodo(genre_id)
        relations_graph.agregar_nodo(editorial_id)

        # Agregar aristas (relaciones)
        relations_graph.agregar_arista(book_title, author_id)   # Libro → Autor
        relations_graph.agregar_arista(book_title, genre_id)    # Libro → Género
        relations_graph.agregar_arista(book_title, editorial_id) # Libro → Editorial
        relations_graph.agregar_arista(author_id, genre_id)     # Autor → Género

    # Convertir el grafo a un formato serializable en JSON
    graph_dict = graph_to_dict(relations_graph)

    # Guardar el grafo en un archivo JSON
    with open(ruta_grafo, 'w', encoding='utf-8') as file:
        json.dump(graph_dict, file, ensure_ascii=False, indent=4)

    print(f"Grafo de relaciones guardado exitosamente en {ruta_grafo}")

if __name__ == "__main__":
    main()
