"""Сравнение подходов ДП."""

import time
from dynamic_programming import fib_naive, fib_memo, fib_bottom_up, knapsack


def compare_fibonacci():
    """Сравнение времени для Фибоначчи."""
    test_cases = [10, 20, 30, 35, 40]

    print("n\tНаивная\tМемоизация\tТабличный")
    print("-" * 40)

    for n in test_cases:
        times = []

        if n <= 35:
            start = time.time()
            fib_naive(n)
            times.append(time.time() - start)
        else:
            times.append(float('inf'))

        start = time.time()
        fib_memo(n)
        times.append(time.time() - start)

        start = time.time()
        fib_bottom_up(n)
        times.append(time.time() - start)

        print(f"{n}\t{times[0]:.6f}\t{times[1]:.6f}\t\t{times[2]:.6f}")


def compare_knapsack():
    """Сравнение жадного и ДП для рюкзака."""
    def greedy_fractional(weights, values, capacity):
        items = [(v / w, v, w) for v, w in zip(values, weights)]
        items.sort(reverse=True)
        total_value = 0
        for ratio, v, w in items:
            if capacity >= w:
                total_value += v
                capacity -= w
            else:
                total_value += ratio * capacity
                break
        return total_value

    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5

    dp_value, _ = knapsack(weights, values, capacity)
    greedy_value = greedy_fractional(weights, values, capacity)

    print("\nЗадача о рюкзаке:")
    print(f"Веса: {weights}")
    print(f"Стоимости: {values}")
    print(f"Вместимость: {capacity}")
    print(f"ДП (0-1): {dp_value}")
    print(f"Жадный (непрерывный): {greedy_value:.2f}")


if __name__ == "__main__":
    print("Сравнение подходов ДП")
    compare_fibonacci()
    compare_knapsack()
