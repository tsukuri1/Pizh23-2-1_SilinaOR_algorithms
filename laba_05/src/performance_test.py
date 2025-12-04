"""
Тестирование производительности хеш-таблиц.
"""

import time
import random
import string


def generate_random_string(length=10):
    """Генерация случайной строки."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


def generate_test_data(num_items=1000):
    """Генерация тестовых данных."""
    keys = [generate_random_string(8) for _ in range(num_items)]
    values = [random.randint(1, 1000) for _ in range(num_items)]
    return list(zip(keys, values))


def test_performance(table_class, test_data, **kwargs):
    """Тестирование производительности таблицы."""
    table = table_class(**kwargs)

    # Тестирование вставки
    start_time = time.perf_counter()
    for key, value in test_data:
        table.insert(key, value)
    insert_time = time.perf_counter() - start_time

    # Тестирование поиска
    sample_size = min(100, len(test_data))
    search_keys = random.sample([k for k, _ in test_data], sample_size)
    start_time = time.perf_counter()
    for key in search_keys:
        _ = table.get(key)
    search_time = time.perf_counter() - start_time

    # Тестирование удаления
    delete_keys = random.sample([k for k, _ in test_data], sample_size)
    start_time = time.perf_counter()
    for key in delete_keys:
        table.remove(key)
    delete_time = time.perf_counter() - start_time

    stats = table.get_statistics()
    return insert_time, search_time, delete_time, stats


def compare_hash_functions():
    """Сравнение хеш-функций."""
    from hash_functions import (
        simple_hash,
        polynomial_hash,
        djb2_hash,
        fnv_hash
    )

    hash_funcs = [
        ('простая', simple_hash),
        ('полиномиальная', polynomial_hash),
        ('djb2', djb2_hash),
        ('fnv-1a', fnv_hash)
    ]
    test_data = generate_test_data(1000)
    table_size = 100

    print("Сравнение хеш-функций:")
    print("-" * 40)

    for name, func in hash_funcs:
        distribution = [0] * table_size
        for key, _ in test_data:
            hash_val = func(key, table_size)
            distribution[hash_val] += 1

        collisions = sum(count - 1 for count in distribution if count > 1)
        max_chain = max(distribution)
        avg_chain = sum(distribution) / len(distribution)

        print(f"\n{name}:")
        print(f"  коллизии: {collisions}")
        print(f"  максимальная цепочка: {max_chain}")
        print(f"  средняя цепочка: {avg_chain:.2f}")


def test_load_factor_impact():
    """Тестирование влияния коэффициента заполнения."""
    from hash_table_chaining import HashTableChaining
    from hash_table_open_addressing import HashTableOpenAddressing

    load_factors = [0.1, 0.25, 0.5, 0.75, 0.9]
    num_items = 1000

    print("\nВлияние коэффициента заполнения:")
    print("-" * 40)

    for load_factor in load_factors:
        test_data = generate_test_data(num_items)
        print(f"\nКоэффициент: {load_factor}")

        # Метод цепочек
        ht_chaining = HashTableChaining(load_factor_threshold=load_factor)
        for key, value in test_data:
            ht_chaining.insert(key, value)
        stats = ht_chaining.get_statistics()
        avg_chain = stats['avg_chain_length']
        print(f"  метод цепочек - ср. длина: {avg_chain:.2f}")

        # Линейное пробирование
        ht_linear = HashTableOpenAddressing(
            load_factor_threshold=load_factor,
            probing_method='linear'
        )
        for key, value in test_data:
            ht_linear.insert(key, value)
        stats = ht_linear.get_statistics()
        avg_probe = stats['avg_probe_length']
        print(f"  линейное - ср. пробирование: {avg_probe:.2f}")

        # Двойное хеширование
        ht_double = HashTableOpenAddressing(
            load_factor_threshold=load_factor,
            probing_method='double'
        )
        for key, value in test_data:
            ht_double.insert(key, value)
        stats = ht_double.get_statistics()
        avg_probe = stats['avg_probe_length']
        print(f"  двойное - ср. пробирование: {avg_probe:.2f}")


def compare_implementations():
    """Сравнение разных реализаций хеш-таблиц."""
    from hash_table_chaining import HashTableChaining
    from hash_table_open_addressing import HashTableOpenAddressing

    test_sizes = [100, 500, 1000, 5000]

    print("\nСравнение реализаций:")
    print("-" * 40)

    for size in test_sizes:
        test_data = generate_test_data(size)
        print(f"\nЭлементов: {size}")

        # Метод цепочек
        insert_time, search_time, delete_time, stats = test_performance(
            HashTableChaining, test_data, initial_capacity=16
        )
        print("  цепочки:")
        print(f"    вставка: {insert_time:.6f} с")
        print(f"    поиск: {search_time:.6f} с")
        print(f"    удаление: {delete_time:.6f} с")
        print(f"    ср. длина цепи: {stats['avg_chain_length']:.2f}")

        # Линейное пробирование
        insert_time, search_time, delete_time, stats = test_performance(
            HashTableOpenAddressing, test_data,
            initial_capacity=16, probing_method='linear'
        )
        print("  линейное пробирование:")
        print(f"    вставка: {insert_time:.6f} с")
        print(f"    поиск: {search_time:.6f} с")
        print(f"    удаление: {delete_time:.6f} с")
        print(f"    ср. пробирование: {stats['avg_probe_length']:.2f}")

        # Двойное хеширование
        insert_time, search_time, delete_time, stats = test_performance(
            HashTableOpenAddressing, test_data,
            initial_capacity=16, probing_method='double'
        )
        print("  двойное хеширование:")
        print(f"    вставка: {insert_time:.6f} с")
        print(f"    поиск: {search_time:.6f} с")
        print(f"    удаление: {delete_time:.6f} с")
        print(f"    ср. пробирование: {stats['avg_probe_length']:.2f}")


def run_comprehensive_test():
    """Запуск комплексного тестирования."""
    print("Тестирование производительности хеш-таблиц")
    print("-" * 40)

    compare_hash_functions()
    test_load_factor_impact()
    compare_implementations()


if __name__ == "__main__":
    run_comprehensive_test()
