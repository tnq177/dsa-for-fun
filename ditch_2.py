"""
ID: toannq12
LANG: PYTHON3
TASK: ditch
"""

# use edmonds-karp
from collections import defaultdict, Counter, deque


def main():
    capacity = defaultdict(Counter)
    with open("ditch.in", "r") as f:
        N, M = [int(x) for x in f.readline().strip().split()]
        for _ in range(N):
            S, E, C = [int(x) for x in f.readline().strip().split()]
            capacity[S - 1][E - 1] += C

    SRC, TGT = 0, M - 1

    def bfs(parent):
        parent[SRC] = None
        q = deque([(float("inf"), SRC)])
        while q:
            flow, node = q.popleft()
            for next_node in capacity[node]:
                if parent[next_node] is None and capacity[node][next_node] > 0:
                    parent[next_node] = node
                    new_flow = min(flow, capacity[node][next_node])
                    if next_node == TGT:
                        return new_flow
                    q.append((new_flow, next_node))

        return 0

    res = 0
    while True:
        parent = [None] * M
        new_flow = bfs(parent)
        if not new_flow:
            break
        res += new_flow
        curr = TGT
        while curr != SRC:
            prev = parent[curr]
            capacity[prev][curr] -= new_flow
            capacity[curr][prev] += new_flow
            curr = prev

    with open("ditch.out", "w") as f:
        f.write(f"{res}\n")


if __name__ == "__main__":
    main()
