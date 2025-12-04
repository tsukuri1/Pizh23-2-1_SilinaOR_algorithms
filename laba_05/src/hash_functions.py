"""
Реализация хеш-функций для строковых ключей.
"""


def simple_hash(key, table_size):
    """Простая хеш-функция: сумма кодов символов."""
    if not key:
        return 0
    return sum(ord(char) for char in key) % table_size


def polynomial_hash(key, table_size, base=31):
    """Полиномиальная хеш-функция."""
    if not key:
        return 0
    hash_value = 0
    for char in key:
        hash_value = (hash_value * base + ord(char)) % table_size
    return hash_value


def djb2_hash(key, table_size):
    """Хеш-функция DJB2."""
    if not key:
        return 0
    hash_value = 5381
    for char in key:
        hash_value = ((hash_value << 5) + hash_value) + ord(char)
    return hash_value % table_size


def fnv_hash(key, table_size):
    """Хеш-функция FNV-1a."""
    if not key:
        return 0
    FNV_OFFSET_BASIS = 2166136261
    FNV_PRIME = 16777619
    hash_value = FNV_OFFSET_BASIS
    for char in key:
        hash_value = hash_value ^ ord(char)
        hash_value = (hash_value * FNV_PRIME) % (2 ** 32)
    return hash_value % table_size


def test_hash_functions():
    """Тестирование хеш-функций."""
    test_keys = ["hello", "world", "test", "hash", "table"]
    table_size = 100
    print("Тестирование хеш-функций:")
    print("-" * 40)
    for key in test_keys:
        print(f"\nКлюч: '{key}'")
        print(f"  простая: {simple_hash(key, table_size)}")
        print(f"  полиномиальная: {polynomial_hash(key, table_size)}")
        print(f"  djb2: {djb2_hash(key, table_size)}")
        print(f"  fnv-1a: {fnv_hash(key, table_size)}")


if __name__ == "__main__":
    test_hash_functions()
