"""
Хеш-таблица с методом цепочек.
"""

from hash_functions import polynomial_hash


class HashTableChaining:
    """Хеш-таблица с разрешением коллизий методом цепочек."""

    def __init__(self, initial_capacity=16, load_factor_threshold=0.75,
                 hash_func=None):
        self.capacity = initial_capacity
        self.size = 0
        self.load_factor_threshold = load_factor_threshold
        self.hash_func = hash_func or polynomial_hash
        self.table = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        return self.hash_func(key, self.capacity)

    def _resize(self, new_capacity):
        old_table = self.table
        self.capacity = new_capacity
        self.table = [[] for _ in range(self.capacity)]
        self.size = 0
        for chain in old_table:
            for key, value in chain:
                self.insert(key, value)

    def insert(self, key, value):
        if self.size / self.capacity >= self.load_factor_threshold:
            self._resize(self.capacity * 2)
        index = self._hash(key)
        chain = self.table[index]
        for i, (k, v) in enumerate(chain):
            if k == key:
                chain[i] = (key, value)
                return True
        chain.append((key, value))
        self.size += 1
        return True

    def get(self, key, default=None):
        index = self._hash(key)
        chain = self.table[index]
        for k, v in chain:
            if k == key:
                return v
        return default

    def remove(self, key):
        index = self._hash(key)
        chain = self.table[index]
        for i, (k, v) in enumerate(chain):
            if k == key:
                del chain[i]
                self.size -= 1
                return True
        return False

    def contains(self, key):
        return self.get(key) is not None

    def load_factor(self):
        return self.size / self.capacity if self.capacity > 0 else 0

    def __len__(self):
        return self.size

    def __getitem__(self, key):
        result = self.get(key)
        if result is None:
            raise KeyError(f"Key '{key}' not found")
        return result

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __delitem__(self, key):
        if not self.remove(key):
            raise KeyError(f"Key '{key}' not found")

    def __contains__(self, key):
        return self.contains(key)

    def keys(self):
        for chain in self.table:
            for key, _ in chain:
                yield key

    def values(self):
        for chain in self.table:
            for _, value in chain:
                yield value

    def items(self):
        for chain in self.table:
            for key, value in chain:
                yield key, value

    def get_statistics(self):
        chain_lengths = [len(chain) for chain in self.table]
        max_chain = max(chain_lengths) if chain_lengths else 0
        avg_chain = (sum(chain_lengths) / len(chain_lengths)
                     if chain_lengths else 0)
        return {
            'size': self.size,
            'capacity': self.capacity,
            'load_factor': self.load_factor(),
            'max_chain_length': max_chain,
            'avg_chain_length': avg_chain,
            'empty_buckets': sum(1 for length in chain_lengths if length == 0)
        }


if __name__ == "__main__":
    ht = HashTableChaining(initial_capacity=8, load_factor_threshold=0.5)
    ht["apple"] = 1
    ht["banana"] = 2
    ht["cherry"] = 3
    ht["date"] = 4
    ht["elderberry"] = 5
    print(f"Размер: {len(ht)}")
    print(f"Коэффициент: {ht.load_factor():.2f}")
    print(f"ht['apple'] = {ht['apple']}")
    print(f"'banana' in ht: {'banana' in ht}")
    del ht["banana"]
    print(f"После удаления: {len(ht)}")
    print(f"'banana' in ht: {'banana' in ht}")
    stats = ht.get_statistics()
    for key, value in stats.items():
        print(f"  {key}: {value}")
