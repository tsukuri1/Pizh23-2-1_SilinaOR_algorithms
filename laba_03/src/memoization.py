#!/usr/bin/env python3
"""
Модуль с мемоизированными версиями рекурсивных алгоритмов.
"""

import time
from typing import Dict, Callable, Any
from functools import wraps

# Импортируем функцию fibonacci из recursion.py
try:
    from recursion import fibonacci
except ImportError:
    # Если не удалось импортировать, определим здесь
    def fibonacci(n: int) -> int:
        """Наивная реализация Фибоначчи."""
        if n < 0:
            raise ValueError(
                "Номер числа Фибоначчи должен быть неотрицательным"
            )
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)


def memoize(func: Callable) -> Callable:
    """
    Декоратор для мемоизации функции.

    Args:
        func (Callable): Функция для мемоизации

    Returns:
        Callable: Мемоизированная функция
    """
    cache: Dict[Any, Any] = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


@memoize
def fibonacci_memoized(n: int) -> int:
    """
    Вычисление n-го числа Фибоначчи с мемоизацией.

    Временная сложность: O(n)
    Глубина рекурсии: O(n)

    Args:
        n (int): Номер числа Фибоначчи

    Returns:
        int: n-е число Фибоначчи
    """
    if n <= 1:
        return n
    return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)


class FibonacciCounter:
    """Класс для подсчета вызовов рекурсивной функции."""

    def __init__(self):
        self.count = 0
        self.cache = {}

    def fibonacci_with_counter(self, n: int) -> int:
        """
        Версия Фибоначчи со счетчиком вызовов.

        Args:
            n (int): Номер числа Фибоначчи

        Returns:
            int: n-е число Фибоначчи
        """
        self.count += 1
        if n <= 1:
            return n
        return (self.fibonacci_with_counter(n - 1) +
                self.fibonacci_with_counter(n - 2))

    def fibonacci_memoized_with_counter(self, n: int) -> int:
        """
        Мемоизированная версия Фибоначчи со счетчиком вызовов.

        Args:
            n (int): Номер числа Фибоначчи

        Returns:
            int: n-е число Фибоначчи
        """
        self.count += 1
        if n <= 1:
            return n

        if n not in self.cache:
            self.cache[n] = (
                self.fibonacci_memoized_with_counter(n - 1) +
                self.fibonacci_memoized_with_counter(n - 2)
            )

        return self.cache[n]


def compare_performance(n: int = 35):
    """
    Сравнение производительности наивной и мемоизированной версий.

    Args:
        n (int): Номер числа Фибоначчи для вычисления
    """
    print(f"\nСравнение производительности для n={n}")
    print("=" * 50)

    # Создаем экземпляры для подсчета вызовов
    naive_counter = FibonacciCounter()
    memoized_counter = FibonacciCounter()

    # Наивная рекурсия
    start_time = time.time()
    result_naive = naive_counter.fibonacci_with_counter(n)
    naive_time = time.time() - start_time

    # Мемоизированная версия
    start_time = time.time()
    result_memoized = memoized_counter.fibonacci_memoized_with_counter(n)
    memoized_time = time.time() - start_time

    # Декораторная мемоизация
    start_time = time.time()
    result_decorator = fibonacci_memoized(n)
    decorator_time = time.time() - start_time

    # Используем переменные, чтобы избежать предупреждения
    _ = result_memoized  # Используем в выводе
    _ = result_decorator  # Используем в выводе

    print(f"Результат (должен быть одинаковым): {result_naive}")
    print("\nНаивная рекурсия:")
    print(f"  Время: {naive_time:.6f} секунд")
    print(f"  Количество вызовов: {naive_counter.count}")

    print("\nМемоизация (ручная):")
    print(f"  Время: {memoized_time:.6f} секунд")
    print(f"  Количество вызовов: {memoized_counter.count}")

    print("\nМемоизация (декоратор):")
    print(f"  Время: {decorator_time:.6f} секунд")

    if memoized_time > 0:
        speedup = naive_time / memoized_time
        print(f"\nУскорение: {speedup:.2f} раз")
    else:
        print("\nУскорение: невозможно вычислить (нулевое время)")


def performance_experiment(max_n: int = 40):
    """
    Экспериментальное исследование производительности.

    Args:
        max_n (int): Максимальное значение n для тестирования
    """
    print("\nЭкспериментальное исследование производительности")
    print("=" * 50)
    header = f"{'n':>5} {'Наивное (с)':>15} {'Мемоизация (с)':>15}"
    header += f" {'Ускорение':>12}"
    print(header)

    results = []

    for n in range(5, max_n + 1, 5):
        # Наивная рекурсия
        start_time = time.time()
        fibonacci(n)  # Из модуля recursion или локальной функции
        naive_time = time.time() - start_time

        # Мемоизация
        start_time = time.time()
        fibonacci_memoized(n)
        memoized_time = time.time() - start_time

        if naive_time > 0 and memoized_time > 0:
            speedup = naive_time / memoized_time
        else:
            speedup = float('inf')

        results.append((n, naive_time, memoized_time, speedup))
        row = f"{n:>5} {naive_time:>15.6f} {memoized_time:>15.6f}"
        row += f" {speedup:>12.2f}"
        print(row)

    return results


if __name__ == "__main__":
    # Сравнение производительности
    compare_performance(35)

    # Эксперимент с разными значениями n
    results = performance_experiment(40)
