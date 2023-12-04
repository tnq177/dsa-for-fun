"""
ID: toannq12
LANG: PYTHON3
TASK: kimbits
"""


def main():
    with open("kimbits.in", "r") as f:
        N, L, I = [int(x) for x in f.readline().strip().split()]

    cache = {}

    def n_choose_k(n, k):
        if k == n or k == 0:
            return 1
        if n == 0:
            return 0
        if (n, k) in cache:
            return cache[(n, k)]
        res = n_choose_k(n - 1, k) + n_choose_k(n - 1, k - 1)
        cache[(n, k)] = res
        return res

    def find(num_bits, num_ones, order, path):
        if len(path) == N:
            return
        # how many has num_ones 1s and start with zero
        zero = 0
        for _num_ones in range(num_ones + 1):
            if num_bits - 1 >= _num_ones:
                zero += n_choose_k(num_bits - 1, _num_ones)
        if order > zero:
            # gotta start with 1
            path.append("1")
            find(num_bits - 1, num_ones - 1, order - zero, path)
        else:
            path.append("0")
            find(num_bits - 1, num_ones, order, path)

    path = []
    find(N, L, I, path)
    path = "".join(path)
    with open("kimbits.out", "w") as f:
        f.write(path + "\n")


if __name__ == "__main__":
    main()
