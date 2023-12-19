def main():
    n = int(input())
    target = n * (n + 1) // 2
    if target % 2 != 0:
        print(0)
        return

    target //= 2
    dp = [[1] * (n + 1)] + [[0] * (n + 1) for _ in range(target)]

    MOD = 2 * (10**9 + 7)
    for amount in range(1, target + 1):
        min_n = ((1 + 8 * amount) ** 0.5 - 1) / 2
        min_n = max(1, int(min_n))
        for num in range(min_n, n + 1):
            if amount < num:
                dp[amount][num] = dp[amount][num - 1]
            else:
                dp[amount][num] = (
                    dp[amount][num - 1] + dp[amount - num][num - 1]
                ) % MOD

    res = dp[-1][-1] // 2
    print(res)


main()
