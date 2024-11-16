

class Node:
    def __init__(self, book):
        self.book = book  # Diccionario que contiene 'id' y 'titulo'
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, book):
        if not self.root:
            self.root = Node(book)
        else:
            self._insert_recursive(self.root, book)

    def _insert_recursive(self, node, book):
        if book['titulo'] < node.book['titulo']:
            if node.left is None:
                node.left = Node(book)
            else:
                self._insert_recursive(node.left, book)
        else:
            if node.right is None:
                node.right = Node(book)
            else:
                self._insert_recursive(node.right, book)

    def search(self, titulo):
        return self._search_recursive(self.root, titulo)

    def _search_recursive(self, node, titulo):
        if node is None:
            return None
        if titulo == node.book['titulo']:
            return node.book
        elif titulo < node.book['titulo']:
            return self._search_recursive(node.left, titulo)
        else:
            return self._search_recursive(node.right, titulo)

    def tree_to_dict(self):
        return self._tree_to_dict_recursive(self.root)

    def _tree_to_dict_recursive(self, node):
        if node is None:
            return None
        return {
            "book": node.book,
            "left": self._tree_to_dict_recursive(node.left),
            "right": self._tree_to_dict_recursive(node.right)
        }
