"""
Хеш-таблица с открытой адресацией.
"""

from hash_functions import polynomial_hash


class HashTableOpenAddressing:
    """Хеш-таблица с открытой адресацией."""

    def __init__(self, initial_capacity=16, load_factor_threshold=0.75,
                 hash_func=None, probing_method='linear'):
        self.capacity = initial_capacity
        self.size = 0
        self.load_factor_threshold = load_factor_threshold
        self.hash_func = hash_func or polynomial_hash
        self.probing_method = probing_method
        self.table = [None] * self.capacity
        self.deleted = [False] * self.capacity

    def _hash(self, key, i=0):
        if self.probing_method == 'linear':
            h = self.hash_func(key, self.capacity)
            return (h + i) % self.capacity
        elif self.probing_method == 'double':
            h1 = self.hash_func(key, self.capacity)
            h2 = 1 + (self.hash_func(key, self.capacity - 1) %
                      (self.capacity - 2))
            return (h1 + i * h2) % self.capacity
        else:
            raise ValueError(f"Неизвестный метод: {self.probing_method}")

    def _find_index(self, key):
        i = 0
        while i < self.capacity:
            index = self._hash(key, i)
            if self.table[index] is None and not self.deleted[index]:
                return None
            item = self.table[index]
            if (item is not None and item[0] == key and
                    not self.deleted[index]):
                return index
            i += 1
        return None

    def _resize(self, new_capacity):
        old_table = self.table
        old_deleted = self.deleted
        self.capacity = new_capacity
        self.table = [None] * self.capacity
        self.deleted = [False] * self.capacity
        self.size = 0
        for i in range(len(old_table)):
            if old_table[i] is not None and not old_deleted[i]:
                key, value = old_table[i]
                self.insert(key, value)

    def insert(self, key, value):
        if self.size / self.capacity >= self.load_factor_threshold:
            self._resize(self.capacity * 2)

        i = 0
        while i < self.capacity:
            index = self._hash(key, i)
            if self.table[index] is None or self.deleted[index]:
                self.table[index] = (key, value)
                self.deleted[index] = False
                self.size += 1
                return True
            item = self.table[index]
            if item[0] == key and not self.deleted[index]:
                self.table[index] = (key, value)
                return True
            i += 1

        # Если таблица заполнена - увеличиваем размер и пробуем снова
        self._resize(self.capacity * 2)
        return self.insert(key, value)

    def get(self, key, default=None):
        index = self._find_index(key)
        return self.table[index][1] if index is not None else default

    def remove(self, key):
        index = self._find_index(key)
        if index is not None:
            self.deleted[index] = True
            self.table[index] = None
            self.size -= 1
            return True
        return False

    def contains(self, key):
        return self._find_index(key) is not None

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
        for i in range(self.capacity):
            if self.table[i] is not None and not self.deleted[i]:
                yield self.table[i][0]

    def values(self):
        for i in range(self.capacity):
            if self.table[i] is not None and not self.deleted[i]:
                yield self.table[i][1]

    def items(self):
        for i in range(self.capacity):
            if self.table[i] is not None and not self.deleted[i]:
                yield self.table[i]

    def get_statistics(self):
        probe_lengths = []
        for i in range(self.capacity):
            if self.table[i] is not None and not self.deleted[i]:
                key = self.table[i][0]
                probe_len = 0
                while probe_len < self.capacity:
                    if self._hash(key, probe_len) == i:
                        break
                    probe_len += 1
                if probe_len > 0:
                    probe_lengths.append(probe_len)
        avg_probe = (sum(probe_lengths) / len(probe_lengths)
                     if probe_lengths else 0)
        max_probe = max(probe_lengths) if probe_lengths else 0
        return {
            'size': self.size,
            'capacity': self.capacity,
            'load_factor': self.load_factor(),
            'avg_probe_length': avg_probe,
            'max_probe_length': max_probe,
            'empty_slots': sum(1 for item in self.table if item is None)
        }


if __name__ == "__main__":
    print("Тестирование линейного пробирования:")
    ht_linear = HashTableOpenAddressing(initial_capacity=8,
                                        load_factor_threshold=0.5,
                                        probing_method='linear')
    ht_linear["apple"] = 1
    ht_linear["banana"] = 2
    ht_linear["cherry"] = 3
    ht_linear["date"] = 4
    print(f"Размер: {len(ht_linear)}")
    print(f"Коэффициент: {ht_linear.load_factor():.2f}")
    print(f"ht_linear['apple'] = {ht_linear['apple']}")
    print(f"'banana' in ht_linear: {'banana' in ht_linear}")
