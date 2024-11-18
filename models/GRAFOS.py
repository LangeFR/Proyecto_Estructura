import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self):
        self.grafo = nx.Graph()

    def agregar_nodo(self, nodo, tipo=None):
        self.grafo.add_node(nodo, tipo=tipo)
        print(f"Nodo '{nodo}' agregado.")

    def eliminar_nodo(self, nodo):
        if nodo in self.grafo:
            self.grafo.remove_node(nodo)
            print(f"Nodo '{nodo}' eliminado.")
        else:
            print(f"Nodo '{nodo}' no encontrado.")

    def agregar_arista(self, nodo1, nodo2):
        self.grafo.add_edge(nodo1, nodo2)
        print(f"Arista entre '{nodo1}' y '{nodo2}' agregada.")

    def visualizar(self):
        plt.figure(figsize=(8, 6))
        nx.draw(self.grafo, with_labels=True, node_color='lightblue', node_size=2000, font_size=16, font_color='black')
        plt.title("Visualización del Grafo")
        plt.show()

    def recorrer_grafo(self):
        print("Recorriendo el grafo en profundidad:")
        for nodo in nx.dfs_preorder_nodes(self.grafo):
            print(nodo)
