
class AVLNode:
    def __init__(self, anio_publicacion, libro_id):
        self.anio_publicacion = anio_publicacion
        self.libros = [libro_id]  # Lista de IDs de libros para este año
        self.left = None
        self.right = None
        self.height = 1

class BalancedTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        if not node:
            return
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self.update_height(y)
        self.update_height(x)
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self.update_height(x)
        self.update_height(y)
        return y

    def insert(self, anio_publicacion, libro_id):
        self.root = self._insert_recursive(self.root, anio_publicacion, libro_id)

    def _insert_recursive(self, node, anio_publicacion, libro_id):
        if not node:
            return AVLNode(anio_publicacion, libro_id)

        if anio_publicacion == node.anio_publicacion:
            # Si el año ya existe, agregar el ID del libro a la lista
            node.libros.append(libro_id)
        elif anio_publicacion < node.anio_publicacion:
            node.left = self._insert_recursive(node.left, anio_publicacion, libro_id)
        else:
            node.right = self._insert_recursive(node.right, anio_publicacion, libro_id)

        self.update_height(node)
        balance = self.balance_factor(node)

        # Balancear el árbol
        if balance > 1:
            if anio_publicacion < node.left.anio_publicacion:
                return self.right_rotate(node)
            if anio_publicacion > node.left.anio_publicacion:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)

        if balance < -1:
            if anio_publicacion > node.right.anio_publicacion:
                return self.left_rotate(node)
            if anio_publicacion < node.right.anio_publicacion:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)

        return node

    def to_dict(self, node=None):
        if node is None:
            node = self.root
        if not node:
            return None

        return {
            "anio_publicacion": node.anio_publicacion,
            "libros": node.libros,
            "left": self.to_dict(node.left) if node.left else None,
            "right": self.to_dict(node.right) if node.right else None,
        }

