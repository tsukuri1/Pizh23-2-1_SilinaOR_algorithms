#!/usr/bin/env python3
"""
Модуль для визуализации результатов.
"""

import time
import matplotlib.pyplot as plt
from recursion import fibonacci
from memoization import fibonacci_memoized


def plot_fibonacci_performance(max_n: int = 30):
    """
    Построение графика времени выполнения для Фибоначчи.

    Args:
        max_n (int): Максимальное значение n
    """
    naive_times = []
    memoized_times = []
    n_values = list(range(1, max_n + 1))

    print("Измерение времени выполнения...")
    for n in n_values:
        # Наивная рекурсия
        start = time.time()
        fibonacci(n)
        naive_times.append(time.time() - start)

        # Мемоизация
        start = time.time()
        fibonacci_memoized(n)
        memoized_times.append(time.time() - start)

        if n % 5 == 0:
            naive_str = f"{naive_times[-1]:.6f}s"
            memo_str = f"{memoized_times[-1]:.6f}s"
            print(f"n={n}: наивное={naive_str}, мемоизация={memo_str}")

    # Построение графиков
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(n_values, naive_times, 'r-', label='Наивная рекурсия',
             linewidth=2)
    plt.plot(n_values, memoized_times, 'b-', label='С мемоизацией',
             linewidth=2)
    plt.xlabel('n')
    plt.ylabel('Время (секунды)')
    plt.title('Время вычисления n-го числа Фибоначчи')
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.subplot(1, 2, 2)
    plt.semilogy(n_values, naive_times, 'r-', label='Наивная рекурсия',
                 linewidth=2)
    plt.semilogy(n_values, memoized_times, 'b-', label='С мемоизацией',
                 linewidth=2)
    plt.xlabel('n')
    plt.ylabel('Время (логарифмическая шкала)')
    plt.title('Логарифмическая шкала времени выполнения')
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('fibonacci_performance.png', dpi=150, bbox_inches='tight')
    plt.show()

    # Анализ роста
    print("\nАнализ роста времени выполнения:")
    print("-" * 50)
    for i in range(5, max_n + 1, 5):
        if (i > 5 and naive_times[i-1] > 0 and naive_times[i-6] > 0
                and memoized_times[i-1] > 0 and memoized_times[i-6] > 0):
            growth_naive = naive_times[i-1] / naive_times[i-6]
            growth_memo = memoized_times[i-1] / memoized_times[i-6]
            print(f"n={i:2d}: Наивный рост={growth_naive:6.2f}x, "
                  f"Мемоизация рост={growth_memo:6.2f}x")


def plot_complexity_comparison():
    """
    Построение графика сравнения сложностей.
    """
    n_values = list(range(1, 21))

    # Теоретические сложности
    # O(2^n) - наивный Фибоначчи
    theoretical_naive = [2 ** n for n in n_values]

    # O(n) - Фибоначчи с мемоизацией
    theoretical_memo = n_values

    # Нормализуем для сравнения
    max_naive = max(theoretical_naive)
    normalized_naive = [x / max_naive for x in theoretical_naive]

    max_memo = max(theoretical_memo)
    normalized_memo = [x / max_memo for x in theoretical_memo]

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, normalized_naive, 'r--', label='O(2ⁿ) - теоретическая',
             linewidth=2)
    plt.plot(n_values, normalized_memo, 'b--', label='O(n) - теоретическая',
             linewidth=2)

    # Добавляем реальные данные
    naive_times = []
    memoized_times = []
    for n in n_values:
        start = time.time()
        fibonacci(n)
        naive_times.append(time.time() - start)

        start = time.time()
        fibonacci_memoized(n)
        memoized_times.append(time.time() - start)

    # Нормализуем реальные данные
    max_naive_real = max(naive_times) if max(naive_times) > 0 else 1
    normalized_naive_real = [t / max_naive_real for t in naive_times]

    max_memo_real = max(memoized_times) if max(memoized_times) > 0 else 1
    normalized_memo_real = [t / max_memo_real for t in memoized_times]

    plt.plot(n_values, normalized_naive_real, 'ro-',
             label='Наивная (реальная)', linewidth=2)
    plt.plot(n_values, normalized_memo_real, 'bo-',
             label='Мемоизация (реальная)', linewidth=2)

    plt.xlabel('n')
    plt.ylabel('Нормализованное время/сложность')
    plt.title('Сравнение теоретической и реальной сложности')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('complexity_comparison.png', dpi=150, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    print("Визуализация производительности рекурсивных алгоритмов")
    print("=" * 60)

    plot_fibonacci_performance(25)
    plot_complexity_comparison()
