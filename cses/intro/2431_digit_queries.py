def main():
    starts = [(10, 2)]
    digit = 2
    MAX = 10 ** 18
    while True:
        new_start = (10**digit - 10 ** (digit - 1)) * digit + starts[-1][0]
        starts.append((new_start, digit + 1))
        digit += 1
        if new_start > MAX:
            break

    def search_digits(num_digits, k):
        res = []
        while num_digits:
            cols = 10 ** (num_digits - 1) * num_digits
            r = k // cols
            res.append(r + 1)
            k = k % cols
            num_digits -= 1
        return res[::-1]


    def search(k):
        if k < 10:
            return k
        for i in range(len(starts) - 1):
            if starts[i][0] <= k < starts[i + 1][0]:
                return search_digits(starts[i][1], k - starts[i][0])

    print(starts)
    return

    q = int(input())
    for _ in range(q):
        k = int(input())
        res = search(k)
        print(res)

main()