def main():
    target = int(input().strip().split()[-1])
    nums = [int(x) for x in input().strip().split()]
    nums = [(num, i + 1) for i, num in enumerate(nums)]
    nums.sort(key=lambda x: x[0])

    for i in range(len(nums) - 2):
        j, k = i + 1, len(nums) - 1
        while j < k:
            sum = nums[j][0] + nums[k][0]
            if sum > target - nums[i][0]:
                k -= 1
            elif sum < target - nums[i][0]:
                j += 1
            else:
                print(nums[i][1], nums[j][1], nums[k][1])
                return

    print("IMPOSSIBLE")


main()
