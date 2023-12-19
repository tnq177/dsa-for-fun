def main():
    n = int(input())
    dp = [0] * (n + 1)
    for num in range(n + 1):
        if num < 10:
            dp[num] = 1 if num > 0 else 0
        else:
            minval = float("inf")
            x = num
            while x:
                d = x % 10
                x //= 10
                if d:
                    minval = min(minval, dp[num - d] + 1)
            dp[num] = minval

    print(dp[-1])


main()
