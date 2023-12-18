def main():
    n, target = [int(x) for x in input().strip().split()]
    nums = [int(x) for x in input().strip().split()]
    from collections import Counter

    cs = 0
    res = 0
    count = Counter()
    i = 0
    while i < len(nums):
        if nums[i] != 0:
            cs += nums[i]
            if cs == target:
                res += 1
            if cs - target in count:
                res += count[cs - target]
            count[cs] += 1
            i += 1
        else:
            j = i
            while j < len(nums) and nums[j] == 0:
                j += 1
            num_0 = j - i
            i = j
             # count for the first 0
            if cs == target:
                res += 1
            if cs - target in count:
                res += count[cs - target]
            count[cs] += 1

            # count for the rest num_0 - 1
            if cs == target:
                res += num_0 - 1
            if cs - target in count:
                a = count[cs - target]
                res += a * (num_0 - 1) + (num_0 - 1) * (num_0 - 2) // 2
            count[cs] += num_0 - 1

    print(res)


main()
