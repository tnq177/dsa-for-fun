import sys
from heapq import heappop, heappush

MAX = 10**16
inp = sys.stdin.readline


def map_input():
    return map(int, inp().split())


def main():
    n, m, q = map_input()
    shortest = [[0 if i == j else MAX for i in range(n + 1)] for j in range(n + 1)]
    G = [{} for _ in range(n + 1)]
    for _ in range(m):
        a, b, w = map_input()
        shortest[a][b] = shortest[b][a] = min(shortest[a][b], w)
        G[a][b] = G[b][a] = min(G[a].get(b, MAX), w)

    for i, tmp in enumerate(shortest):
        if i == 0:
            continue
        h = [(0, i)]
        for _ in range(n):
            if not h:
                break
            dist, node = heappop(h)
            for next_node in G[node]:
                if tmp[next_node] > dist + G[node][next_node]:
                    tmp[next_node] = dist + G[node][next_node]
                    heappush(h, (tmp[next_node], next_node))

    for c, dc in enumerate(shortest):
        for a, da in enumerate(shortest):
            for b in range(1, n + 1):
                if da[b] > da[c] + dc[b]:
                    da[b] = da[c] + dc[b]

    for _ in range(q):
        a, b = map_input()
        print(shortest[a][b] if shortest[a][b] != MAX else -1)


if __name__ == "__main__":
    main()
