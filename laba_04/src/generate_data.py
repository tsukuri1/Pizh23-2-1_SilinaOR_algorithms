"""
Генерация тестовых данных для анализа алгоритмов сортировки.
"""

import random


def generate_random_array(size, min_val=0, max_val=10000):
    """Генерация массива случайных чисел."""
    return [random.randint(min_val, max_val) for _ in range(size)]


def generate_sorted_array(size, min_val=0, max_val=10000):
    """Генерация отсортированного массива."""
    arr = generate_random_array(size, min_val, max_val)
    arr.sort()
    return arr


def generate_reversed_array(size, min_val=0, max_val=10000):
    """Генерация массива, отсортированного в обратном порядке."""
    arr = generate_sorted_array(size, min_val, max_val)
    arr.reverse()
    return arr


def generate_almost_sorted_array(size, swap_percentage=0.05,
                                 min_val=0, max_val=10000):
    """
    Генерация почти отсортированного массива.
    swap_percentage: процент элементов для случайных перестановок
    """
    arr = generate_sorted_array(size, min_val, max_val)

    # Выбираем случайные индексы для перестановки
    num_swaps = int(size * swap_percentage)
    for _ in range(num_swaps):
        i = random.randint(0, size - 1)
        j = random.randint(0, size - 1)
        arr[i], arr[j] = arr[j], arr[i]

    return arr


def generate_data_sets(sizes):
    """
    Генерация всех типов данных для заданных размеров.

    Возвращает словарь: тип_данных -> размер -> массив
    """
    data_sets = {
        'random': {},
        'sorted': {},
        'reversed': {},
        'almost_sorted': {}
    }

    for size in sizes:
        data_sets['random'][size] = generate_random_array(size)
        data_sets['sorted'][size] = generate_sorted_array(size)
        data_sets['reversed'][size] = generate_reversed_array(size)
        data_sets['almost_sorted'][size] = generate_almost_sorted_array(size)

    return data_sets


if __name__ == "__main__":
    # Пример использования
    sizes = [100, 1000, 5000, 10000]
    data = generate_data_sets(sizes)

    print(f"Сгенерированы массивы размеров: {sizes}")
    print(f"Типы данных: {list(data.keys())}")
    for data_type in data:
        for size in sizes:
            arr = data[data_type][size]
            print(f"{data_type}[{size}]: первые 5 элементов: {arr[:5]}")
