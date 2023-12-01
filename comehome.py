"""
ID: toannq12
LANG: PYTHON3
TASK: comehome
"""
from collections import defaultdict
import heapq as H


def main():
    paths = defaultdict(dict)
    pastures = set()
    with open("comehome.in", "r") as f:
        P = int(f.readline().strip())
        for _ in range(P):
            a, b, d = [x for x in f.readline().strip().split()]
            d = int(d)
            if b in paths[a]:
                paths[a][b] = min(paths[a][b], d)
            else:
                paths[a][b] = d
            if a in paths[b]:
                paths[b][a] = min(paths[b][a], d)
            else:
                paths[b][a] = d
            pastures.add(a)
            pastures.add(b)

    dist = {p: float("inf") for p in pastures}
    dist["Z"] = 0
    h = []
    H.heappush(h, (0, "Z"))
    visited = set()
    while len(visited) < len(pastures):
        d, p = H.heappop(h)
        if d > dist[p]:
            continue
        visited.add(p)
        for next_p in paths[p]:
            next_d = d + paths[p][next_p]
            if next_d < dist[next_p]:
                H.heappush(h, (next_d, next_p))
                dist[next_p] = next_d

    best_p = None
    best_d = float("inf")
    for p in pastures:
        if p.isupper() and p != "Z" and dist[p] < best_d:
            best_d = dist[p]
            best_p = p

    with open("comehome.out", "w") as f:
        f.write(f"{best_p} {best_d}\n")


if __name__ == "__main__":
    main()
