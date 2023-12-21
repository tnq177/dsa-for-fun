"""
Wonderful explanation https://cp-algorithms.com/sequences/longest_increasing_subsequence.html
"""
def main():
    n = int(input())
    nums = [int(x) for x in input().strip().split()]
    INF = 10**9 + 1
    dp = [INF] * (n + 1)
    dp[0] = -INF

    def binary_search(num):
        # look for the first number dp[i] in the range [1, n]
        # that dp[i] > num
        if num > dp[n]:
            return n + 1
        if num < dp[1]:
            return 1
        l, r = 1, n
        while l < r:
            if r - l + 1 <= 3:
                for i in range(l, r + 1):
                    if dp[i] > num:
                        return i
            else:
                m = (l + r) // 2
                if dp[m - 1] <= num < dp[m]:
                    return m
                elif dp[m] <= num < dp[m + 1]:
                    return m + 1
                if dp[m] < num:
                    l = m + 1
                else:
                    r = m - 1

    for num in nums:
        l = binary_search(num)
        if l <= n and dp[l - 1] < num < dp[l]:
            dp[l] = num

    res = 0
    for i, val in enumerate(dp):
        if val < INF:
            res = i

    print(res)


main()
