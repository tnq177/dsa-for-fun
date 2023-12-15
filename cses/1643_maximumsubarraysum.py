def main():
    _ = input()
    nums = input().strip().split()
    nums = [int(x) for x in nums]
    minsofar = 0
    cs = 0
    res = float("-inf")
    for num in nums:
        cs += num
        best = cs - minsofar
        res = max(res, best)
        minsofar = min(minsofar, cs)

    print(res)

main()