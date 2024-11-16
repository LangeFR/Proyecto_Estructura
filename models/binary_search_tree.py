# models/binary_tree.py

class Node:
    def __init__(self, titulo, id=None):
        self.titulo = titulo
        self.id = id
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        # Nodo raíz con titulo 'Biblioteca' y sin id
        self.root = Node(titulo="Biblioteca", id=None)

    def insert(self, id, titulo):
        # Insertar a partir del nodo raíz
        self._insert_recursive(self.root, id, titulo)

    def _insert_recursive(self, node, id, titulo):
        # Si el nodo actual es 'Biblioteca', decidimos dónde insertar
        if node.titulo == "Biblioteca":
            # Si no tiene hijos, insertamos el primer libro a la izquierda
            if node.left is None:
                node.left = Node(titulo, id)
            else:
                self._insert_recursive(node.left, id, titulo)
        else:
            # Comparación de títulos para decidir el lado
            if titulo < node.titulo:
                if node.left is None:
                    node.left = Node(titulo, id)
                else:
                    self._insert_recursive(node.left, id, titulo)
            else:
                if node.right is None:
                    node.right = Node(titulo, id)
                else:
                    self._insert_recursive(node.right, id, titulo)

    # Método para convertir el árbol a un diccionario
    def to_dict(self, node=None):
        if node is None:
            node = self.root
        node_dict = {
            "titulo": node.titulo,
            "id": node.id,
            "left": self.to_dict(node.left) if node.left else None,
            "right": self.to_dict(node.right) if node.right else None
        }
        return node_dict
