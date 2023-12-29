def main():
    n = int(input())
    nums = [int(x) for x in input().strip().split()]
    cache = {}
    idx = 0
    for num in nums:
        if num - 1 not in cache:
            idx += 1
            cache[num] = idx
        else:
            cache[num] = cache[num - 1]

    print(max(cache.values()))


main()
