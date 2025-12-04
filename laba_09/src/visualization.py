"""Визуализация таблиц ДП."""

from dynamic_programming import lcs


def print_dp_table(dp, title="Таблица ДП"):
    """Печать таблицы ДП."""
    print(f"\n{title}:")
    for row in dp:
        print(' '.join(f'{val:3}' for val in row))
    print()


def visualize_lcs(str1: str, str2: str):
    """Визуализация таблицы LCS."""
    n, m = len(str1), len(str2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    print("   ∅ " + ' '.join(f'{c:2}' for c in str2))

    for i in range(n + 1):
        row = []
        row_char = '∅' if i == 0 else str1[i - 1]
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            row.append(dp[i][j])
        print(f"{row_char:2} " + ' '.join(f'{val:2}' for val in row))

    return dp


if __name__ == "__main__":
    str1 = "AGGTAB"
    str2 = "GXTXAYB"
    print(f"LCS для '{str1}' и '{str2}':")
    dp = visualize_lcs(str1, str2)

    length, sequence = lcs(str1, str2)
    print(f"\nДлина LCS: {length}")
    print(f"LCS: {sequence}")
