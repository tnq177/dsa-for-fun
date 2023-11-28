"""
ID: toannq12
LANG: PYTHON3
TASK: frac1
"""


class Fraction(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __lt__(self, other):
        return self.a * other.b < self.b * other.a


def main():
    with open("frac1.in", "r") as f:
        N = int(f.readline().strip())

    res = []

    def dfs(low, high):
        if low.b + high.b <= N:
            mid = Fraction(low.a + high.a, low.b + high.b)
            res.append(mid)
            dfs(low, mid)
            dfs(mid, high)

    res.append(Fraction(0, 1))
    res.append(Fraction(1, 1))
    dfs(res[0], res[1])
    res.sort()
    with open("frac1.out", "w") as f:
        for frac in res:
            f.write(f"{frac.a}/{frac.b}\n")


if __name__ == "__main__":
    main()
