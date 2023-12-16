n = int(input())
nums = [int(x) for x in input().strip().split()]
total = sum(nums)
print(n * (n + 1) // 2 - total)