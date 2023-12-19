def main():
    n = int(input())
    nums = [int(x) for x in input().strip().split()]

    l2r = [0]
    for num in nums:
        l2r.append(num + l2r[-1])

    dp = [[0] * n for _ in range(n)]
    for l in range(1, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if i == j:
                dp[i][j] = nums[i]
            else:
                sum_left = l2r[j + 1] - l2r[i + 1]
                sum_right = l2r[j] - l2r[i]
                left = nums[i] + sum_left - dp[i + 1][j]
                right = nums[j] + sum_right - dp[i][j - 1]
                dp[i][j] = max(left, right)

    print(dp[0][-1])


main()
