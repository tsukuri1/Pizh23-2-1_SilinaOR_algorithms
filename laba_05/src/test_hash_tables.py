"""
Unit-тесты для хеш-таблиц.
"""

import unittest
from hash_functions import simple_hash, polynomial_hash, djb2_hash, fnv_hash
from hash_table_chaining import HashTableChaining
from hash_table_open_addressing import HashTableOpenAddressing


class TestHashFunctions(unittest.TestCase):
    """Тесты хеш-функций."""

    def test_all_hash_functions(self):
        """Тест всех хеш-функций."""
        table_size = 100
        test_key = "test"
        funcs = [simple_hash, polynomial_hash, djb2_hash, fnv_hash]
        for func in funcs:
            hash1 = func(test_key, table_size)
            hash2 = func(test_key, table_size)
            self.assertEqual(hash1, hash2)
            self.assertGreaterEqual(hash1, 0)
            self.assertLess(hash1, table_size)


class TestHashTableChaining(unittest.TestCase):
    """Тесты хеш-таблицы с цепочками."""

    def test_basic_operations(self):
        """Тест основных операций."""
        ht = HashTableChaining()
        ht["key1"] = "value1"
        ht["key2"] = "value2"
        self.assertEqual(ht["key1"], "value1")
        self.assertEqual(ht["key2"], "value2")
        self.assertEqual(len(ht), 2)

    def test_update_and_contains(self):
        """Тест обновления и проверки наличия."""
        ht = HashTableChaining()
        ht["key1"] = "value1"
        ht["key1"] = "value2"
        self.assertEqual(ht["key1"], "value2")
        self.assertTrue("key1" in ht)
        self.assertFalse("key3" in ht)

    def test_delete(self):
        """Тест удаления."""
        ht = HashTableChaining()
        ht["key1"] = "value1"
        ht["key2"] = "value2"
        del ht["key1"]
        self.assertFalse("key1" in ht)
        self.assertTrue("key2" in ht)
        self.assertEqual(len(ht), 1)

    def test_collisions(self):
        """Тест коллизий."""
        ht = HashTableChaining(initial_capacity=2)
        ht["key1"] = "value1"
        ht["key2"] = "value2"
        ht["key3"] = "value3"
        self.assertEqual(len(ht), 3)
        self.assertEqual(ht["key1"], "value1")
        self.assertEqual(ht["key2"], "value2")
        self.assertEqual(ht["key3"], "value3")


class TestHashTableOpenAddressing(unittest.TestCase):
    """Тесты хеш-таблицы с открытой адресацией."""

    def test_linear_probing(self):
        """Тест линейного пробирования."""
        ht = HashTableOpenAddressing(probing_method='linear')
        ht["key1"] = "value1"
        ht["key2"] = "value2"
        ht["key3"] = "value3"
        self.assertEqual(ht["key1"], "value1")
        self.assertEqual(ht["key2"], "value2")
        self.assertEqual(ht["key3"], "value3")

    def test_double_hashing(self):
        """Тест двойного хеширования."""
        ht = HashTableOpenAddressing(probing_method='double')
        ht["key1"] = "value1"
        ht["key2"] = "value2"
        ht["key3"] = "value3"
        self.assertEqual(ht["key1"], "value1")
        self.assertEqual(ht["key2"], "value2")
        self.assertEqual(ht["key3"], "value3")

    def test_basic_operations(self):
        """Тест основных операций."""
        ht = HashTableOpenAddressing()
        ht["key1"] = "value1"
        ht["key2"] = "value2"
        self.assertEqual(ht["key1"], "value1")
        self.assertEqual(ht["key2"], "value2")
        self.assertEqual(len(ht), 2)

    def test_delete_and_reuse(self):
        """Тест удаления и повторного использования."""
        ht = HashTableOpenAddressing(initial_capacity=4)
        ht["key1"] = "value1"
        ht["key2"] = "value2"
        del ht["key1"]
        self.assertFalse("key1" in ht)
        ht["key3"] = "value3"
        self.assertTrue("key3" in ht)
        self.assertEqual(ht["key3"], "value3")


class TestComparison(unittest.TestCase):
    """Сравнительные тесты."""

    def test_all_implementations(self):
        """Тест всех реализаций на одинаковых данных."""
        test_data = [("apple", 1), ("banana", 2), ("cherry", 3),
                     ("date", 4), ("elderberry", 5)]
        implementations = [
            HashTableChaining(),
            HashTableOpenAddressing(probing_method='linear'),
            HashTableOpenAddressing(probing_method='double')
        ]
        for ht in implementations:
            for key, value in test_data:
                ht[key] = value
            for key, value in test_data:
                self.assertEqual(ht[key], value)
            self.assertEqual(len(ht), len(test_data))
            for key, _ in test_data:
                self.assertTrue(key in ht)
            for key, _ in test_data:
                del ht[key]
                self.assertFalse(key in ht)
            self.assertEqual(len(ht), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
