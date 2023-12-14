x = input().strip()
curr = None
count = 0
res = 0
for ch in x:
    if curr is None or curr != ch:
        curr = ch
        count = 1
    else:
        count += 1
    res = max(res, count)

print(res)
