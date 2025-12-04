"""Тестирование реализации кучи."""
import unittest
from heap import MinHeap, MaxHeap
from heapsort import heapsort_inplace
from priority_queue import PriorityQueue


class TestMinHeap(unittest.TestCase):
    """Тесты для MinHeap."""
    def setUp(self):
        self.heap = MinHeap()

    def test_empty_heap(self):
        self.assertTrue(self.heap.is_empty())
        self.assertEqual(self.heap.size(), 0)
        self.assertIsNone(self.heap.peek())
        self.assertIsNone(self.heap.extract())

    def test_insert_and_peek(self):
        self.heap.insert(5)
        self.assertEqual(self.heap.peek(), 5)
        self.assertEqual(self.heap.size(), 1)

        self.heap.insert(3)
        self.assertEqual(self.heap.peek(), 3)
        self.assertEqual(self.heap.size(), 2)

        self.heap.insert(7)
        self.assertEqual(self.heap.peek(), 3)

    def test_extract(self):
        values = [5, 3, 7, 2, 8, 1]
        for val in values:
            self.heap.insert(val)

        expected_order = [1, 2, 3, 5, 7, 8]
        for expected in expected_order:
            self.assertEqual(self.heap.extract(), expected)

        self.assertTrue(self.heap.is_empty())

    def test_build_heap(self):
        array = [9, 5, 3, 7, 2, 8, 1]
        self.heap.build_heap(array)

        self.assertEqual(self.heap.size(), 7)
        self.assertEqual(self.heap.peek(), 1)

        expected_order = [1, 2, 3, 5, 7, 8, 9]
        for expected in expected_order:
            self.assertEqual(self.heap.extract(), expected)


class TestMaxHeap(unittest.TestCase):
    """Тесты для MaxHeap."""
    def setUp(self):
        self.heap = MaxHeap()

    def test_insert_and_extract(self):
        values = [5, 3, 7, 2, 8, 1]
        for val in values:
            self.heap.insert(val)

        expected_order = [8, 7, 5, 3, 2, 1]
        for expected in expected_order:
            self.assertEqual(self.heap.extract(), expected)

    def test_build_heap_max(self):
        array = [9, 5, 3, 7, 2, 8, 1]
        self.heap.build_heap(array)

        self.assertEqual(self.heap.peek(), 9)

        expected_order = [9, 8, 7, 5, 3, 2, 1]
        for expected in expected_order:
            self.assertEqual(self.heap.extract(), expected)


class TestHeapsort(unittest.TestCase):
    """Тесты для Heapsort."""
    def test_heapsort_empty(self):
        array = []
        result = heapsort_inplace(array)
        self.assertEqual(result, [])

    def test_heapsort_single(self):
        array = [5]
        result = heapsort_inplace(array)
        self.assertEqual(result, [5])

    def test_heapsort_sorted(self):
        array = [1, 2, 3, 4, 5]
        result = heapsort_inplace(array)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_heapsort_reverse(self):
        array = [5, 4, 3, 2, 1]
        result = heapsort_inplace(array)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_heapsort_random(self):
        array = [9, 5, 3, 7, 2, 8, 1, 6, 4]
        result = heapsort_inplace(array.copy())
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9])


class TestPriorityQueue(unittest.TestCase):
    """Тесты для PriorityQueue."""
    def setUp(self):
        self.pq = PriorityQueue()

    def test_enqueue_dequeue(self):
        self.pq.enqueue("task1", 3)
        self.pq.enqueue("task2", 1)
        self.pq.enqueue("task3", 2)

        self.assertEqual(self.pq.dequeue(), "task2")
        self.assertEqual(self.pq.dequeue(), "task3")
        self.assertEqual(self.pq.dequeue(), "task1")
        self.assertIsNone(self.pq.dequeue())

    def test_peek(self):
        self.pq.enqueue("task1", 3)
        self.pq.enqueue("task2", 1)

        self.assertEqual(self.pq.peek(), "task2")
        self.assertEqual(self.pq.size(), 2)

    def test_is_empty(self):
        self.assertTrue(self.pq.is_empty())
        self.pq.enqueue("task", 1)
        self.assertFalse(self.pq.is_empty())
        self.pq.dequeue()
        self.assertTrue(self.pq.is_empty())


if __name__ == "__main__":
    unittest.main()
