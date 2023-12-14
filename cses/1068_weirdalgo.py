n = int(input())
res = []
while True:
    res.append(str(n))
    if n == 1:
        break
    if n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1

print(" ".join(res) + "\n")
