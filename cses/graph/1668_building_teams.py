from collections import defaultdict


def main():
    n, m = [int(x) for x in input().strip().split()]
    G = defaultdict(list)
    for _ in range(m):
        a, b = [int(x) for x in input().strip().split()]
        G[a].append(b)
        G[b].append(a)

    team = {}
    for i in range(1, n + 1):
        if i in team:
            continue

        color = 0
        team[i] = color
        level = [i]
        while level:
            color = 1 - color
            new_level = []
            while level:
                node = level.pop()
                for neighbor in G[node]:
                    if neighbor in team and team[neighbor] != color:
                        print("IMPOSSIBLE")
                        return
                    if neighbor not in team:
                        team[neighbor] = color
                        new_level.append(neighbor)
            level = new_level

    res = [team[i] + 1 for i in range(1, n + 1)]
    print(*res)

main()
