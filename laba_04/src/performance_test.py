"""
Тестирование производительности алгоритмов сортировки.
"""

import timeit
import copy
import csv
from sorts import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    quick_sort_optimized
)
from generate_data import generate_data_sets


def measure_sorting_time(sort_func, arr, number_of_runs=1):
    """
    Измерение времени выполнения функции сортировки.

    Args:
        sort_func: функция сортировки
        arr: массив для сортировки
        number_of_runs: количество запусков для усреднения

    Returns:
        Время выполнения в секундах
    """
    test_arr = copy.deepcopy(arr)
    timer = timeit.Timer(lambda: sort_func(copy.deepcopy(test_arr)))
    time_taken = timer.timeit(number=number_of_runs) / number_of_runs
    return time_taken


def test_all_algorithms(data_sets, sizes, algorithms):
    """
    Тестирование всех алгоритмов на всех типах данных и размерах.

    Returns:
        Словарь результатов: алгоритм -> тип_данных -> размер -> время
    """
    results = {algo_name: {data_type: {} for data_type in data_sets}
               for algo_name in algorithms.keys()}

    for algo_name, algo_func in algorithms.items():
        print(f"\nТестирование {algo_name}...")

        for data_type in data_sets:
            print(f"  Тип данных: {data_type}")

            for size in sizes:
                arr = data_sets[data_type][size]

                if size <= 1000:
                    runs = 5
                elif size <= 5000:
                    runs = 3
                else:
                    runs = 1

                time_taken = measure_sorting_time(algo_func, arr, runs)
                results[algo_name][data_type][size] = time_taken

                print(f"    Размер {size}: {time_taken:.6f} секунд")

    return results


def save_results_to_csv(results, filename='results.csv'):
    """
    Сохранение результатов в CSV файл.
    """
    data_types = ['random', 'sorted', 'reversed', 'almost_sorted']
    sizes = sorted(list(next(iter(results.values()))['random'].keys()))
    algorithms = list(results.keys())

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        header = ['Алгоритм', 'Тип данных'] + [f'n={size}' for size in sizes]
        writer.writerow(header)

        for algo_name in algorithms:
            for data_type in data_types:
                row = [algo_name, data_type]
                for size in sizes:
                    time_val = results[algo_name][data_type].get(size, 0)
                    row.append(f"{time_val:.6f}")
                writer.writerow(row)

    print(f"\nРезультаты сохранены в файл: {filename}")


def verify_sorting_correctness(algorithms):
    """Проверка корректности сортировки всех алгоритмов."""
    print("Проверка корректности сортировки...")

    test_cases = [
        ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
        ([5, 2, 8, 1, 9], [1, 2, 5, 8, 9]),
        ([1], [1]),
        ([], []),
        ([3, 3, 3, 3], [3, 3, 3, 3]),
        ([5, -3, 2, -8, 1], [-8, -3, 1, 2, 5])
    ]

    all_correct = True

    for algo_name, algo_func in algorithms.items():
        print(f"\n{algo_name}:")
        for i, (input_arr, expected) in enumerate(test_cases):
            arr_copy = copy.deepcopy(input_arr)
            result = algo_func(arr_copy)

            if result == expected:
                print(f"  Тест {i+1}: ✓")
            else:
                print(f"  Тест {i+1}: ✗ (ожидалось {expected}, "
                      f"получено {result})")
                all_correct = False

    if all_correct:
        print("\nВсе алгоритмы работают корректно!")
    else:
        print("\nНекоторые алгоритмы работают некорректно!")

    return all_correct


if __name__ == "__main__":
    algorithms = {
        'Bubble Sort': bubble_sort,
        'Selection Sort': selection_sort,
        'Insertion Sort': insertion_sort,
        'Merge Sort': merge_sort,
        'Quick Sort': quick_sort,
        'Quick Sort (оптимизированный)': quick_sort_optimized
    }

    sizes = [100, 500, 1000, 5000, 10000]

    print("Генерация тестовых данных...")
    data_sets = generate_data_sets(sizes)

    verify_sorting_correctness(algorithms)

    print("\n")
    print("Начало тестирования производительности")
    print("")

    results = test_all_algorithms(data_sets, sizes, algorithms)

    save_results_to_csv(results, 'results.csv')

    print("\n")
    print("Сводная таблица (случайные данные):")
    print("")
    print(f"{'Алгоритм':<25}", end="")
    for size in sizes:
        print(f"{size:>10}", end="")
    print()

    for algo_name in algorithms:
        print(f"{algo_name:<25}", end="")
        for size in sizes:
            time_val = results[algo_name]['random'][size]
            print(f"{time_val:>10.6f}", end="")
        print()
