"""
ID: toannq12
LANG: PYTHON3
TASK: concom
"""
from collections import defaultdict, Counter


def main():
    owns = defaultdict(set)
    percent = defaultdict(Counter)
    companies = set()
    with open("concom.in", "r") as f:
        N = int(f.readline().strip())
        for _ in range(N):
            a, b, p = [int(x) for x in f.readline().strip().split()]
            companies.add(a)
            companies.add(b)
            percent[a][b] += p
            owns[a].add(a)
            owns[b].add(b)
            if p > 50:
                owns[a].add(b)

    companies = list(companies)

    # minimum case we add 1 new each time
    # we only need to do it len(companies) times
    for _ in range(len(companies)):
        has_new = False
        for a in companies:
            accum = Counter()
            a_owns = list(owns[a])
            for c in a_owns:
                for b in percent[c]:
                    accum[b] += percent[c][b]
            for b in companies:
                if accum[b] > 50:
                    owns[a].add(b)
                    has_new = True
        if not has_new:
            break

    companies.sort()
    with open("concom.out", "w") as f:
        for a in companies:
            a_owns = list(owns[a])
            a_owns.sort()
            for b in a_owns:
                if b != a:
                    f.write(f"{a} {b}\n")


if __name__ == "__main__":
    main()
