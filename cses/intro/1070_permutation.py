n = int(input())
if n == 1:
    print(n)
if n <= 3:
    print("NO SOLUTION")
else:
    res = []
    i, j = 1, n
    while i <= j:
        if i == j:
            res = [i] + res
            break
        elif i == j - 1:
            res = [j] + res + [i]
            break
        else:
            res.append(i)
            res.append(j)
            i += 1
            j -= 1
    res = [str(x) for x in res]
    print(" ".join(res) + "\n")