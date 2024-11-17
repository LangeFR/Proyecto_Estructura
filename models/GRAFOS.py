import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self):
        self.grafo = nx.Graph()

    def agregar_nodo(self, nodo):
        self.grafo.add_node(nodo)
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

def main():
    grafo = Grafo()

    while True:
        print("\nOpciones:")
        print("1. Agregar nodo")
        print("2. Eliminar nodo")
        print("3. Agregar arista")
        print("4. Visualizar grafo")
        print("5. Recorrer grafo")
        print("6. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nodo = input("Ingresa el nombre del nodo a agregar: ")
            grafo.agregar_nodo(nodo)
        elif opcion == '2':
            nodo = input("Ingresa el nombre del nodo a eliminar: ")
            grafo.eliminar_nodo(nodo)
        elif opcion == '3':
            nodo1 = input("Ingresa el nombre del primer nodo: ")
            nodo2 = input("Ingresa el nombre del segundo nodo: ")
            grafo.agregar_arista(nodo1, nodo2)
        elif opcion == '4':
            grafo.visualizar()
        elif opcion == '5':
            grafo.recorrer_grafo()
        elif opcion == '6':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
