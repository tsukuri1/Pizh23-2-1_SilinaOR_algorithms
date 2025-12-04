#!/usr/bin/env python3
"""
Модуль с практическими задачами на рекурсию.
"""

import os
from typing import List, Optional, Tuple


def binary_search_recursive(
    arr: List[int],
    target: int,
    left: int = 0,
    right: Optional[int] = None
) -> Optional[int]:
    """
    Рекурсивный бинарный поиск в отсортированном массиве.

    Временная сложность: O(log n)
    Глубина рекурсии: O(log n)

    Args:
        arr (List[int]): Отсортированный массив целых чисел
        target (int): Искомый элемент
        left (int): Левая граница поиска
        right (Optional[int]): Правая граница поиска

    Returns:
        Optional[int]: Индекс элемента или None, если не найден
    """
    if right is None:
        right = len(arr) - 1

    # Базовый случай: элемент не найден
    if left > right:
        return None

    # Находим средний элемент
    mid = (left + right) // 2

    # Базовый случай: элемент найден
    if arr[mid] == target:
        return mid

    # Рекурсивный шаг
    if arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    return binary_search_recursive(arr, target, mid + 1, right)


def traverse_filesystem(
    path: str,
    level: int = 0,
    max_depth: Optional[int] = None
) -> int:
    """
    Рекурсивный обход файловой системы с выводом дерева.

    Args:
        path (str): Путь для начала обхода
        level (int): Текущий уровень вложенности
        max_depth (Optional[int]): Максимальная глубина рекурсии

    Returns:
        int: Количество найденных файлов и директорий

    Raises:
        FileNotFoundError: Если указанный путь не существует
    """
    if max_depth is not None and level >= max_depth:
        return 0

    if not os.path.exists(path):
        raise FileNotFoundError(f"Путь не существует: {path}")

    total_count = 0
    indent = "  " * level

    try:
        items = os.listdir(path)
    except PermissionError:
        print(f"{indent}[Ошибка доступа: {os.path.basename(path)}]")
        return 0

    for item in sorted(items):
        item_path = os.path.join(path, item)
        total_count += 1

        if os.path.isdir(item_path):
            print(f"{indent}📁 {item}/")
            total_count += traverse_filesystem(
                item_path, level + 1, max_depth
            )
        else:
            print(f"{indent}📄 {item}")

    return total_count


class TowersOfHanoi:
    """Класс для решения задачи 'Ханойские башни'."""

    def __init__(self):
        self.moves = []

    def solve(
        self,
        n: int,
        source: str = "A",
        auxiliary: str = "B",
        destination: str = "C"
    ) -> List[Tuple[int, str, str]]:
        """
        Решение задачи Ханойские башни для n дисков.

        Временная сложность: O(2^n)
        Глубина рекурсии: O(n)

        Args:
            n (int): Количество дисков
            source (str): Исходный стержень
            auxiliary (str): Вспомогательный стержень
            destination (str): Целевой стержень

        Returns:
            List[Tuple[int, str, str]]: Список перемещений
        """
        self.moves = []
        self._move_disks(n, source, auxiliary, destination)
        return self.moves

    def _move_disks(
        self,
        n: int,
        source: str,
        auxiliary: str,
        destination: str
    ):
        """
        Вспомогательная рекурсивная функция для перемещения дисков.

        Args:
            n (int): Количество дисков для перемещения
            source (str): Исходный стержень
            auxiliary (str): Вспомогательный стержень
            destination (str): Целевой стержень
        """
        if n == 1:
            self.moves.append((1, source, destination))
            return

        # Перемещаем n-1 дисков с source на auxiliary
        self._move_disks(n - 1, source, destination, auxiliary)

        # Перемещаем самый большой диск на destination
        self.moves.append((n, source, destination))

        # Перемещаем n-1 дисков с auxiliary на destination
        self._move_disks(n - 1, auxiliary, source, destination)

    def print_solution(self, n: int):
        """
        Вывод решения задачи на экран.

        Args:
            n (int): Количество дисков
        """
        print(f"\nРешение задачи 'Ханойские башни' для {n} дисков:")
        print("=" * 40)

        moves = self.solve(n)
        for i, (disk, source, destination) in enumerate(moves, 1):
            msg = f"{i:3}. Переместить диск {disk} с {source} на {destination}"
            print(msg)

        total_moves = len(moves)
        min_possible = 2 ** n - 1
        print(f"\nВсего перемещений: {total_moves}")
        print(f"Минимально возможное: {min_possible}")


def measure_recursion_depth():
    """
    Измерение максимальной глубины рекурсии для разных задач.
    """
    import sys

    print("\nИзмерение максимальной глубины рекурсии:")
    print("=" * 50)

    # Получаем лимит глубины рекурсии
    recursion_limit = sys.getrecursionlimit()
    print(f"Лимит глубины рекурсии в Python: {recursion_limit}")

    # Создаем глубоко вложенную структуру для тестирования
    test_dir = "test_deep_structure"
    os.makedirs(test_dir, exist_ok=True)

    # Создаем глубокую вложенность
    current_path = test_dir
    max_test_depth = 20

    for i in range(max_test_depth):
        new_dir = os.path.join(current_path, f"level_{i}")
        os.makedirs(new_dir, exist_ok=True)
        current_path = new_dir

        # Создаем файл на каждом уровне
        file_path = os.path.join(current_path, f"file_{i}.txt")
        with open(file_path, "w") as f:
            f.write(f"Test file at level {i}")

    msg = f"Создана тестовая структура глубиной {max_test_depth} уровней"
    print(f"\n{msg}")

    # Тестируем обход с разной глубиной
    for depth in [5, 10, 15, 20]:
        print(f"\nОбход с ограничением глубины {depth}:")
        try:
            count = traverse_filesystem(test_dir, max_depth=depth)
            print(f"Найдено элементов: {count}")
        except Exception as e:
            print(f"Ошибка: {e}")

    # Очистка тестовой структуры
    import shutil
    shutil.rmtree(test_dir)


if __name__ == "__main__":
    # Пример бинарного поиска
    print("Бинарный поиск:")
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 13
    result = binary_search_recursive(arr, target)
    print(f"Массив: {arr}")
    print(f"Ищем {target}: индекс {result}")

    # Пример обхода файловой системы (текущая директория)
    print("\nОбход файловой системы (текущая директория, глубина 2):")
    try:
        count = traverse_filesystem(".", max_depth=2)
        print(f"\nВсего элементов: {count}")
    except Exception as e:
        print(f"Ошибка при обходе: {e}")

    # Ханойские башни
    hanoi = TowersOfHanoi()
    hanoi.print_solution(3)

    # Измерение глубины рекурсии
    measure_recursion_depth()
