"""Реализация приоритетной очереди на основе кучи."""
from heap import MinHeap


class PriorityQueue:
    """Приоритетная очередь (меньшее число = выше приоритет)."""
    def __init__(self):
        self.heap = MinHeap()

    def enqueue(self, item, priority):
        """Добавить элемент. O(log n)."""
        self.heap.insert((priority, item))

    def dequeue(self):
        """Извлечь элемент с наивысшим приоритетом. O(log n)."""
        result = self.heap.extract()
        return result[1] if result else None

    def peek(self):
        """Посмотреть элемент с наивысшим приоритетом. O(1)."""
        result = self.heap.peek()
        return result[1] if result else None

    def is_empty(self):
        return self.heap.is_empty()

    def size(self):
        return self.heap.size()


def demo_priority_queue():
    """Демонстрация работы приоритетной очереди."""
    print("Демонстрация приоритетной очереди")
    print()

    pq = PriorityQueue()

    tasks = [
        ("Помыть посуду", 3),
        ("Сделать домашку", 1),
        ("Посмотреть фильм", 5),
        ("Сходить в магазин", 2),
    ]

    for task, priority in tasks:
        pq.enqueue(task, priority)
        print(f"Добавлено: {task} (приоритет: {priority})")

    print()
    print("Извлечение задач по приоритету:")

    while not pq.is_empty():
        task = pq.dequeue()
        print(f"  Выполняем: {task}")
