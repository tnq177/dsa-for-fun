"""
ID: toannq12
LANG: PYTHON3
TASK: milk2
"""


def main():
    points = []
    with open("milk2.in", "r") as f:
        N = int(f.readline().strip())
        for _ in range(N):
            start, end = f.readline().strip().split()
            points.append((int(start), -1))
            points.append((int(end), 1))
    points.sort(key=lambda x: (x[0], x[1]))
    start = None
    count = 0
    max_cont = 0
    max_dist = 0
    for i, (p, is_start) in enumerate(points):
        if i != 0 and count == 0:
            max_dist = max(max_dist, p - points[i - 1][0])

        if start is None:
            start = p

        is_start = is_start > 0
        if is_start:
            count += 1
        else:
            count -= 1

        if count == 0:
            max_cont = max(max_cont, p - start)
            start = None

    with open("milk2.out", "w") as f:
        f.write(f"{max_cont} {max_dist}\n")


if __name__ == "__main__":
    main()
