"""Реализация бинарного дерева поиска на основе узлов."""


class TreeNode:
    """Класс узла для бинарного дерева поиска."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class BinarySearchTree:
    """Реализация бинарного дерева поиска."""
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Вставить значение в БДП. O(log n) средняя, O(n) худшая."""
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if node is None:
            return TreeNode(value)
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))
        return node

    def insert_iterative(self, value):
        """Итеративная вставка для избежания рекурсии."""
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        parent = None

        while current:
            parent = current
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return  # Значение уже существует

        if value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        # Обновление высот
        self._update_heights(parent)

    def _update_heights(self, node):
        """Обновить высоты начиная с узла до корня."""
        while node:
            node.height = 1 + max(self._get_height(node.left),
                                  self._get_height(node.right))
            node = self._get_parent(node)

    def _get_parent(self, child):
        """Найти родительский узел для данного узла."""
        if child == self.root:
            return None

        current = self.root

        while current:
            if child.value < current.value:
                if current.left == child:
                    return current
                current = current.left
            else:
                if current.right == child:
                    return current
                current = current.right
        return None

    def search(self, value):
        """Найти значение в БДП. O(log n) средняя, O(n) худшая."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def search_iterative(self, value):
        """Итеративный поиск."""
        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def delete(self, value):
        """Удалить значение из БДП. O(log n) средняя, O(n) худшая."""
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None and node.right is None:
                return None
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            successor = self.find_min(node.right)
            node.value = successor.value
            node.right = self._delete_recursive(node.right, successor.value)
        if node:
            node.height = 1 + max(self._get_height(node.left),
                                  self._get_height(node.right))
        return node

    def find_min(self, node=None):
        """Найти минимальное значение в поддереве. O(h)."""
        if node is None:
            node = self.root
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node

    def find_max(self, node=None):
        """Найти максимальное значение в поддереве. O(h)."""
        if node is None:
            node = self.root
        if node is None:
            return None
        while node.right is not None:
            node = node.right
        return node

    def is_valid_bst(self):
        """Проверить, является ли дерево корректным БДП. O(n)."""
        return self._validate_recursive(self.root, float('-inf'), float('inf'))

    def _validate_recursive(self, node, min_val, max_val):
        if node is None:
            return True
        if not (min_val < node.value < max_val):
            return False
        return (self._validate_recursive(node.left, min_val, node.value) and
                self._validate_recursive(node.right, node.value, max_val))

    def get_height(self, node=None):
        """Получить высоту дерева или поддерева. O(1)."""
        if node is None:
            node = self.root
        return node.height if node else 0

    def _get_height(self, node):
        return node.height if node else 0

    def visualize(self, node=None, level=0, prefix="Root: "):
        """Текстовая визуализация дерева."""
        if node is None:
            node = self.root
        if node is None:
            print("Дерево пустое")
            return
        indent = "    " * level
        print(f"{indent}{prefix}{node.value} (h={node.height})")
        if node.left:
            self.visualize(node.left, level + 1, "L: ")
        if node.right:
            self.visualize(node.right, level + 1, "R: ")
