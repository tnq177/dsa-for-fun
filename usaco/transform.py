"""
ID: toannq12
LANG: PYTHON3
TASK: transform
"""


def clock90(arr):
    N = len(arr)
    out = [[""] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            out[c][N - 1 - r] = arr[r][c]
    return out


def clock180(arr):
    return clock90(clock90(arr))


def clock270(arr):
    return clock90(clock180(arr))


def reflect(arr):
    return [x[::-1] for x in arr]


def comb90(arr):
    return clock90(reflect(arr))


def comb180(arr):
    return clock180(reflect(arr))


def comb270(arr):
    return clock270(reflect(arr))


def same(arr1, arr2):
    return all(x1 == x2 for x1, x2 in zip(arr1, arr2))


def main():
    with open("transform.in", "r") as f:
        N = int(f.readline().strip())
        arr = []
        for _ in range(N):
            arr.append(list(f.readline().strip()))
        target = []
        for _ in range(N):
            target.append(list(f.readline().strip()))

    if same(clock90(arr), target):
        res = 1
    elif same(clock180(arr), target):
        res = 2
    elif same(clock270(arr), target):
        res = 3
    elif same(reflect(arr), target):
        res = 4
    elif (
        same(comb90(arr), target)
        or same(comb180(arr), target)
        or same(comb270(arr), target)
    ):
        res = 5
    elif same(arr, target):
        res = 6
    else:
        res = 7

    with open("transform.out", "w") as f:
        f.write(f"{res}\n")


if __name__ == "__main__":
    main()
