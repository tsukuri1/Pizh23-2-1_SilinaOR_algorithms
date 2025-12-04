"""Анализ производительности операций с кучей."""
import random
import time
import matplotlib.pyplot as plt
from heap import MinHeap
from heapsort import heapsort_inplace


def test_insert_performance():
    """Тестирование производительности вставки."""
    print("Тестирование производительности вставки")
    print()

    sizes = [100, 1000, 5000, 10000, 50000]
    print(f"{'Размер':<10} {'Время (сек)':<15}")

    for size in sizes:
        heap = MinHeap()
        data = [random.randint(0, 100000) for _ in range(size)]

        start = time.time()
        for item in data:
            heap.insert(item)
        elapsed = time.time() - start

        print(f"{size:<10} {elapsed:<15.6f}")


def test_build_heap_performance():
    """Сравнение двух методов построения кучи."""
    print()
    print("Сравнение методов построения кучи")
    print()
    header = f"{'Размер':<10} {'Посл. вставка':<15} "
    header += f"{'Build_heap':<15} {'Отношение':<10}"
    print(header)

    sizes = [100, 1000, 5000, 10000]

    for size in sizes:
        data = [random.randint(0, 100000) for _ in range(size)]

        # Метод 1: Последовательная вставка
        heap1 = MinHeap()
        start = time.time()
        for item in data:
            heap1.insert(item)
        time_insert = time.time() - start

        # Метод 2: Build_heap
        heap2 = MinHeap()
        start = time.time()
        heap2.build_heap(data)
        time_build = time.time() - start

        ratio = time_insert / time_build if time_build > 0 else 0

        msg = f"{size:<10} {time_insert:<15.6f} "
        msg += f"{time_build:<15.6f} {ratio:<10.2f}"
        print(msg)


def test_heapsort_performance():
    """Тестирование производительности Heapsort."""
    print()
    print("Тестирование производительности Heapsort")
    print()
    print(f"{'Размер':<10} {'Heapsort':<15}")

    sizes = [100, 1000, 5000, 10000, 50000]

    for size in sizes:
        data = [random.randint(0, 100000) for _ in range(size)]

        start = time.time()
        heapsort_inplace(data.copy())
        elapsed = time.time() - start

        print(f"{size:<10} {elapsed:<15.6f}")


def plot_performance():
    """Построение графиков производительности."""
    print()
    print("Построение графиков производительности")
    print()

    sizes = [100, 500, 1000, 2000, 5000, 10000]
    insert_times = []
    build_times = []
    heapsort_times = []

    for size in sizes:
        data = [random.randint(0, 100000) for _ in range(size)]

        # Время последовательной вставки
        heap = MinHeap()
        start = time.time()
        for item in data:
            heap.insert(item)
        insert_times.append(time.time() - start)

        # Время build_heap
        heap = MinHeap()
        start = time.time()
        heap.build_heap(data)
        build_times.append(time.time() - start)

        # Время Heapsort
        start = time.time()
        heapsort_inplace(data.copy())
        heapsort_times.append(time.time() - start)

    # Построение графиков
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.plot(sizes, insert_times, 'b-', label='Посл. вставка', linewidth=2)
    plt.xlabel('Размер')
    plt.ylabel('Время (сек)')
    plt.title('Последовательная вставка')
    plt.grid(True, alpha=0.3)

    plt.subplot(1, 3, 2)
    plt.plot(sizes, build_times, 'r-', label='Build_heap', linewidth=2)
    plt.xlabel('Размер')
    plt.ylabel('Время (сек)')
    plt.title('Build_heap')
    plt.grid(True, alpha=0.3)

    plt.subplot(1, 3, 3)
    plt.plot(sizes, heapsort_times, 'g-', label='Heapsort', linewidth=2)
    plt.xlabel('Размер')
    plt.ylabel('Время (сек)')
    plt.title('Heapsort')
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('heap_performance.png', dpi=150)
    plt.show()


def main():
    """Основная функция анализа."""
    print("Анализ производительности операций с кучей")
    print()

    test_insert_performance()
    test_build_heap_performance()
    test_heapsort_performance()
    plot_performance()


if __name__ == "__main__":
    main()
