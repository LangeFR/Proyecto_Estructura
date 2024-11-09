class NAryNode:
    def __init__(self, value):
        self.value = value
        self.children = []

class NAryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = NAryNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if not node.children:
                node.children.append(NAryNode(value))
            else:
                self._insert_recursive(node.children[0], value)
        else:
            if len(node.children) < 3:  # Limitamos a 3 hijos por nodo
                node.children.append(NAryNode(value))
            else:
                self._insert_recursive(node.children[-1], value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if not node:
            return None
        if node.value == value:
            return node
        for child in node.children:
            result = self._search_recursive(child, value)
            if result:
                return result
        return None

    def delete(self, value):
        if not self.root:
            return False
        if self.root.value == value:
            if not self.root.children:
                self.root = None
            else:
                self.root = self.root.children[0]
            return True
        return self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        for i, child in enumerate(node.children):
            if child.value == value:
                node.children.pop(i)
                return True
            if self._delete_recursive(child, value):
                return True
        return False

    def __str__(self):
        if not self.root:
            return "Árbol vacío"
        return self._str_recursive(self.root, 0)

    def _str_recursive(self, node, level):
        result = "  " * level + str(node.value) + "\n"
        for child in node.children:
            result += self._str_recursive(child, level + 1)
        return result
