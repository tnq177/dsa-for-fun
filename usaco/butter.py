"""
ID: toannq12
LANG: PYTHON3
TASK: butter
"""
# the key is to start from cows instead of all nodes
# if djk for all nodes it's P * Plog(P)
# if cows, it's N * Plog(P)
# N < P
from heapq import heappop, heappush


def main():
    with open("butter.in", "r") as f:
        N, P, C = [int(x) for x in f.readline().strip().split()]
        cows = {}
        for _ in range(N):
            cow = int(f.readline())
            cows[cow - 1] = cows.get(cow - 1, 0) + 1
        edges = {p: [] for p in range(P)}
        for _ in range(C):
            a, b, d = [int(x) for x in f.readline().strip().split()]
            a -= 1
            b -= 1
            edges[a].append((b, d))
            edges[b].append((a, d))

    min_paths = [0] * P
    for cow in cows:
        num_cow = cows[cow]
        shortest = [float("inf")] * P
        shortest[cow] = 0
        h = [(0, cow)]
        while h:
            dist, node = heappop(h)
            if dist > shortest[node]:
                continue

            min_paths[node] += num_cow * dist

            for nei, nei_dist in edges[node]:
                new_dist = dist + nei_dist
                if new_dist < shortest[nei]:
                    shortest[nei] = new_dist
                    heappush(h, (new_dist, nei))

    with open("butter.out", "w") as f:
        f.write(f"{min(min_paths)}\n")


if __name__ == "__main__":
    main()
