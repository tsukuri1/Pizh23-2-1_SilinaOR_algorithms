"""
Визуализация дерева кодов Хаффмана.
"""

import matplotlib.pyplot as plt
import numpy as np
import time
import random
from greedy_algorithms import huffman_coding


def visualize_huffman_simple(text: str):
    """
    Простая визуализация дерева Хаффмана.

    Args:
        text: Входной текст для кодирования
    """
    codes, _ = huffman_coding(text)

    print(f"Текст: '{text[:50]}{'...' if len(text) > 50 else ''}'")
    print(f"Длина: {len(text)} символов")
    print(f"Уникальных символов: {len(codes)}")
    print("Коды Хаффмана:")

    for char, code in sorted(codes.items()):
        if char.isprintable() and char != ' ':
            print(f"  '{char}': {code}")
        else:
            print(f"  (непечатный): {code}")


def plot_huffman_performance():
    """
    Строит график производительности алгоритма Хаффмана.
    """
    sizes = [100, 500, 1000, 5000, 10000, 50000]
    times = []

    print("Измерение производительности...")

    for size in sizes:
        random.seed(42)
        text = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=size))

        start = time.perf_counter()
        huffman_coding(text)
        elapsed = (time.perf_counter() - start) * 1000

        times.append(elapsed)
        print(f"  n={size}: {elapsed:.2f} мс")

    plt.figure(figsize=(8, 5))
    plt.plot(sizes, times, 'bo-', linewidth=2, markersize=6)
    plt.xlabel('Размер входных данных')
    plt.ylabel('Время (мс)')
    plt.title('Производительность алгоритма Хаффмана')
    plt.grid(True, alpha=0.3)

    x_fit = np.linspace(min(sizes), max(sizes), 100)
    y_fit = times[0] * (x_fit / sizes[0]) * np.log(x_fit) / np.log(sizes[0])
    plt.plot(x_fit, y_fit, 'r--', label='O(n log n)', alpha=0.7)

    plt.legend()
    plt.tight_layout()
    plt.savefig('huffman_performance.png', dpi=120)
    print("График сохранен в huffman_performance.png")

    print("\nОтношение времени при увеличении размера:")
    for i in range(1, len(sizes)):
        ratio = sizes[i] / sizes[i-1]
        time_ratio = times[i] / times[i-1]
        print(f"  ×{ratio:.1f} по размеру -> ×{time_ratio:.2f} по времени")


def main():
    """Основная функция для визуализации."""
    print("Визуализация алгоритма Хаффмана")

    text1 = "abracadabra"
    visualize_huffman_simple(text1)

    text2 = "hello world this is huffman coding example"
    visualize_huffman_simple(text2)

    plot_huffman_performance()


if __name__ == "__main__":
    main()
