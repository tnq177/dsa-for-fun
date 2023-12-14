"""
ID: toannq12
LANG: PYTHON3
TASK: runround
"""
import math


def list2num(path):
    res = 0
    for digit in path:
        res = res * 10 + digit
    return res


def generate_runround(num_digits):
    res = []

    def f(i, path, remain, digits):
        if remain == 0:
            if i == 0:
                res.append(list2num(path))
            return
        if path[i] is not None:
            return
        candidates = list(digits)
        for d in candidates:
            path[i] = d
            digits.remove(d)
            f((i + d) % len(path), path, remain - 1, digits)
            digits.add(d)
            path[i] = None

    f(0, [None] * num_digits, num_digits, set(range(1, 10)))
    return res


def main():
    with open("runround.in", "r") as f:
        M = int(f.readline().strip())

    num_digits = int(math.log10(M)) + 1
    res = None

    runrounds = generate_runround(num_digits)
    for num in runrounds:
        if num > M and (res is None or res > num):
            res = num

    if res is None:
        runrounds = generate_runround(num_digits + 1)
        res = min(runrounds)

    with open("runround.out", "w") as f:
        f.write(f"{res}\n")


if __name__ == "__main__":
    main()
