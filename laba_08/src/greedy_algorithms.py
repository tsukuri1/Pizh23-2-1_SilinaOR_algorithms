"""
Реализации классических жадных алгоритмов.
Все алгоритмы соответствуют принципам жадного выбора.
"""

import heapq
from typing import List, Tuple, Dict
from collections import Counter


def interval_scheduling(
    intervals: List[Tuple[float, float]]
) -> List[Tuple[float, float]]:
    """
    Выбирает максимальное количество непересекающихся интервалов.

    Args:
        intervals: Список интервалов в формате (start, end)

    Returns:
        Список выбранных интервалов
    """
    if not intervals:
        return []

    intervals_sorted = sorted(intervals, key=lambda x: x[1])
    selected = []
    last_end = float('-inf')

    for start, end in intervals_sorted:
        if start >= last_end:
            selected.append((start, end))
            last_end = end

    return selected


def fractional_knapsack(
    items: List[Tuple[float, float]], capacity: float
) -> Tuple[float, List[Tuple[int, float]]]:
    """
    Решает задачу о непрерывном (дробном) рюкзаке.

    Args:
        items: Список предметов в формате (вес, цена)
        capacity: Вместимость рюкзака

    Returns:
        Кортеж (максимальная стоимость, список взятых предметов)
    """
    if capacity <= 0 or not items:
        return 0.0, []

    items_with_ratio = []
    for i, (weight, value) in enumerate(items):
        if weight > 0:
            items_with_ratio.append((value / weight, weight, value, i))

    items_with_ratio.sort(reverse=True, key=lambda x: x[0])

    total_value = 0.0
    taken_items = []
    remaining = capacity

    for ratio, weight, value, idx in items_with_ratio:
        if remaining <= 0:
            break

        taken = min(weight, remaining)
        fraction = taken / weight

        total_value += fraction * value
        taken_items.append((idx, fraction))
        remaining -= taken

    return total_value, taken_items


class HuffmanNode:
    """Узел дерева Хаффмана."""

    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def huffman_coding(text: str) -> Tuple[Dict[str, str], HuffmanNode]:
    """
    Строит оптимальный префиксный код Хаффмана для заданного текста.

    Args:
        text: Входной текст

    Returns:
        Кортеж (словарь кодов, корень дерева)
    """
    if not text:
        return {}, None

    freq = Counter(text)
    heap = [HuffmanNode(char=ch, freq=count) for ch, count in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged_freq = left.freq + right.freq
        merged = HuffmanNode(freq=merged_freq, left=left, right=right)
        heapq.heappush(heap, merged)

    root = heap[0] if heap else None
    codes = {}

    def traverse(node, code):
        if not node:
            return
        if node.char:
            codes[node.char] = code
        else:
            traverse(node.left, code + '0')
            traverse(node.right, code + '1')

    if root:
        traverse(root, '')

    return codes, root


def min_coins_greedy(
    amount: int, coins: List[int]
) -> Tuple[int, Dict[int, int]]:
    """
    Находит минимальное количество монет для выдачи суммы.

    Args:
        amount: Сумма для выдачи
        coins: Доступные номиналы монет

    Returns:
        Кортеж (общее количество монет, словарь {номинал: количество})
    """
    if amount <= 0:
        return 0, {}

    coins_sorted = sorted(coins, reverse=True)
    result = {}
    remaining = amount

    for coin in coins_sorted:
        if coin <= 0 or remaining < coin:
            continue

        count = remaining // coin
        if count > 0:
            result[coin] = count
            remaining -= count * coin

    if remaining > 0:
        raise ValueError(f"Невозможно выдать сумму {amount}")

    return sum(result.values()), result


class UnionFind:
    """Структура данных для системы непересекающихся множеств."""

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


def kruskal_mst(
    vertices: int, edges: List[Tuple[int, int, float]]
) -> List[Tuple[int, int, float]]:
    """
    Алгоритм Краскала для построения минимального остовного дерева.

    Args:
        vertices: Количество вершин
        edges: Список ребер в формате (вершина1, вершина2, вес)

    Returns:
        Список ребер минимального остовного дерева
    """
    edges_sorted = sorted(edges, key=lambda x: x[2])
    uf = UnionFind(vertices)
    mst = []

    for u, v, weight in edges_sorted:
        if uf.union(u, v):
            mst.append((u, v, weight))
            if len(mst) == vertices - 1:
                break

    return mst
