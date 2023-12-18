def main():
    n, goal = [int(x) for x in input().strip().split()]
    nums = [(int(x), i) for i, x in enumerate(input().strip().split())]
    nums.sort(key=lambda x: x[0])

    for i in range(len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            target = goal - (nums[i][0] + nums[j][0])
            if target <= 0:
                continue
            k, l = j + 1, len(nums) - 1
            while k < l:
                sum = nums[k][0] + nums[l][0]
                if sum == target:
                    print(
                        nums[i][1] + 1,
                        nums[j][1] + 1,
                        nums[k][1] + 1,
                        nums[l][1] + 1,
                    )
                    return
                elif sum > target:
                    l -= 1
                else:
                    k += 1

    print("IMPOSSIBLE")


main()
