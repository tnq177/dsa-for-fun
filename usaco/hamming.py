"""
ID: toannq12
LANG: PYTHON3
TASK: hamming
"""
from collections import defaultdict


def hamming(a, b):
    dist = 0
    while a or b:
        dist += 1 if (a % 2 != b % 2) else 0
        a //= 2
        b //= 2
    return dist


def main():
    with open("hamming.in", "r") as f:
        tmp = f.readline().strip().split()
        N, B, D = [int(x) for x in tmp]

    edges = defaultdict(list)
    for a in range(2**B):
        for b in range(2**B):
            if a != b and hamming(a, b) >= D:
                edges[a].append(b)

    res = [None]

    def dfs(path, inpath):
        if len(path) == N:
            res[0] = path[:]
            return

        for new_num in edges[path[-1]]:
            if new_num in inpath:
                continue
            if all(new_num in edges[num] for num in path):
                path.append(new_num)
                inpath.add(new_num)
                dfs(path, inpath)
                if res[0] is not None:
                    return
                path.pop()
                inpath.remove(new_num)

    for num in range(2**B):
        dfs([num], {num})
        if res[0] is not None:
            break

    res = res[0]
    res.sort()
    with open("hamming.out", "w") as f:
        while res:
            tmp = [str(x) for x in res[:10]]
            res = res[10:]
            f.write(" ".join(tmp) + "\n")


if __name__ == "__main__":
    main()
