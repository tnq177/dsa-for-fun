"""
ID: toannq12
LANG: PYTHON3
TASK: cowtour
"""
from collections import defaultdict


def calc_dist(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def main():
    with open("cowtour.in", "r") as f:
        N = int(f.readline().strip())
        pastures = []
        for _ in range(N):
            xy = tuple(int(z) for z in f.readline().strip().split())
            pastures.append(xy)
        adj = defaultdict(list)
        for i in range(N):
            line = f.readline().strip()
            for j, c in enumerate(line):
                if c == "1":
                    adj[i].append(j)

    # find components
    pasture2component = {}
    num_components = -1
    for pasture_idx in range(N):
        if pasture_idx in pasture2component:
            continue

        num_components += 1
        pasture2component[pasture_idx] = num_components
        stack = [pasture_idx]
        while stack:
            i = stack.pop()
            for j in adj[i]:
                if j not in pasture2component:
                    pasture2component[j] = num_components
                    stack.append(j)

    num_components += 1
    component2pastures = defaultdict(list)
    for p, c in pasture2component.items():
        component2pastures[c].append(p)

    # dist between every pair
    dist = [[float("inf")] * N for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0
        for j in adj[i]:
            dist[i][j] = calc_dist(*pastures[i], *pastures[j])

    # calculate shortest distance btw pairs within each components
    for component_idx in range(num_components):
        p_ids = list(component2pastures[component_idx])
        for k in p_ids:
            for i in p_ids:
                for j in p_ids:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

    # calculate the farthest j from i for i, j in the same component
    comp_max_dist = {}
    diameter = {}
    for component_idx in range(num_components):
        diameter[component_idx] = 0
        p_ids = list(component2pastures[component_idx])
        for i in p_ids:
            comp_max_dist[i] = max([dist[i][j] for j in p_ids])
            diameter[component_idx] = max(diameter[component_idx], comp_max_dist[i])

    # find best pair of components
    res = float("inf")
    for i in range(N - 1):
        for j in range(i + 1, N):
            pi = pasture2component[i]
            pj = pasture2component[j]
            if pi == pj:
                continue

            d = (
                calc_dist(*pastures[i], *pastures[j])
                + comp_max_dist[i]
                + comp_max_dist[j]
            )
            d = max(d, diameter[pi])
            d = max(d, diameter[pj])
            res = min(d, res)

    with open("cowtour.out", "w") as f:
        f.write(f"{res:.6f}\n")


if __name__ == "__main__":
    main()
