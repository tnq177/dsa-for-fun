"""
ID: toannq12
LANG: PYTHON3
TASK: gift1
"""
from collections import defaultdict


def main():
    res = defaultdict(int)
    with open("gift1.in", "r") as f:
        NP = int(f.readline().strip())
        names = []
        for _ in range(NP):
            names.append(f.readline().strip())

        for _ in range(NP):
            name = f.readline().strip()
            money, count = f.readline().strip().split()
            money = int(money)
            count = int(count)

            if count > 0:
                res[name] += money % count - money
                for _ in range(count):
                    receiver = f.readline().strip()
                    res[receiver] += money // count
            else:
                res[name] -= money

    with open("gift1.out", "w") as f:
        for name in names:
            f.write(f"{name} {res[name]}\n")


if __name__ == "__main__":
    main()
