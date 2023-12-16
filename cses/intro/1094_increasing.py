_ = input()
nums = [int(x) for x in input().strip().split()]
res = 0
for i in range(1, len(nums)):
    if nums[i] < nums[i - 1]:
        res += nums[i - 1] - nums[i]
        nums[i] = nums[i - 1]

print(res)