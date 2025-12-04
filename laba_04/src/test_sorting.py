"""
Тесты для проверки корректности реализации алгоритмов сортировки.
"""

import unittest
import random
from sorts import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    quick_sort_optimized
)


class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        """Подготовка тестовых данных."""
        self.test_cases = [
            [],  # пустой массив
            [1],  # один элемент
            [1, 2, 3, 4, 5],  # уже отсортированный
            [5, 4, 3, 2, 1],  # обратно отсортированный
            [3, 1, 4, 1, 5, 9, 2, 6, 5],  # случайный с повторениями
            [64, 34, 25, 12, 22, 11, 90],  # стандартный тест
            [-5, -1, -3, 0, 2, 4, -2],  # с отрицательными числами
        ]

        # Большой случайный массив для производительности
        self.large_array = random.sample(range(10000), 1000)

    def test_bubble_sort(self):
        """Тест сортировки пузырьком."""
        for arr in self.test_cases:
            with self.subTest(arr=arr):
                expected = sorted(arr.copy())
                result = bubble_sort(arr.copy())
                self.assertEqual(result, expected)

    def test_selection_sort(self):
        """Тест сортировки выбором."""
        for arr in self.test_cases:
            with self.subTest(arr=arr):
                expected = sorted(arr.copy())
                result = selection_sort(arr.copy())
                self.assertEqual(result, expected)

    def test_insertion_sort(self):
        """Тест сортировки вставками."""
        for arr in self.test_cases:
            with self.subTest(arr=arr):
                expected = sorted(arr.copy())
                result = insertion_sort(arr.copy())
                self.assertEqual(result, expected)

    def test_merge_sort(self):
        """Тест сортировки слиянием."""
        for arr in self.test_cases:
            with self.subTest(arr=arr):
                expected = sorted(arr.copy())
                result = merge_sort(arr.copy())
                self.assertEqual(result, expected)

    def test_quick_sort(self):
        """Тест быстрой сортировки."""
        for arr in self.test_cases:
            with self.subTest(arr=arr):
                expected = sorted(arr.copy())
                result = quick_sort(arr.copy())
                self.assertEqual(result, expected)

    def test_quick_sort_optimized(self):
        """Тест оптимизированной быстрой сортировки."""
        for arr in self.test_cases:
            with self.subTest(arr=arr):
                expected = sorted(arr.copy())
                result = quick_sort_optimized(arr.copy())
                self.assertEqual(result, expected)

    def test_large_array(self):
        """Тест на большом массиве."""
        for sort_func in [bubble_sort, selection_sort, insertion_sort,
                          merge_sort, quick_sort, quick_sort_optimized]:
            with self.subTest(sort_func=sort_func.__name__):
                arr_copy = self.large_array.copy()
                result = sort_func(arr_copy)
                self.assertEqual(result, sorted(self.large_array.copy()))

    def test_stability_check(self):
        """
        Проверка устойчивости сортировок.
        Устойчивые сортировки сохраняют порядок равных элементов.
        """
        # Создаем массив пар (число, индекс) для проверки устойчивости
        test_arr = [(3, 1), (1, 1), (2, 1), (1, 2), (3, 2), (2, 2)]

        # Функция для проверки сохранения порядка равных элементов
        def check_stability(sorted_arr, original_arr):
            # Для каждого уникального значения проверяем порядок индексов
            value_indices = {}
            for val, idx in sorted_arr:
                if val not in value_indices:
                    value_indices[val] = []
                value_indices[val].append(idx)

            # В устойчивой сортировке индексы должны быть в порядке возрастания
            for val, indices in value_indices.items():
                if indices != sorted(indices):
                    return False
            return True

        # Создаем копию для каждой сортировки
        arr_copy = test_arr.copy()
        result = merge_sort(arr_copy)
        self.assertTrue(check_stability(result, test_arr),
                        "Merge Sort должен быть устойчивым")

        # Bubble Sort тоже устойчив
        arr_copy = test_arr.copy()
        result = bubble_sort(arr_copy)
        self.assertTrue(check_stability(result, test_arr),
                        "Bubble Sort должен быть устойчивым")

        # Insertion Sort тоже устойчив
        arr_copy = test_arr.copy()
        result = insertion_sort(arr_copy)
        self.assertTrue(check_stability(result, test_arr),
                        "Insertion Sort должен быть устойчивым")


if __name__ == '__main__':
    unittest.main(verbosity=2)
