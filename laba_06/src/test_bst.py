"""Тестирование реализации бинарного дерева поиска."""
import unittest
from binary_search_tree import BinarySearchTree
from tree_traversal import (
    inorder_recursive,
    inorder_iterative,
    preorder_recursive,
    postorder_recursive,
    breadth_first
)


class TestBST(unittest.TestCase):
    """Тесты для бинарного дерева поиска."""
    def setUp(self):
        self.tree = BinarySearchTree()

    def test_insert_and_search(self):
        elements = [50, 30, 70, 20, 40, 60, 80]
        for element in elements:
            self.tree.insert(element)

        for element in elements:
            self.assertTrue(self.tree.search(element))

        self.assertFalse(self.tree.search(100))
        self.assertFalse(self.tree.search(10))

    def test_delete(self):
        elements = [50, 30, 70, 20, 40, 60, 80]
        for element in elements:
            self.tree.insert(element)

        self.tree.delete(20)
        self.assertFalse(self.tree.search(20))

        self.tree.insert(25)
        self.tree.delete(30)
        self.assertFalse(self.tree.search(30))

        self.tree.delete(50)
        self.assertFalse(self.tree.search(50))

        self.assertTrue(self.tree.is_valid_bst())

    def test_find_min_max(self):
        elements = [50, 30, 70, 20, 40, 60, 80]
        for element in elements:
            self.tree.insert(element)

        minimum = self.tree.find_min()
        maximum = self.tree.find_max()

        self.assertIsNotNone(minimum)
        self.assertIsNotNone(maximum)
        self.assertEqual(minimum.value, 20)
        self.assertEqual(maximum.value, 80)

    def test_is_valid_bst(self):
        self.tree.insert(50)
        self.tree.insert(30)
        self.tree.insert(70)
        self.assertTrue(self.tree.is_valid_bst())

        empty_tree = BinarySearchTree()
        self.assertTrue(empty_tree.is_valid_bst())

    def test_height(self):
        self.assertEqual(self.tree.get_height(), 0)

        self.tree.insert(50)
        self.assertEqual(self.tree.get_height(), 1)

        self.tree.insert(30)
        self.tree.insert(70)
        self.assertEqual(self.tree.get_height(), 2)

        self.tree.insert(20)
        self.tree.insert(40)
        self.assertEqual(self.tree.get_height(), 3)


class TestTraversals(unittest.TestCase):
    """Тесты для алгоритмов обхода дерева."""
    def setUp(self):
        self.tree = BinarySearchTree()
        elements = [50, 30, 70, 20, 40, 60, 80]
        for element in elements:
            self.tree.insert(element)

    def test_inorder(self):
        recursive = inorder_recursive(self.tree.root)
        iterative = inorder_iterative(self.tree.root)
        expected = [20, 30, 40, 50, 60, 70, 80]

        self.assertEqual(recursive, expected)
        self.assertEqual(iterative, expected)

    def test_preorder(self):
        result = preorder_recursive(self.tree.root)
        self.assertEqual(len(result), 7)
        self.assertEqual(set(result), set(range(20, 81, 10)))

    def test_postorder(self):
        result = postorder_recursive(self.tree.root)
        self.assertEqual(len(result), 7)
        self.assertEqual(set(result), set(range(20, 81, 10)))
        self.assertEqual(result[-1], 50)

    def test_breadth_first(self):
        result = breadth_first(self.tree.root)
        self.assertEqual(result[0], 50)
        self.assertEqual(len(result), 7)
        self.assertEqual(set(result), set(range(20, 81, 10)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
