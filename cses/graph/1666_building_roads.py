from collections import defaultdict


def main():
    n, m = [int(x) for x in input().strip().split()]
    G = defaultdict(list)
    for _ in range(m):
        a, b = [int(x) for x in input().strip().split()]
        G[a].append(b)
        G[b].append(a)

    cluster = -1
    city2cluster = {i: -1 for i in range(1, n + 1)}
    for i in range(1, n + 1):
        if city2cluster[i] != -1:
            continue

        cluster += 1
        city2cluster[i] = cluster
        stack = [i]
        while stack:
            city = stack.pop()
            for neighbor in G[city]:
                if city2cluster[neighbor] == -1:
                    city2cluster[neighbor] = cluster
                    stack.append(neighbor)

    print(cluster)

    cities = [-1] * (cluster + 1)
    for i in range(1, n + 1):
        cities[city2cluster[i]] = i

    for i in range(1, cluster + 1):
        print(f"{cities[0]} {cities[i]}")


main()
