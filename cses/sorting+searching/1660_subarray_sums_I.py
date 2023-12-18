def main():
    n, target = [int(x) for x in input().strip().split()]
    nums = [int(x) for x in input().strip().split()]
    from collections import Counter

    cs = 0
    res = 0
    count = Counter()
    for num in nums:
        cs += num
        if cs == target:
            res += 1
        elif (cs - target) in count:
            res += count[cs - target]
        count[cs] += 1

    print(res)


main()
