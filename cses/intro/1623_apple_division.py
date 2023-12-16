def main():
    _ = int(input())
    nums = [int(x) for x in input().strip().split()]
    total = sum(nums)
    res = [float("inf")]

    if len(nums) == 1:
        print(nums[0])
        return

    def dfs(i, sum):
        if i == len(nums):
            if 0 < sum < total:
                diff = abs(total - sum - sum)
                res[0] = min(res[0], diff)
            return

        # take nums[i]
        sum += nums[i]
        dfs(i + 1, sum)
        sum -= nums[i]

        # don't take nums[i]
        dfs(i + 1, sum)

    dfs(0, 0)
    print(res[0])


main()
