import sys


def main():
    _, target = input().strip().split()
    nums = input().strip().split()
    target = int(target)
    nums = [(int(x), i) for i, x in enumerate(nums)]
    nums.sort(key=lambda x: x[0])
    i, j = 0, len(nums) - 1
    while i < j:
        sum = nums[i][0] + nums[j][0]
        if sum > target:
            j -= 1
        elif sum < target:
            i += 1
        else:
            print(nums[i][1] + 1, nums[j][1] + 1)
            return

    print("IMPOSSIBLE")


main()
