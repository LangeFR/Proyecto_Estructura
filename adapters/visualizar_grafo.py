# scripts/visualizacion_grafos.py

import json
import sys
import os
import networkx as nx
import matplotlib.pyplot as plt
from adjustText import adjust_text

# Obtener el directorio actual (scripts/)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Navegar al directorio raíz del proyecto (Proyecto_Estructura/)
project_root = os.path.abspath(os.path.join(current_dir, '..'))

# Agregar el directorio 'models' al sys.path
models_dir = os.path.join(project_root, 'models')
if models_dir not in sys.path:
    sys.path.append(models_dir)

# Ruta del archivo del grafo
ruta_grafo = os.path.join(project_root, 'arboles_persistencia', 'grafo_libros.json')

# Función para cargar el grafo desde un archivo JSON
def load_graph_from_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        graph = nx.node_link_graph(data)
        return graph

# Función para visualizar el grafo con colores diferenciados
def visualizar_grafo(graph):
    plt.figure(figsize=(16, 12))
    pos = nx.spring_layout(graph, k=1, iterations=200)

    # Listas para cada tipo de nodo
    libros = [n for n, attrs in graph.nodes(data=True) if attrs.get('tipo') == 'libro']
    autores = [n for n, attrs in graph.nodes(data=True) if attrs.get('tipo') == 'autor']
    generos = [n for n, attrs in graph.nodes(data=True) if attrs.get('tipo') == 'género']
    anios = [n for n, attrs in graph.nodes(data=True) if attrs.get('tipo') == 'año']

    # Dibujar nodos por separado con colores específicos
    nx.draw_networkx_nodes(graph, pos, nodelist=libros, node_color='#db00b6', node_size=400, label='Libros')
    nx.draw_networkx_nodes(graph, pos, nodelist=autores, node_color='#fdb17d', node_size=400, label='Autores')
    nx.draw_networkx_nodes(graph, pos, nodelist=generos, node_color='#fd7de8', node_size=400, label='Géneros')
    nx.draw_networkx_nodes(graph, pos, nodelist=anios, node_color='#7de2fd', node_size=400, label='Años')

    # Dibujar aristas
    nx.draw_networkx_edges(graph, pos, edge_color='gray')

    # Preparar las etiquetas
    texts = []
    for node, (x, y) in pos.items():
        texts.append(plt.text(x, y, node, fontsize=6, ha='center', va='center'))

    # Ajustar las etiquetas para evitar superposición
    adjust_text(texts, arrowprops=dict(arrowstyle='-', color='gray', lw=0.5))

    # Añadir leyenda
    handles = [
        plt.Line2D([], [], color='#db00b6', marker='o', linestyle='', label='Libros'),
        plt.Line2D([], [], color='#fdb17d', marker='o', linestyle='', label='Autores'),
        plt.Line2D([], [], color='#fd7de8', marker='o', linestyle='', label='Géneros'),
        plt.Line2D([], [], color='#7de2fd', marker='o', linestyle='', label='Años')
    ]
    plt.legend(handles=handles, scatterpoints=1)

    plt.title("Grafo de Libros")
    plt.axis('off')
    plt.tight_layout()
    plt.show()

# Función principal
def main():
    # Verificar si el archivo del grafo existe
    if not os.path.exists(ruta_grafo):
        print(f"El archivo {ruta_grafo} no existe. Por favor, genera el grafo primero.")
        return

    # Cargar el grafo desde el archivo JSON
    graph = load_graph_from_json(ruta_grafo)

    # Visualizar el grafo
    visualizar_grafo(graph)

if __name__ == "__main__":
    main()
