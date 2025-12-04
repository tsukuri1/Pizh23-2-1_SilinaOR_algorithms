"""
Сравнительный анализ жадных алгоритмов и точных методов.
"""

import time
import random
from typing import List, Tuple
from itertools import combinations
from greedy_algorithms import (
    interval_scheduling,
    fractional_knapsack,
    huffman_coding,
    min_coins_greedy,
    kruskal_mst
)


def brute_force_knapsack_01(
    items: List[Tuple[float, float]], capacity: float
) -> float:
    """
    Точное решение задачи о рюкзаке 0-1 методом полного перебора.

    Args:
        items: Список предметов (вес, цена)
        capacity: Вместимость рюкзака

    Returns:
        Максимальная стоимость
    """
    n = len(items)
    max_value = 0

    for r in range(1, n + 1):
        for combo in combinations(range(n), r):
            total_weight = sum(items[i][0] for i in combo)
            total_value = sum(items[i][1] for i in combo)

            if total_weight <= capacity and total_value > max_value:
                max_value = total_value

    return max_value


def compare_knapsack_algorithms():
    """Сравнивает жадный и точный алгоритмы для задачи о рюкзаке."""
    print("Сравнение алгоритмов для задачи о рюкзаке")

    items = [(10, 60), (20, 100), (30, 120)]
    capacity = 50

    frac_value, _ = fractional_knapsack(items, capacity)

    items_sorted = sorted(items, key=lambda x: x[1]/x[0], reverse=True)
    greedy_01_value = 0
    greedy_01_weight = 0

    for weight, value in items_sorted:
        if greedy_01_weight + weight <= capacity:
            greedy_01_value += value
            greedy_01_weight += weight

    exact_01_value = brute_force_knapsack_01(items, capacity)

    print(f"Предметы: {items}")
    print(f"Вместимость: {capacity}")
    print(f"Дробный рюкзак (жадный): {frac_value:.2f}")
    print(f"Дискретный 0-1 (жадный): {greedy_01_value}")
    print(f"Дискретный 0-1 (точный): {exact_01_value}")

    if greedy_01_value < exact_01_value:
        print("Жадный для 0-1 не оптимален!")
    else:
        print("Жадный оптимален")

    print("\nПроизводительность алгоритмов")

    sizes = [5, 10, 15]

    for size in sizes:
        print(f"\nРазмер: {size} предметов")

        random.seed(42)
        items = [
            (random.randint(1, 50), random.randint(1, 100))
            for _ in range(size)
        ]
        capacity = sum(w for w, _ in items) // 2

        start = time.perf_counter()
        frac_value, _ = fractional_knapsack(items, capacity)
        frac_time = (time.perf_counter() - start) * 1000

        if size <= 15:
            start = time.perf_counter()
            exact_value = brute_force_knapsack_01(items, capacity)
            exact_time = (time.perf_counter() - start) * 1000

            print(f"  Дробный: {frac_value:.2f} ({frac_time:.2f} мс)")
            print(f"  Точный 0-1: {exact_value} ({exact_time:.2f} мс)")
        else:
            print(f"  Дробный: {frac_value:.2f} ({frac_time:.2f} мс)")


def test_interval_scheduling():
    """Тестирование алгоритма выбора заявок."""
    print("\nТест: выбор заявок")

    intervals = [(1, 3), (2, 5), (4, 6), (6, 8), (5, 7), (7, 9)]
    selected = interval_scheduling(intervals)

    print(f"Интервалы: {intervals}")
    print(f"Выбрано: {len(selected)}")
    print(f"Выбранные: {selected}")


def test_huffman_performance():
    """Тестирование производительности алгоритма Хаффмана."""
    print("\nПроизводительность: Хаффман")

    sizes = [100, 1000, 10000, 50000]

    print("\nРазмер | Время (мс) | Уникальных символов")

    for size in sizes:
        random.seed(42)
        text = ''.join(random.choices('abcdefghij', k=size))

        start = time.perf_counter()
        codes, _ = huffman_coding(text)
        elapsed = (time.perf_counter() - start) * 1000

        print(f"{size:6d} | {elapsed:10.3f} | {len(codes):18d}")


def test_coin_change():
    """Тестирование задачи о сдаче."""
    print("\nТест: минимальное количество монет")

    standard_coins = [1, 5, 10, 25, 50]
    amounts = [37, 68, 99, 123]

    print(f"Система: {standard_coins}")
    for amount in amounts:
        try:
            total, coins = min_coins_greedy(amount, standard_coins)
            print(f"  {amount}: {total} монет - {coins}")
        except ValueError as e:
            print(f"  {amount}: {e}")

    print("\nПример неоптимальности для системы [1, 3, 4]:")
    print("Сумма 6:")
    print("  Жадный: 3 монеты (4+1+1)")
    print("  Оптимально: 2 монеты (3+3)")


def test_mst():
    """Тестирование алгоритма Краскала."""
    print("\nТест: минимальное остовное дерево")

    vertices = 4
    edges = [
        (0, 1, 2),
        (0, 2, 3),
        (1, 2, 1),
        (1, 3, 4),
        (2, 3, 5)
    ]

    mst = kruskal_mst(vertices, edges)
    total_weight = sum(w for _, _, w in mst)

    print(f"Граф: {vertices} вершин, {len(edges)} ребер")
    print(f"MST (вес {total_weight}):")
    for u, v, w in mst:
        print(f"  {u} -- {v} ({w})")


def main():
    """Основная функция для запуска всех тестов."""
    print("Лабораторная работа №8: Анализ жадных алгоритмов")

    compare_knapsack_algorithms()
    test_interval_scheduling()
    test_huffman_performance()
    test_coin_change()
    test_mst()

    print("\nТесты завершены")


if __name__ == "__main__":
    main()
