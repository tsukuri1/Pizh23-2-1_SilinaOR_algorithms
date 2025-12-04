"""Решение практических задач ДП."""

from typing import List, Tuple


def coin_change(coins: List[int], amount: int) -> int:
    """Минимальное количество монет для суммы O(n*m)."""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


def lis(nums: List[int]) -> int:
    """LIS за O(n^2)."""
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def lis_with_sequence(nums: List[int]) -> Tuple[int, List[int]]:
    """LIS с восстановлением последовательности."""
    if not nums:
        return 0, []

    n = len(nums)
    dp = [1] * n
    prev = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    max_len = max(dp)
    max_idx = dp.index(max_len)

    sequence = []
    idx = max_idx
    while idx != -1:
        sequence.append(nums[idx])
        idx = prev[idx]

    return max_len, list(reversed(sequence))


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    result = coin_change(coins, amount)
    print(f"Размен {amount} монетами {coins}: {result}")

    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    length, seq = lis_with_sequence(nums)
    print(f"LIS для {nums}: длина={length}, последовательность={seq}")
