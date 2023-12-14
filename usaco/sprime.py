"""
ID: toannq12
LANG: PYTHON3
TASK: sprime
"""
import math


def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    max_factor = int(num**0.5) + 1
    for factor in range(3, max_factor + 1, 2):
        if num % factor == 0:
            return False
    return True


def main():
    with open("sprime.in", "r") as f:
        N = int(f.readline().strip())

    if N == 1:
        res = [2, 3, 5, 7]
    else:
        res = []

        def dfs(num, num_digits):
            if num_digits == N:
                res.append(num)
                return
            for d in range(1, 10, 2):
                new_num = num * 10 + d
                if is_prime(new_num):
                    dfs(new_num, num_digits + 1)

        for num in [2, 3, 5, 7]:
            dfs(num, 1)

    with open("sprime.out", "w") as f:
        for num in res:
            f.write(f"{num}\n")


if __name__ == "__main__":
    main()
