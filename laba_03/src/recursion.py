#!/usr/bin/env python3
"""
Модуль с классическими рекурсивными алгоритмами.
"""


def factorial(n: int) -> int:
    """
    Вычисление факториала числа n рекурсивным способом.

    Временная сложность: O(n)
    Глубина рекурсии: O(n)

    Args:
        n (int): Неотрицательное целое число

    Returns:
        int: Факториал числа n

    Raises:
        ValueError: Если n < 0
    """
    if n < 0:
        raise ValueError(
            "Факториал определен только для неотрицательных чисел"
        )
    if n == 0:
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    """
    Вычисление n-го числа Фибоначчи наивным рекурсивным способом.

    Временная сложность: O(2^n)
    Глубина рекурсии: O(n)

    Args:
        n (int): Номер числа Фибоначчи

    Returns:
        int: n-е число Фибоначчи

    Raises:
        ValueError: Если n < 0
    """
    if n < 0:
        raise ValueError(
            "Номер числа Фибоначчи должен быть неотрицательным"
        )
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fast_power(a: float, n: int) -> float:
    """
    Быстрое возведение числа a в степень n через степень двойки.

    Временная сложность: O(log n)
    Глубина рекурсии: O(log n)

    Args:
        a (float): Основание
        n (int): Показатель степени

    Returns:
        float: a в степени n

    Raises:
        ValueError: Если n < 0 (для простоты реализации)
    """
    if n < 0:
        # Для отрицательных степеней можно добавить обработку,
        # но в рамках задания ограничимся неотрицательными
        raise ValueError("Показатель степени должен быть неотрицательным")

    if n == 0:
        return 1
    if n == 1:
        return a

    # Рекурсивно вычисляем a^(n//2)
    half_power = fast_power(a, n // 2)

    # Если n четное
    if n % 2 == 0:
        return half_power * half_power
    # Если n нечетное
    return half_power * half_power * a


if __name__ == "__main__":
    # Примеры использования
    print("Факториал 5:", factorial(5))
    print("10-е число Фибоначчи:", fibonacci(10))
    print("2^10 (быстрое возведение):", fast_power(2, 10))
