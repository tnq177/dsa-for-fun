def main():
    t = int(input())
    for _ in range(t):
        r, c = [int(x) for x in input().strip().split()]
        round = max(r, c)
        end = round * round
        start = round * round - 2 * round + 2
        if r == c:
            res = (start + end) // 2
        elif r < c:
            increasing = c % 2 == 0
            if increasing:
                res = start + r - 1
            else:
                res = end - (r - 1)
        else:
            increasing = r % 2 != 0
            if increasing:
                res = start + c - 1
            else:
                res = end - (c - 1)

        print(res)


main()
