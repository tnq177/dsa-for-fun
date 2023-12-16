def main():
    _ = input()
    nums = input().strip().split()
    seen = set()
    for num in nums:
        seen.add(num)
    print(len(seen))

def main2():
    _ = input()
    nums = input().strip().split()
    nums = [int(x) for x in nums]
    nums.sort()
    res = 0
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i - 1]:
            res += 1
    print(res)

# main()
main2()
