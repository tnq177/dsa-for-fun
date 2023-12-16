from collections import Counter

x = input().strip()
count = Counter(x)
num_odd = sum([1 if count[k] % 2 != 0 else 0 for k in count])
if num_odd > 1:
    print("NO SOLUTION")
else:
    res = [""] * len(x)
    even, odd = [], []
    for k in count:
        if count[k] % 2 == 0:
            even.append(k)
        else:
            odd.append(k)
    i, j = 0, len(x) - 1
    while even:
        ch = even.pop()
        ch_count = count[ch]
        while ch_count:
            res[i] = res[j] = ch
            ch_count -= 2
            i += 1
            j -= 1

    for k in range(i, j + 1):
        res[k] = odd[0]

    print("".join(res))
