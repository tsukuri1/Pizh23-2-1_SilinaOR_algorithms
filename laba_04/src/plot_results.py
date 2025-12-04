"""
Визуализация результатов тестирования алгоритмов сортировки.
"""

import matplotlib.pyplot as plt
import numpy as np
import csv
from performance_test import test_all_algorithms, generate_data_sets
from sorts import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort_optimized
)


def plot_time_vs_size(results, data_type='random'):
    """
    График зависимости времени от размера массива для каждого алгоритма.
    """
    plt.figure(figsize=(12, 8))

    algorithms = list(results.keys())
    sizes = sorted(list(next(iter(results.values()))[data_type].keys()))

    for algo_name in algorithms:
        times = [results[algo_name][data_type][size] for size in sizes]
        plt.plot(sizes, times, marker='o', label=algo_name, linewidth=2)

    plt.xlabel('Размер массива (n)', fontsize=12)
    plt.ylabel('Время выполнения (секунды)', fontsize=12)
    title = f'Зависимость времени от размера массива ({data_type} данные)'
    plt.title(title, fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(fontsize=10)
    plt.yscale('log')
    plt.xscale('log')

    plt.tight_layout()
    filename = f'time_vs_size_{data_type}.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.show()


def plot_time_vs_datatype(results, size=5000):
    """
    График зависимости времени от типа данных для фиксированного размера.
    """
    plt.figure(figsize=(12, 8))

    algorithms = list(results.keys())
    data_types = ['random', 'sorted', 'reversed', 'almost_sorted']

    x = np.arange(len(data_types))
    width = 0.15

    fig, ax = plt.subplots(figsize=(12, 8))

    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
              '#9467bd', '#8c564b']
    for i, algo_name in enumerate(algorithms):
        times = [results[algo_name][data_type].get(size, 0)
                 for data_type in data_types]
        pos = x + i*width - (len(algorithms)-1)*width/2
        ax.bar(pos, times, width, label=algo_name,
               color=colors[i % len(colors)])

    ax.set_xlabel('Тип данных', fontsize=12)
    ax.set_ylabel('Время выполнения (секунды)', fontsize=12)
    ax.set_title(f'Сравнение времени выполнения для n={size}', fontsize=14)
    ax.set_xticks(x)
    labels = ['Случайные', 'Отсортированные',
              'Обратные', 'Почти отсорт.']
    ax.set_xticklabels(labels)
    ax.legend(fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.6, axis='y')

    plt.tight_layout()
    filename = f'time_vs_datatype_size{size}.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.show()


def create_summary_table(results):
    """
    Создание сводной таблицы результатов.
    """
    data_types = ['random', 'sorted', 'reversed', 'almost_sorted']
    sizes = sorted(list(next(iter(results.values()))['random'].keys()))

    print("\n")
    print("Сводная таблица результатов")
    print("")

    for data_type in data_types:
        print(f"\n{data_type} данные:")
        print("")
        print(f"{'Алгоритм':<25}", end="")
        for size in sizes:
            print(f"{'n=' + str(size):>12}", end="")
        print()

        for algo_name in results:
            print(f"{algo_name:<25}", end="")
            for size in sizes:
                time_val = results[algo_name][data_type][size]
                print(f"{time_val:>12.6f}", end="")
            print()


def save_results_to_csv(results, filename='results.csv'):
    """
    Сохранение результатов в CSV файл.

    Args:
        results: словарь с результатами тестирования
        filename: имя файла для сохранения
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


def plot_comparison_line(results):
    """
    Сравнительный график всех алгоритмов на разных типах данных.
    """
    data_types = ['random', 'sorted', 'reversed', 'almost_sorted']
    data_types_rus = ['Случайные', 'Отсортированные',
                      'Обратные', 'Почти отсорт.']
    algorithms = list(results.keys())

    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    axes = axes.flatten()

    colors = ['#1f77b4', '#ff7f0e', '#2ca02c',
              '#d62728', '#9467bd', '#8c564b']

    for idx, (data_type, data_type_rus) in enumerate(zip(data_types,
                                                         data_types_rus)):
        ax = axes[idx]
        sizes = sorted(list(next(iter(results.values()))[data_type].keys()))

        for i, algo_name in enumerate(algorithms):
            times = [results[algo_name][data_type][size] for size in sizes]
            ax.plot(sizes, times, marker='o', label=algo_name,
                    linewidth=2, color=colors[i % len(colors)])

        ax.set_xlabel('Размер массива (n)', fontsize=10)
        ax.set_ylabel('Время (сек)', fontsize=10)
        ax.set_title(f'{data_type_rus} данные', fontsize=12)
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.set_xscale('log')
        ax.set_yscale('log')

        if idx == 0:
            ax.legend(fontsize=9)

    plt.tight_layout()
    plt.savefig('all_comparisons.png', dpi=300, bbox_inches='tight')
    plt.show()


def create_detailed_report_from_csv():
    """
    Создание детализированного отчета на основе CSV файла.
    """
    try:
        with open('results.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)

        if len(data) < 2:
            print("Файл results.csv пуст или содержит только заголовок")
            return

        header = data[0]
        sizes = [int(col[2:]) for col in header[2:]]

        results = {}
        for row in data[1:]:
            algo = row[0]
            data_type = row[1]
            times = [float(x) for x in row[2:]]

            if algo not in results:
                results[algo] = {}
            results[algo][data_type] = dict(zip(sizes, times))

        print("\n")
        print("Итоговый отчет по тестированию алгоритмов сортировки")
        print("")

        print("\nАнализ производительности:")
        print("")

        for size in sizes:
            print(f"\nДля размера массива n={size}:")
            header_line = (f"{'Алгоритм':<25} {'Случайные':>12} "
                           f"{'Отсорт.':>12} {'Обратные':>12} "
                           f"{'Почти отсорт.':>12}")
            print(header_line)
            print("")

            for algo in results:
                times = []
                for data_type in ['random', 'sorted', 'reversed',
                                  'almost_sorted']:
                    time_val = results[algo][data_type].get(size, 0)
                    times.append(time_val)

                print(f"{algo:<25} {times[0]:>12.6f} {times[1]:>12.6f} "
                      f"{times[2]:>12.6f} {times[3]:>12.6f}")

        print("\n\nЛучшие алгоритмы для каждого типа данных:")
        print("")

        data_types = ['random', 'sorted', 'reversed', 'almost_sorted']
        data_types_rus = ['Случайные', 'Отсортированные',
                          'Обратные', 'Почти отсортированные']

        for size in sizes:
            print(f"\nПри n={size}:")
            for data_type, data_type_rus in zip(data_types, data_types_rus):
                best_algo = None
                best_time = float('inf')

                for algo in results:
                    time_val = results[algo][data_type].get(size, 0)
                    if time_val < best_time:
                        best_time = time_val
                        best_algo = algo

                print(f"  {data_type_rus:<20}: {best_algo:<20} "
                      f"({best_time:.6f} сек)")

    except FileNotFoundError:
        print("Ошибка: файл results.csv не найден.")
        print("Сначала запустите performance_test.py или plot_results.py")


if __name__ == "__main__":
    plt.style.use('default')

    algorithms = {
        'Bubble Sort': bubble_sort,
        'Selection Sort': selection_sort,
        'Insertion Sort': insertion_sort,
        'Merge Sort': merge_sort,
        'Quick Sort': quick_sort_optimized
    }

    sizes = [100, 500, 1000, 5000]

    print("Генерация данных и тестирование...")
    data_sets = generate_data_sets(sizes)
    results = test_all_algorithms(data_sets, sizes, algorithms)

    save_results_to_csv(results, 'results.csv')

    print("\nПостроение графиков...")

    plot_time_vs_size(results, 'random')
    plot_time_vs_size(results, 'sorted')
    plot_time_vs_size(results, 'reversed')
    plot_time_vs_size(results, 'almost_sorted')
    plot_time_vs_datatype(results, size=5000)
    plot_comparison_line(results)

    create_summary_table(results)
    create_detailed_report_from_csv()

    print("\nВсе графики сохранены в PNG файлы.")
