# models/binary_tree.py

class Node:
    def __init__(self, titulo, id=None):
        self.titulo = titulo
        self.id = id
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None  # Sin nodo raíz inicial

    def insert(self, id, titulo):
        if self.root is None:
            # Si el árbol no tiene raíz, el primer nodo insertado se convierte en la raíz
            self.root = Node(titulo, id)
        else:
            self._insert_recursive(self.root, id, titulo)

    def _insert_recursive(self, node, id, titulo):
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
        if node is None:
            return None  # El árbol está vacío
        node_dict = {
            "titulo": node.titulo,
            "id": node.id,
            "left": self.to_dict(node.left) if node.left else None,
            "right": self.to_dict(node.right) if node.right else None
        }
        return node_dict
