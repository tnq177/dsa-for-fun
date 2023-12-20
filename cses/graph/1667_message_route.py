from collections import defaultdict, deque


def main():
    n, m = [int(x) for x in input().strip().split()]
    G = defaultdict(list)
    for _ in range(m):
        a, b = [int(x) for x in input().strip().split()]
        G[a].append(b)
        G[b].append(a)

    q = deque([(1, 1)])
    bp = {1: None}
    while q:
        node, dist = q.popleft()
        if node == n:
            print(dist)
            curr = node
            path = []
            while curr is not None:
                path.append(curr)
                curr = bp[curr]
            print(*path[::-1])
            return
        for next_node in G[node]:
            if next_node not in bp:
                bp[next_node] = node
                q.append((next_node, dist + 1))

    print("IMPOSSIBLE")


main()
