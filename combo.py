"""
ID: toannq12
LANG: PYTHON3
TASK: combo
"""


def format(d, N):
    d -= 1
    d = d % N
    return d + 1


def main():
    with open("combo.in", "r") as f:
        N = int(f.readline().strip())
        c1 = f.readline().strip().split()
        c2 = f.readline().strip().split()
        c1 = [int(x) for x in c1]
        c2 = [int(x) for x in c2]

    res = set()
    for c in [c1, c2]:
        for diff_1 in range(-2, 3):
            for diff_2 in range(-2, 3):
                for diff_3 in range(-2, 3):
                    d1 = c[0] + diff_1
                    d2 = c[1] + diff_2
                    d3 = c[2] + diff_3
                    d1 = format(d1, N)
                    d2 = format(d2, N)
                    d3 = format(d3, N)

                    res.add((d1, d2, d3))

    with open("combo.out", "w") as f:
        f.write(f"{len(res)}\n")


if __name__ == "__main__":
    main()
