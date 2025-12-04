"""Реализация структуры данных "куча" на основе массива."""


class MinHeap:
    """Min-куча (наименьший элемент в корне)."""
    def __init__(self):
        self.heap = []

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _sift_up(self, index):
        """Всплытие элемента. O(log n)."""
        parent = self._parent(index)
        while index > 0 and self.heap[index] < self.heap[parent]:
            self._swap(index, parent)
            index = parent
            parent = self._parent(index)

    def _sift_down(self, index):
        """Погружение элемента. O(log n)."""
        size = len(self.heap)
        while True:
            left = self._left_child(index)
            right = self._right_child(index)
            smallest = index

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self._swap(index, smallest)
                index = smallest
            else:
                break

    def insert(self, value):
        """Вставить элемент. O(log n)."""
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def extract(self):
        """Извлечь минимальный элемент. O(log n)."""
        if not self.heap:
            return None

        root = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._sift_down(0)

        return root

    def peek(self):
        """Посмотреть минимальный элемент. O(1)."""
        return self.heap[0] if self.heap else None

    def build_heap(self, array):
        """Построить кучу из массива. O(n)."""
        self.heap = array[:]
        n = len(self.heap)
        start_index = (n - 2) // 2

        for i in range(start_index, -1, -1):
            self._sift_down(i)

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0


class MaxHeap:
    """Max-куча (наибольший элемент в корне)."""
    def __init__(self):
        self.heap = []

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _sift_up(self, index):
        """Всплытие для max-кучи. O(log n)."""
        parent = self._parent(index)
        while index > 0 and self.heap[index] > self.heap[parent]:
            self._swap(index, parent)
            index = parent
            parent = self._parent(index)

    def _sift_down(self, index):
        """Погружение для max-кучи. O(log n)."""
        size = len(self.heap)
        while True:
            left = self._left_child(index)
            right = self._right_child(index)
            largest = index

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left

            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != index:
                self._swap(index, largest)
                index = largest
            else:
                break

    def insert(self, value):
        """Вставить элемент. O(log n)."""
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def extract(self):
        """Извлечь максимальный элемент. O(log n)."""
        if not self.heap:
            return None

        root = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._sift_down(0)

        return root

    def peek(self):
        """Посмотреть максимальный элемент. O(1)."""
        return self.heap[0] if self.heap else None

    def build_heap(self, array):
        """Построить кучу из массива. O(n)."""
        self.heap = array[:]
        n = len(self.heap)
        start_index = (n - 2) // 2

        for i in range(start_index, -1, -1):
            self._sift_down(i)

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0
