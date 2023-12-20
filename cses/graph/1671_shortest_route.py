from collections import defaultdict
import heapq as H


def main():
    n, m = [int(x) for x in input().strip().split()]
    G = defaultdict(dict)
    for _ in range(m):
        a, b, w = [int(x) for x in input().strip().split()]
        if b not in G[a]:
            G[a][b] = w
        else:
            G[a][b] = min(G[a][b], w)

    shortest = [float("inf")] * (n + 1)
    shortest[1] = 0
    h = [(0, 1)]
    while h:
        distance, city = H.heappop(h)
        if distance > shortest[city]:
            continue
        for next_city in G[city]:
            duration = G[city][next_city]
            if shortest[next_city] > distance + duration:
                shortest[next_city] = distance + duration
                H.heappush(h, (distance + duration, next_city))

    print(*shortest[1:])


main()
