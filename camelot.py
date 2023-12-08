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
    king_c = ord(data[2]) - ord("A")
    king_r = R - int(data[3])
    king = king_r * C + king_c

    knights = []
    for i in range(4, len(data), 2):
        c = ord(data[i]) - ord("A")
        r = R - int(data[i + 1])
        knights.append(r * C + c)

    king_dirs = [
        (-1, -1),
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    knight_dirs = [
        (-2, -1),
        (-2, 1),
        (-1, -2),
        (-1, 2),
        (1, -2),
        (1, 2),
        (2, -1),
        (2, 1),
    ]

    def shortest_path(start, is_king=False):
        dirs = king_dirs if is_king else knight_dirs
        cache = {i: float("inf") for i in range(R * C)}
        maps = {}

        cache[start] = 0
        h = [(0, start, None)]
        for _ in range(R * C):
            dist, node, parent = H.heappop(h)
            maps[node] = parent
            r = node // C
            c = node % C
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                next_node = nr * C + nc
                if 0 <= nr < R and 0 <= nc < C and cache[next_node] > dist + 1:
                    cache[next_node] = dist + 1
                    H.heappush(h, (dist + 1, next_node, node))

        return cache, maps

    king_dist = shortest_path(king, is_king=True)[0]
    all_dists = []
    all_maps = []
    for loc in range(R * C):
        cache, maps = shortest_path(loc, is_king=False)
        all_dists.append(cache)
        all_maps.append(maps)

    knight_dist = {}
    closest_knight = {}
    for loc in range(R * C):
        total = 0
        min_knight = min_dist = None
        for knight in knights:
            d = all_dists[knight][loc]
            total += d
            if min_dist is None or min_dist > d:
                min_dist = d
                min_knight = knight
        closest_knight[loc] = min_knight
        knight_dist[loc] = total


    res = float("inf")
    for loc in range(R * C):
        total_knight = knight_dist[loc]
        total_king = king_dist[loc]

        # king go by himself
        res = min(res, total_knight + total_king)

        # king try to get a ride
        if knights:
            for meet_loc in range(R * C):
                chosen_knight = closest_knight[meet_loc]
                meet_dist = total_knight - all_dists[chosen_knight][loc] + king_dist[meet_loc] + all_dists[chosen_knight][meet_loc] + all_dists[meet_loc][loc]
                res = min(res, meet_dist)

    with open("camelot.out", "w") as f:
        f.write(f"{res}\n")


if __name__ == "__main__":
    main()
