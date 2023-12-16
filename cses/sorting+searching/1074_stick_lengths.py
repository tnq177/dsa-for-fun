def main():
    _ = input()
    nums = input().strip().split()
    nums = [int(x) for x in nums]
    nums.sort()
    r2l = [0] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        r2l[i] = nums[i] if i == len(nums) - 1 else r2l[i + 1] + nums[i]

    sum_left = 0
    best = float("inf")
    for i, num in enumerate(nums):
        num_left = i
        num_right = len(nums) - i - 1
        sum_right = 0 if i == len(nums) - 1 else r2l[i + 1]
        cost = sum_right - num_right * num + num_left * num - sum_left
        best = min(best, cost)
        sum_left += num
    print(best)


main()
