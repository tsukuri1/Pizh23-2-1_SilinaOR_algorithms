"""
Реализация 5 алгоритмов сортировки с указанием временной и
пространственной сложности.
"""


def bubble_sort(arr):
    """
    Сортировка пузырьком (Bubble Sort)

    Временная сложность:
        - Худший случай: O(n²)
        - Средний случай: O(n²)
        - Лучший случай: O(n) (уже отсортированный массив с флагом swapped)
    Пространственная сложность: O(1) (in-place)
    """
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def selection_sort(arr):
    """
    Сортировка выбором (Selection Sort)

    Временная сложность:
        - Худший случай: O(n²)
        - Средний случай: O(n²)
        - Лучший случай: O(n²)
    Пространственная сложность: O(1) (in-place)
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    """
    Сортировка вставками (Insertion Sort)

    Временная сложность:
        - Худший случай: O(n²)
        - Средний случай: O(n²)
        - Лучший случай: O(n) (уже отсортированный массив)
    Пространственная сложность: O(1) (in-place)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    """
    Сортировка слиянием (Merge Sort)

    Временная сложность:
        - Худший случай: O(n log n)
        - Средний случай: O(n log n)
        - Лучший случай: O(n log n)
    Пространственная сложность: O(n) (требует дополнительной памяти)
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr


def quick_sort(arr):
    """
    Быстрая сортировка (Quick Sort)

    Временная сложность:
        - Худший случай: O(n²) (плохой выбор опорного элемента)
        - Средний случай: O(n log n)
        - Лучший случай: O(n log n)
    Пространственная сложность: O(log n) в среднем для стека рекурсии
    """
    def _quick_sort_helper(arr, low, high):
        if low < high:
            pi = _partition(arr, low, high)
            _quick_sort_helper(arr, low, pi - 1)
            _quick_sort_helper(arr, pi + 1, high)

    def _partition(arr, low, high):
        # Выбор медианы трех в качестве опорного элемента
        mid = (low + high) // 2
        if arr[high] < arr[low]:
            arr[low], arr[high] = arr[high], arr[low]
        if arr[mid] < arr[low]:
            arr[mid], arr[low] = arr[low], arr[mid]
        if arr[high] < arr[mid]:
            arr[mid], arr[high] = arr[high], arr[mid]
        pivot = arr[mid]

        arr[mid], arr[high] = arr[high], arr[mid]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    if len(arr) <= 1:
        return arr

    _quick_sort_helper(arr, 0, len(arr) - 1)
    return arr


def quick_sort_optimized(arr):
    """
    Оптимизированная быстрая сортировка с переключением на
    insertion sort для малых массивов
    """
    def _quick_sort_opt(arr, low, high):
        while low < high:
            if high - low < 16:  # Порог для переключения
                _insertion_sort_sublist(arr, low, high)
                break

            pi = _partition_opt(arr, low, high)

            # Рекурсивно сортируем меньшую часть, итеративно - большую
            if pi - low < high - pi:
                _quick_sort_opt(arr, low, pi - 1)
                low = pi + 1
            else:
                _quick_sort_opt(arr, pi + 1, high)
                high = pi - 1

    def _partition_opt(arr, low, high):
        mid = (low + high) // 2
        if arr[high] < arr[low]:
            arr[low], arr[high] = arr[high], arr[low]
        if arr[mid] < arr[low]:
            arr[mid], arr[low] = arr[low], arr[mid]
        if arr[high] < arr[mid]:
            arr[mid], arr[high] = arr[high], arr[mid]
        pivot = arr[mid]

        arr[mid], arr[high - 1] = arr[high - 1], arr[mid]
        i = low
        j = high - 1

        while True:
            i += 1
            while arr[i] < pivot:
                i += 1
            j -= 1
            while pivot < arr[j]:
                j -= 1
            if i >= j:
                break
            arr[i], arr[j] = arr[j], arr[i]

        arr[i], arr[high - 1] = arr[high - 1], arr[i]
        return i

    def _insertion_sort_sublist(arr, low, high):
        for i in range(low + 1, high + 1):
            key = arr[i]
            j = i - 1
            while j >= low and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    if len(arr) <= 1:
        return arr

    _quick_sort_opt(arr, 0, len(arr) - 1)
    return arr
