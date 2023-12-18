def main():
    n = int(input())
    bosses = input().strip().split()
    from collections import defaultdict

    graph = defaultdict(list)
    for i, boss in enumerate(bosses):
        boss = int(boss)
        graph[boss].append(i + 2)

    levels = {1: [1]}
    while True:
        level = levels[len(levels)]
        new_level = []
        for boss in level:
            new_level.extend(graph[boss])
        if new_level:
            levels[len(levels) + 1] = new_level
        else:
            break

    res = [0] * (n + 1)
    for i in range(len(levels), 0, -1):
        level = levels[i]
        for boss in level:
            total = len(graph[boss])
            for child in graph[boss]:
                total += res[child]
            res[boss] = total

    print(*res[1:])


main()
