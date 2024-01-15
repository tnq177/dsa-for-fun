def main():
    _ = int(input())
    coins = [int(x) for x in input().strip().split()]
    total = sum(coins)
    coins.sort()
    coins = [-1] + coins

    dp = [[True] * len(coins)] + [[False] * len(coins) for _ in range(total + 1)]
    for coin_sum in range(1, total + 1):
        dp[coin_sum][0] = False

    for coin_sum in range(1, total + 1):
        for i in range(1, len(coins)):
            coin = coins[i]
            if coin_sum < coin:
                dp[coin_sum][i] = dp[coin_sum][i - 1]
            else:
                dp[coin_sum][i] = dp[coin_sum][i - 1] or dp[coin_sum - coin][i - 1]

    possible_sums = [coin_sum for coin_sum in range(1, total + 1) if dp[coin_sum][-1]]
    print(len(possible_sums))
    print(*possible_sums)


main()
