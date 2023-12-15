n = int(input())
MAX = 2**n

res = [0, 1]
for _ in range(n - 1):
    new_res = []
    flip = True
    for prev_num in res:
        if flip:
            added = [0, 1]
        else:
            added = [1, 0]
        flip = not flip
        for bit in added:
            new_res.append(prev_num * 2 + bit)
    res = new_res

for num in res:
    x = num
    binary = []
    for _ in range(n):
        binary.append(x % 2)
        x //= 2
    binary = binary[::-1]
    print(*binary, sep="")