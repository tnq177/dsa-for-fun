"""
ID: toannq12
LANG: PYTHON3
TASK: fence6
"""
from collections import defaultdict


def main():
    node_idx = -1
    edges = defaultdict(dict)
    tuple2node = {}

    with open("fence6.in", "r") as f:
        N = int(f.readline().strip())
        for _ in range(N):
            s, l, n1, n2 = [int(x) for x in f.readline().strip().split()]
            left = [int(x) for x in f.readline().strip().split()]
            right = [int(x) for x in f.readline().strip().split()]

            left.append(s)
            right.append(s)
            left.sort()
            right.sort()
            left = tuple(left)
            right = tuple(right)

            if left not in tuple2node:
                node_idx += 1
                tuple2node[left] = node_left = node_idx
            else:
                node_left = tuple2node[left]

            if right not in tuple2node:
                node_idx += 1
                tuple2node[right] = node_right = node_idx
            else:
                node_right = tuple2node[right]

            # bridge them
            edges[node_left][node_right] = l
            edges[node_right][node_left] = l

    res = [float("inf")]
    visited = set()

    def dfs(path, cumsum, inpath):
        curr = path[-1]
        for nei in edges[curr]:
            if len(path) >= 2 and nei == path[-2]:
                continue
            if nei in inpath:
                # found a cycle
                cycle_len = cumsum[-1] - cumsum[inpath[nei]]
                cycle_len += edges[curr][nei]
                res[0] = min(res[0], cycle_len)
            else:
                visited.add(nei)
                path.append(nei)
                inpath[nei] = len(path) - 1
                cumsum.append(cumsum[-1] + edges[curr][nei])
                dfs(path, cumsum, inpath)
                cumsum.pop()
                del inpath[nei]
                path.pop()

    # find all cycles
    for i in range(node_idx + 1):
        if i in visited:
            continue
        visited.add(i)
        dfs([i], [0], {i: 0})

    with open("fence6.out", "w") as f:
        f.write(f"{res[0]}\n")


if __name__ == "__main__":
    main()
