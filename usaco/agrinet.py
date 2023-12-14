"""
ID: toannq12
LANG: PYTHON3
TASK: agrinet
"""


def main():
    with open("agrinet.in", "r") as f:
        tmp = []
        for line in f:
            tmp.extend(line.strip().split())
        tmp = [int(x) for x in tmp]
        N = tmp[0]
        matrix = []
        for i in range(1, N * N + 1, N):
            matrix.append(tmp[i : i + N])

    res = 0
    dist = matrix[0][:]
    seen = set()
    while len(seen) < N:
        min_dist = float("inf")
        min_node = None
        for node in range(N):
            if node not in seen and dist[node] < min_dist:
                min_dist = dist[node]
                min_node = node
        dist[min_node] = min_dist
        print(min_node, min_dist)
        res += min_dist
        seen.add(min_node)

        # update dist
        for node in range(N):
            dist[node] = min(dist[node], matrix[min_node][node])

    with open("agrinet.out", "w") as f:
        f.write(f"{res}\n")


if __name__ == "__main__":
    main()
