"""
ID: toannq12
LANG: PYTHON3
TASK: ditch
"""

from collections import defaultdict, Counter


def main():
    capacity = defaultdict(Counter)
    with open("ditch.in", "r") as f:
        N, M = [int(x) for x in f.readline().strip().split()]
        for _ in range(N):
            S, E, C = [int(x) for x in f.readline().strip().split()]
            capacity[S - 1][E - 1] += C

    res = 0
    while True:
        # find the maximum path from source to sink
        prev_node = [None] * M
        flow = [0] * M
        visited = [False] * M

        flow[0] = float("inf")
        while True:
            max_flow = 0
            max_loc = None
            for i in range(M):
                if flow[i] > max_flow and not visited[i]:
                    max_flow = flow[i]
                    max_loc = i
            if max_loc is None or max_loc == M - 1:
                break
            visited[max_loc] = True
            for nei in capacity[max_loc]:
                if flow[nei] < min(max_flow, capacity[max_loc][nei]):
                    flow[nei] = min(max_flow, capacity[max_loc][nei])
                    prev_node[nei] = max_loc

        if max_loc is None:
            break
        res += flow[M - 1]

        # update capacity
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
