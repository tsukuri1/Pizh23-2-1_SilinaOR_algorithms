"""Анализ производительности операций БДП."""
import random
import time
import matplotlib.pyplot as plt
import platform
import sys
from binary_search_tree import BinarySearchTree


def create_random_tree(size, use_iterative=False):
    """Создать сбалансированное дерево случайными элементами."""
    tree = BinarySearchTree()
    elements = list(range(size))
    random.shuffle(elements)
    if use_iterative:
        for element in elements:
            tree.insert_iterative(element)
    else:
        for element in elements:
            tree.insert(element)
    return tree


def create_degenerate_tree(size, use_iterative=True):
    """Создать вырожденное дерево отсортированными элементами."""
    tree = BinarySearchTree()
    if use_iterative:
        for element in range(size):
            tree.insert_iterative(element)
    else:
        sys.setrecursionlimit(max(1000, size * 2))
        for element in range(size):
            tree.insert(element)
    return tree


def measure_search_time(tree, search_count, use_iterative=False):
    """Измерить среднее время поиска в дереве."""
    values = [random.randint(0, search_count * 2)
              for _ in range(search_count)]

    start_time = time.time()
    if use_iterative:
        for value in values:
            tree.search_iterative(value)
    else:
        for value in values:
            tree.search(value)
    end_time = time.time()

    return (end_time - start_time) / search_count


def run_experiment(max_size=500, step=50):
    """Провести эксперимент по измерению производительности."""
    sizes = list(range(step, max_size + 1, step))
    balanced_times = []
    degenerate_times = []

    print("\nЭкспериментальное исследование")
    print()
    print("Проведение эксперимента...")
    header1 = "Размер | Время сбалансированного | "
    header2 = "Время вырожденного | Отношение"
    print(header1 + header2)

    for size in sizes:
        balanced = create_random_tree(size, use_iterative=False)
        degenerate = create_degenerate_tree(size, use_iterative=True)

        time_balanced = measure_search_time(
            balanced, 1000, use_iterative=False)
        time_degenerate = measure_search_time(
            degenerate, 1000, use_iterative=True)

        balanced_times.append(time_balanced)
        degenerate_times.append(time_degenerate)

        ratio = time_degenerate / time_balanced if time_balanced > 0 else 0

        msg = f"{size:6d} | {time_balanced:21.6e} | "
        msg += f"{time_degenerate:18.6e} | {ratio:8.2f}"
        print(msg)

    plot_graphs(sizes, balanced_times, degenerate_times)


def plot_graphs(sizes, balanced_times, degenerate_times):
    """Построить графики зависимости времени от размера."""
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(sizes, balanced_times, 'b-',
             label='Сбалансированное', linewidth=2)
    plt.plot(sizes, degenerate_times, 'r-',
             label='Вырожденное', linewidth=2)
    plt.xlabel('Размер дерева (n)')
    plt.ylabel('Среднее время поиска (сек)')
    plt.title('Зависимость времени поиска от размера дерева')
    plt.grid(True, alpha=0.3)
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.loglog(sizes, balanced_times, 'b-',
               label='Сбалансированное', linewidth=2)
    plt.loglog(sizes, degenerate_times, 'r-',
               label='Вырожденное', linewidth=2)
    plt.xlabel('Размер дерева (n) - логарифмическая шкала')
    plt.ylabel('Время поиска (сек) - логарифмическая шкала')
    plt.title('Логарифмический масштаб')
    plt.grid(True, alpha=0.3)
    plt.legend()

    plt.tight_layout()
    plt.savefig('результаты_производительности.png', dpi=150)
    plt.show()


def print_pc_specs():
    """Вывести характеристики компьютера для тестирования."""
    print("\nХарактеристики компьютера для тестирования")
    print()
    print(f"Система: {platform.system()} {platform.release()}")
    print(f"Процессор: {platform.processor()}")
    print(f"Архитектура: {platform.machine()}")
    print(f"Python версия: {sys.version.split()[0]}")
    print(f"Платформа: {platform.platform()}")


def main():
    """Основная функция демонстрации."""
    print("Демонстрация работы бинарного дерева поиска")
    print()

    tree = BinarySearchTree()
    elements = [50, 30, 70, 20, 40, 60, 80]

    print(f"Вставляем элементы: {elements}")
    for element in elements:
        tree.insert(element)

    print("\nВизуализация дерева:")
    tree.visualize()

    print(f"\nВысота дерева: {tree.get_height()}")
    print(f"Минимум: {tree.find_min().value}")
    print(f"Максимум: {tree.find_max().value}")
    print(f"Корректное БДП: {tree.is_valid_bst()}")

    from tree_traversal import inorder_recursive, inorder_iterative
    print(f"\nОбход in-order (рекурсивно): {inorder_recursive(tree.root)}")
    print(f"Обход in-order (итеративно): {inorder_iterative(tree.root)}")

    run_experiment(max_size=500, step=50)
    print_pc_specs()


if __name__ == "__main__":
    main()
