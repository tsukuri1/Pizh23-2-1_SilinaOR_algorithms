"""Реализация сортировки кучей (Heapsort)."""


def heapsort_inplace(array):
    """In-place сортировка кучей. O(n log n), память O(1)."""
    n = len(array)

    def _sift_down(arr, index, size):
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < size and arr[left] > arr[largest]:
                largest = left

            if right < size and arr[right] > arr[largest]:
                largest = right

            if largest != index:
                arr[index], arr[largest] = arr[largest], arr[index]
                index = largest
            else:
                break

    # Построение max-кучи
    for i in range(n // 2 - 1, -1, -1):
        _sift_down(array, i, n)

    # Извлечение элементов
    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        _sift_down(array, 0, i)

    return array


def test_sorting_algorithms():
    """Тестирование алгоритмов сортировки."""
    import random
    import time

    sizes = [100, 1000, 5000, 10000]

    print("Сравнение алгоритмов сортировки")
    print()
    print(f"{'Размер':<10} {'Heapsort':<15} {'Built-in':<15}")

    for size in sizes:
        data1 = [random.randint(0, 10000) for _ in range(size)]
        data2 = data1[:]

        start = time.time()
        heapsort_inplace(data1)
        time_heap = time.time() - start

        start = time.time()
        sorted(data2)
        time_builtin = time.time() - start

        msg = f"{size:<10} {time_heap:<15.6f} {time_builtin:<15.6f}"
        print(msg)
