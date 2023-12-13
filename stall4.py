"""
ID: toannq12
LANG: PYTHON3
TASK: stall4
"""

from collections import defaultdict, Counter, deque


def main():
    SRC = "src"
    SINK = "sink"
    cows = set()
    stalls = set()
    graph = defaultdict(Counter)
    with open("stall4.in", "r") as f:
        N, M = [int(x) for x in f.readline().strip().split()]
        for i in range(N):
            cow = f"cow-{i}"
            cows.add(cow)
            tmp = [int(x) for x in f.readline().strip().split()]
            for num in tmp[1:]:
                stall = f"stall-{num}"
                stalls.add(stall)
                graph[cow][stall] = 1

    for cow in cows:
        graph[SRC][cow] = 1
    for stall in stalls:
        graph[stall][SINK] = 1

    def bfs(parent):
        parent[SRC] = None
        q = deque([(float("inf"), SRC)])
        while q:
            flow, node = q.popleft()
            for next_node in graph[node]:
                if graph[node][next_node] > 0 and next_node not in parent:
                    parent[next_node] = node
                    new_flow = min(flow, graph[node][next_node])
                    if next_node == SINK:
                        return new_flow
                    q.append((new_flow, next_node))
        return 0

    while True:
        parent = {}
        new_flow = bfs(parent)
        if not new_flow:
            break

        curr = SINK
        while curr != SRC:
            prev = parent[curr]
            graph[prev][curr] -= 1
            graph[curr][prev] += 1
            curr = prev

    res = 0
    for cow in cows:
        for stall in graph[cow]:
            if graph[cow][stall] == 0:
                res += 1

    with open("stall4.out", "w") as f:
        f.write(f"{res}\n")


if __name__ == "__main__":
    main()
