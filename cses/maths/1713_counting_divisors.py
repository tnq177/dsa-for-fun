def main():
    dp = [2] * 1000001
    dp[1] = 1
    for i in range(2, len(dp)):
        for j in range(i + i, len(dp), i):
            dp[j] += 1

    n = int(input().strip())
    res = []
    for _ in range(n):
        print(dp[int(input().strip())])


main()
