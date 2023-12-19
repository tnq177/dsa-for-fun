def main():
    s1 = input().strip()
    s2 = input().strip()
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    for j in range(len(s2) + 1):
        dp[0][j] = j
    for i in range(len(s1) + 1):
        dp[i][0] = i

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                c1 = dp[i][j - 1]
                c2 = dp[i - 1][j]
                c3 = dp[i - 1][j - 1]
                dp[i][j] = min(min(c1, c2), c3) + 1

    print(dp[-1][-1])


main()
