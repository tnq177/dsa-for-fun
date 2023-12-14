"""
ID: toannq12
LANG: PYTHON3
TASK: range
"""


def main():
    with open("range.in", "r") as f:
        N = int(f.readline().strip())
        field = [f.readline().strip() for _ in range(N)]
    max_square = [[0] * N for _ in range(N)]

    from collections import Counter

    res = Counter()
    for r in range(N):
        for c in range(N):
            if r == 0 or c == 0:
                max_square[r][c] = 1 if field[r][c] == "1" else 0
            elif field[r][c] == "1":
                size = min(max_square[r - 1][c], max_square[r - 1][c - 1])
                size = min(size, max_square[r][c - 1])
                max_square[r][c] = size + 1

            # only need to record the maximum squares
            if max_square[r][c] >= 2:
                res[max_square[r][c]] += 1

    # previously we only record the maximum square
    # we can use that to update the number of smaller squares
    sizes = sorted(res.keys(), reverse=True)
    for size in sizes:
        if size - 1 >= 2:
            res[size - 1] += res[size]
    sizes = sizes[::-1]
    with open("range.out", "w") as f:
        for size in sizes:
            f.write(f"{size} {res[size]}\n")


if __name__ == "__main__":
    main()
