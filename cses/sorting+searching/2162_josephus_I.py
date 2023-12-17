def main():
    n = int(input())
    if n == 1:
        print(1)
        return

    res = []
    picked = [False] * n
    i = 1
    skip = False
    while len(res) < n:
        if not picked[i]:
            if len(res) == n - 1 or not skip:
                picked[i] = True
                res.append(i + 1)
            skip = not skip
        i = (i + 1) % n

    print(*res, sep=" ")


main()
