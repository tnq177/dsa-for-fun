"""
ID: toannq12
LANG: PYTHON3
TASK: zerosum
"""


def eval(path):
    res = 0
    i = 0
    while i < len(path):
        op = path[i]
        j = i + 1
        num = 0
        while j < len(path) and path[j] not in "+-":
            if path[j] != " ":
                num = num * 10 + int(path[j])
            j += 1
        res = res + num if op == "+" else res - num
        i = j
    return res


def main():
    with open("zerosum.in", "r") as f:
        N = int(f.readline().strip())

    seq = list(range(1, N + 1))
    res = []

    def f(i, path):
        if i == len(seq):
            tmp = "".join(path)
            if eval(tmp) == 0:
                res.append(tmp[1:])
            return

        for op in ["+", "-", " "]:
            path.append(op)
            path.append(str(seq[i]))
            f(i + 1, path)
            path.pop()
            path.pop()

    f(1, ["+1"])
    res.sort()
    with open("zerosum.out", "w") as f:
        f.write("\n".join(res) + "\n")


if __name__ == "__main__":
    main()
