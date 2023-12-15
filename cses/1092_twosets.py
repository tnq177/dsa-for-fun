def main():
    n = int(input())
    total = (n + 1) * n // 2
    if total % 2 != 0:
        print("NO")
        return

    if n % 2 == 0:
        s1, s2 = [], []
        i, j = 1, n
        flip = True
        while i < j:
            append = s1.append if flip else s2.append
            flip = not flip
            append(i)
            append(j)
            i += 1
            j -= 1
        print("YES")
        print(n // 2)
        print(*s1, sep=" ")
        print(n // 2)
        print(*s2, sep=" ")
        return

    if (n + 1) % 4 != 0:
        print("NO")
        return

    nums = set(range(1, n + 1))
    s1 = [(n + 1) // 4, (n + 1) // 2]
    s2 = [3 * (n + 1) // 4]
    reserve = set(s1 + s2)
    i, j = 1, n
    flip = True
    while i < j:
        if i in reserve or j in reserve:
            i += 1
            j -= 1
            continue
        append = s1.append if flip else s2.append
        flip = not flip
        append(i)
        append(j)
        i += 1
        j -= 1
    print("YES")
    print(len(s1))
    print(*s1, sep=" ")
    print(len(s2))
    print(*s2, sep=" ")


main()
