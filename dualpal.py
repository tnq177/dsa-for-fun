"""
ID: toannq12
LANG: PYTHON3
TASK: dualpal
"""


def convert2base(num, base):
    if num == 0:
        return [0]
    arr = []
    while num:
        arr.append(num % base)
        num //= base
    return arr


def is_pali(arr):
    i, j = 0, len(arr) - 1
    while i < j:
        if arr[i] != arr[j]:
            return False
        i, j = i + 1, j - 1
    return True


def main():
    with open("dualpal.in", "r") as f:
        N, S = f.readline().strip().split()
    N = int(N)
    S = int(S)
    count = 0
    num = S
    with open("dualpal.out", "w") as f:
        while count < N:
            num += 1
            multipali = 0
            for base in range(2, 11):
                arr = convert2base(num, base)
                if is_pali(arr):
                    multipali += 1
                if multipali >= 2:
                    break
            if multipali >= 2:
                f.write(f"{num}\n")
                count += 1


if __name__ == "__main__":
    main()
