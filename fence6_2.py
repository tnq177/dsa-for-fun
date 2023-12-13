"""
ID: toannq12
LANG: PYTHON3
TASK: fence6
"""
from collections import defaultdict


def main():
    node_idx = -1
    edges = defaultdict(dict)
    tuple2node = {}

    with open("fence6.in", "r") as f:
        N = int(f.readline().strip())
        for _ in range(N):
            s, l, n1, n2 = [int(x) for x in f.readline().strip().split()]
            left = [int(x) for x in f.readline().strip().split()]
            right = [int(x) for x in f.readline().strip().split()]

            left.append(s)
            right.append(s)
            left.sort()
            right.sort()
            left = tuple(left)
            right = tuple(right)

            if left not in tuple2node:
                node_idx += 1
                tuple2node[left] = node_left = node_idx
            else:
                node_left = tuple2node[left]

            if right not in tuple2node:
                node_idx += 1
                tuple2node[right] = node_right = node_idx
            else:
                node_right = tuple2node[right]

            # bridge them
            edges[node_left][node_right] = l
            edges[node_right][node_left] = l

    # USACO's analysis' idea
    import heapq as H

    res = float("inf")
    seen = set()
    for src in range(node_idx + 1):
        neighbors = list(edges[src].keys())
        for nei in neighbors:
            _min, _max = min(src, nei), max(src, nei)
            if (_min, _max) in seen:
                continue
            seen.add((_min, _max))

            # delete this edge
            edge_weight = edges[src][nei]
            del edges[src][nei]

            shortest = [float("inf") for i in range(node_idx + 1)]
            visited = set()
            shortest[src] = 0
            h = [(0, src)]
            while h and len(visited) < len(shortest):
                dist, node = H.heappop(h)
                visited.add(node)
                for new_node in edges[node]:
                    new_dist = dist + edges[node][new_node]
                    if new_dist < shortest[new_node]:
                        shortest[new_node] = new_dist
                        H.heappush(h, (new_dist, new_node))

            cycle_len = edge_weight + shortest[nei]
            res = min(res, cycle_len)
            # put edge back
            edges[src][nei] = edge_weight

    with open("fence6.out", "w") as f:
        f.write(f"{res}\n")


if __name__ == "__main__":
    main()
