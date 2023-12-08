"""
ID: toannq12
LANG: PYTHON3
TASK: camelot
"""
import heapq as H


def main():
    with open("camelot.in", "r") as f:
        data = []
        for line in f:
            data.extend(line.strip().split())

    R, C = int(data[0]), int(data[1])
    MIN, MAX = 0, R * C - 1
    king_c = ord(data[2]) - ord("A")
    king_r = R - int(data[3])
    king = king_r * C + king_c

    knights = []
    for i in range(4, len(data), 2):
        c = ord(data[i]) - ord("A")
        r = R - int(data[i + 1])
        knights.append(r * C + c)

    king_dirs = [
        -C,
        -C - 1,
        -C + 1,
        1,
        C + 1,
        C,
        C - 1,
        -1,
    ]
    knight_dirs = [
        -2 * C - 1,
        -2 * C + 1,
        -C + 2,
        -C - 2,
        C + 2,
        C - 2,
        2 * C + 1,
        2 * C - 1,
    ]

    def shortest_path(start, is_king=False):
        dirs = king_dirs if is_king else knight_dirs
        cache = {i: float("inf") for i in range(MAX + 1)}
        maps = {}

        cache[start] = 0
        h = [(0, start, None)]
        for _ in range(MAX + 1):
            dist, node, parent = H.heappop(h)
            maps[node] = parent
            for dir in dirs:
                next_node = node + dir
                if MIN <= next_node <= MAX and cache[next_node] > dist + 1:
                    cache[next_node] = dist + 1
                    H.heappush(h, (dist + 1, next_node, node))

        return cache, maps

    king_dist = shortest_path(king, is_king=True)[0]
    knight_dists = []
    knight_maps = []
    for knight in knights:
        dist, maps = shortest_path(knight, is_king=False)
        knight_dists.append(dist)
        knight_maps.append(maps)

    res = float("inf")
    for loc in range(MAX + 1):
        dist = 0
        for knight_dist in knight_dists:
            dist += knight_dist[loc]

        # try to get on one of the knights
        all_knight_locs = set()
        for knight_map in knight_maps:
            curr = loc
            while curr is not None:
                all_knight_locs.add(curr)
                curr = knight_map[curr]
        dist += min([king_dist[_loc] for _loc in all_knight_locs])
        res = min(res, dist)
        if res == 9:
            print(loc)

    with open("camelot.out", "w") as f:
        f.write(f"{res}\n")


if __name__ == "__main__":
    main()
