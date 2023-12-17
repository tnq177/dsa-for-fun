def main():
    starts = [(10, 2)]
    digit = 2
    MAX = 10**18
    while True:
        new_start = (10**digit - 10 ** (digit - 1)) * digit + starts[-1][0]
        starts.append((new_start, digit + 1))
        digit += 1
        if new_start > MAX:
            break

    def search_digits(num_digits, k):
        """
        view this as a matrix of
        rows = 9 * 10 ** (num_digits - 1) rows
        and cols = num_digits
        like:
        10
        11
        12
        13
        ...
        99

        The last column repeats 0,1,2,...9
        The next to last column: 10x0, 10x1, 10x2....
        and so on.
        so we just need to find which bucket it belongs to
        by first dividing by repeating period, then mod 10.

        The first column is special as it goes 1 -> 9
        """
        cols = num_digits
        c = k % cols
        r = k // cols
        if c == 0:
            res = r // 10 ** (num_digits - 1) + 1
        else:
            repeat_period = 10 ** (cols - c - 1)
            res = (r // repeat_period) % 10
        return res

    def search(k):
        if k < 10:
            return k
        for i in range(len(starts) - 1):
            if starts[i][0] <= k < starts[i + 1][0]:
                return search_digits(starts[i][1], k - starts[i][0])

    q = int(input())
    for _ in range(q):
        k = int(input())
        res = search(k)
        print(res)


main()
