"""
Визуализация результатов тестирования хеш-таблиц.
"""

import matplotlib.pyplot as plt
import random
import string
from hash_functions import simple_hash, polynomial_hash, djb2_hash, fnv_hash
from hash_table_chaining import HashTableChaining
from hash_table_open_addressing import HashTableOpenAddressing


def generate_test_data(num_items=1000):
    keys = []
    for _ in range(num_items):
        key = ''.join(random.choice(string.ascii_letters + string.digits)
                      for _ in range(8))
        keys.append(key)
    values = [random.randint(1, 1000) for _ in range(num_items)]
    return list(zip(keys, values))


def plot_collision_distribution():
    hash_funcs = [('simple', simple_hash), ('polynomial', polynomial_hash),
                  ('djb2', djb2_hash), ('fnv', fnv_hash)]
    test_data = generate_test_data(1000)
    table_size = 100
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()
    for idx, (name, func) in enumerate(hash_funcs):
        ax = axes[idx]
        distribution = [0] * table_size
        for key, _ in test_data:
            hash_val = func(key, table_size)
            distribution[hash_val] += 1
        ax.bar(range(table_size), distribution, alpha=0.7)
        ax.set_title(f'{name} hash')
        ax.set_xlabel('Bucket index')
        ax.set_ylabel('Number of items')
        ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('hash_distribution.png', dpi=300)
    plt.show()
    print("Гистограмма сохранена в 'hash_distribution.png'")


def plot_load_factor_impact():
    load_factors = [0.1, 0.25, 0.5, 0.75, 0.9]
    num_items = 1000
    test_data = generate_test_data(num_items)
    chaining_avg = []
    linear_avg = []
    double_avg = []
    for load_factor in load_factors:
        ht = HashTableChaining(load_factor_threshold=load_factor)
        for key, value in test_data:
            ht.insert(key, value)
        stats = ht.get_statistics()
        chaining_avg.append(stats['avg_chain_length'])
        ht = HashTableOpenAddressing(load_factor_threshold=load_factor,
                                     probing_method='linear')
        for key, value in test_data:
            ht.insert(key, value)
        stats = ht.get_statistics()
        linear_avg.append(stats['avg_probe_length'])
        ht = HashTableOpenAddressing(load_factor_threshold=load_factor,
                                     probing_method='double')
        for key, value in test_data:
            ht.insert(key, value)
        stats = ht.get_statistics()
        double_avg.append(stats['avg_probe_length'])
    plt.figure(figsize=(10, 6))
    plt.plot(load_factors, chaining_avg, 'o-', label='Chaining', linewidth=2)
    plt.plot(load_factors, linear_avg, 's-',
             label='Linear probing', linewidth=2)
    plt.plot(load_factors, double_avg, '^-',
             label='Double hashing', linewidth=2)
    plt.xlabel('Load factor')
    plt.ylabel('Average chain/probe length')
    plt.title('Impact of load factor on performance')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('load_factor_impact.png', dpi=300)
    plt.show()
    print("График сохранен в 'load_factor_impact.png'")


def plot_performance_comparison():
    test_sizes = [100, 500, 1000, 5000]
    insert_times = {'Chaining': [], 'Linear': [], 'Double': []}
    search_times = {'Chaining': [], 'Linear': [], 'Double': []}
    for size in test_sizes:
        test_data = generate_test_data(size)
        import time
        start = time.perf_counter()
        ht = HashTableChaining()
        for key, value in test_data:
            ht.insert(key, value)
        insert_times['Chaining'].append(time.perf_counter() - start)
        start = time.perf_counter()
        for key, _ in test_data[:100]:
            _ = ht.get(key)
        search_times['Chaining'].append(time.perf_counter() - start)
        start = time.perf_counter()
        ht = HashTableOpenAddressing(probing_method='linear')
        for key, value in test_data:
            ht.insert(key, value)
        insert_times['Linear'].append(time.perf_counter() - start)
        start = time.perf_counter()
        for key, _ in test_data[:100]:
            _ = ht.get(key)
        search_times['Linear'].append(time.perf_counter() - start)
        start = time.perf_counter()
        ht = HashTableOpenAddressing(probing_method='double')
        for key, value in test_data:
            ht.insert(key, value)
        insert_times['Double'].append(time.perf_counter() - start)
        start = time.perf_counter()
        for key, _ in test_data[:100]:
            _ = ht.get(key)
        search_times['Double'].append(time.perf_counter() - start)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    for name in insert_times:
        ax1.plot(test_sizes, insert_times[name], 'o-', label=name, linewidth=2)
        ax2.plot(test_sizes, search_times[name], 'o-', label=name, linewidth=2)
    ax1.set_xlabel('Number of items')
    ax1.set_ylabel('Insert time (seconds)')
    ax1.set_title('Insert performance')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_xscale('log')
    ax2.set_xlabel('Number of items')
    ax2.set_ylabel('Search time (seconds)')
    ax2.set_title('Search performance')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_xscale('log')
    plt.tight_layout()
    plt.savefig('performance_comparison.png', dpi=300)
    plt.show()
    print("График сохранен в 'performance_comparison.png'")


if __name__ == "__main__":
    plt.style.use('default')
    plot_collision_distribution()
    plot_load_factor_impact()
    plot_performance_comparison()
    print("\nВсе графики созданы!")
