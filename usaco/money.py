"""
ID: toannq12
LANG: PYTHON3
TASK: money
"""


def main():
    with open("money.in", "r") as f:
        N = 0
        coins = []
        for i, line in enumerate(f):
            if i == 0:
                N = [int(x) for x in line.strip().split()][1]
            else:
                coins.extend([int(x) for x in line.strip().split()])

    coins = [c for c in coins if c <= N]
    coins = list(set(coins))
    coins.sort()
    dp = [1] + [0] * N
    for coin in coins:
        for amount in range(1, N + 1):
            if amount >= coin:
                dp[amount] += dp[amount - coin]

    with open("money.out", "w") as f:
        f.write(f"{dp[-1]}\n")


if __name__ == "__main__":
    main()
