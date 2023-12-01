"""
ID: toannq12
LANG: PYTHON3
TASK: fracdec
"""


def div(n, d):
    if n % d == 0:
        return str(n // d) + ".0"

    before = str(n // d)
    decimals = []
    repeat_i = None
    seen = {}
    n = (n % d) * 10
    while True:
        if n in seen:
            repeat_i = seen[n]
            break
        decimals.append(str(n // d))
        seen[n] = len(decimals) - 1
        n = (n % d) * 10

    res = (
        before
        + "."
        + "".join(decimals[:repeat_i])
        + "("
        + "".join(decimals[repeat_i:])
        + ")"
    )
    if res.endswith("(0)"):
        res = res[:-3]
    return res


def main():
    with open("fracdec.in", "r") as f:
        N, D = [int(x) for x in f.readline().strip().split()]

    res = div(N, D)
    with open("fracdec.out", "w") as f:
        i = 0
        while i < len(res):
            f.write(res[i : i + 76] + "\n")
            i += 76


if __name__ == "__main__":
    main()
