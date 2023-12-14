"""
ID: toannq12
LANG: PYTHON3
TASK: ditch
"""

from collections import defaultdict, Counter
import heapq as H


def main():
    capacity = defaultdict(Counter)
    with open("ditch.in", "r") as f:
        N, M = [int(x) for x in f.readline().strip().split()]
        for _ in range(N):
            S, E, C = [int(x) for x in f.readline().strip().split()]
            capacity[S - 1][E - 1] += C

    res = 0
    while True:
        prev_node = [None] * M
        flow = [0] * M
        visited = [False] * M
        flow[0] = float("inf")
        h = [(float("-inf"), 0, None)]
        while h:
            max_flow, node, parent = H.heappop(h)
            if visited[node]:
                continue
            visited[node] = True
            prev_node[node] = parent
            max_flow = -max_flow
            if node == M - 1:
                # found sink
                break

            for nei in capacity[node]:
                if visited[nei]:
                    continue
                if flow[nei] < min(max_flow, capacity[node][nei]):
                    flow[nei] = min(max_flow, capacity[node][nei])
                    H.heappush(h, (-flow[nei], nei, node))

        if flow[M - 1] == 0:
            break
        res += flow[M - 1]
        curr = M - 1
        while curr != 0:
            next_curr = prev_node[curr]
            capacity[next_curr][curr] -= flow[M - 1]
            if capacity[next_curr][curr] == 0:
                del capacity[next_curr][curr]
            capacity[curr][next_curr] += flow[M - 1]
            curr = next_curr

    with open("ditch.out", "w") as f:
        f.write(f"{res}\n")


if __name__ == "__main__":
    main()
