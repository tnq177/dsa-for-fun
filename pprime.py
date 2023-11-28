"""
ID: toannq12
LANG: PYTHON3
TASK: pprime
"""
import math


def is_prime(num):
    if num % 2 == 0:
        return False
    max_factor = int(num**0.5) + 1
    for factor in range(3, max_factor + 1, 2):
        if num % factor == 0:
            return False
    return True


def main():
    with open("pprime.in", "r") as f:
        ab = f.readline().strip().split()
        a, b = [int(x) for x in ab]

    low = int(math.log10(a) + 1)
    high = int(math.log10(b) + 1)

    res = []

    def gen_palin(i, path):
        j = len(path) - 1 - i
        if i > j:
            num = 0
            for d in path:
                num = num * 10 + d
            if a <= num <= b and is_prime(num):
                res.append(num)
        else:
            if i == 0:
                digits = range(1, 10)
            else:
                digits = range(10)

            for d in digits:
                path[i] = path[j] = d
                gen_palin(i + 1, path)
                path[i] = path[j] = 0

    for num_digits in range(low, high + 1):
        path = [0] * num_digits
        gen_palin(0, path)

    res.sort()
    with open("pprime.out", "w") as f:
        for num in res:
            f.write(f"{num}\n")


if __name__ == "__main__":
    main()
