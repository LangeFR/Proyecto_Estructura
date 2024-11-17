class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, vertice):
        self.vertices[vertice] = []

    def agregar_arista(self, origen, destino):
        if origen in self.vertices and destino in self.vertices:
            self.vertices[origen].append(destino)
            self.vertices[destino].append(origen)  # Para grafos no dirigidos

    def mostrar_grafo(self):
        for vertice in self.vertices:
            print(vertice, "->", self.vertices[vertice])

    def dfs(self, inicio, visitados=None):
        if visitados is None:
            visitados = set()
        visitados.add(inicio)
        print(inicio, end=' ')
        for vecino in self.vertices[inicio]:
            if vecino not in visitados:
                self.dfs(vecino, visitados)

    def bfs(self, inicio):
        visitados = set()
        cola = [inicio]
        while cola:
            vertice = cola.pop(0)
            if vertice not in visitados:
                print(vertice, end=' ')
                visitados.add(vertice)
                for vecino in self.vertices[vertice]:
                    cola.append(vecino)