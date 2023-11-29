"""
ID: toannq12
LANG: PYTHON3
TASK: subset
"""


def count(N):
    total = N * (N + 1) // 2
    if total % 2 != 0:
        return 0

    total = total // 2
    dp = [[1] * (N + 1)] + [[0] * (N + 1) for _ in range(total)]
    for amount in range(1, total + 1):
        for num in range(N + 1):
            if amount < num:
                dp[amount][num] = dp[amount][num - 1]
            else:
                dp[amount][num] = dp[amount][num - 1] + dp[amount - num][num - 1]

    return dp[-1][-1] // 2


def main():
    with open("subset.in", "r") as f:
        N = int(f.readline().strip())

    res = count(N)
    with open("subset.out", "w") as f:
        f.write(f"{res}\n")


if __name__ == "__main__":
    main()
