"""
ID: toannq12
LANG: PYTHON3
TASK: camelot
"""
from collections import defaultdict, deque


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

    KING_DIRS = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    KNIGHT_DIRS = [
        (-2, -1),
        (-2, 1),
        (-1, -2),
        (-1, 2),
        (1, -2),
        (1, 2),
        (2, -1),
        (2, 1),
    ]

    king_neighbors = defaultdict(list)
    knight_neighbors = defaultdict(list)

    for s in range(R * C):
        r, c = s // C, s % C
        for dr, dc in KING_DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                new_s = nr * C + nc
                king_neighbors[s].append(new_s)
        for dr, dc in KNIGHT_DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                new_s = nr * C + nc
                knight_neighbors[s].append(new_s)

    q = deque([(0, king)])
    king_shortest = [float("inf")] * (R * C)
    king_shortest[king] = 0
    while q:
        d, s = q.popleft()
        for new_s in king_neighbors[s]:
            if king_shortest[new_s] > d + 1:
                king_shortest[new_s] = d + 1
                q.append((d + 1, new_s))

    # shortest = [[float("inf")] * (R * C) for _ in range(R * C)]
    # for i in range(R * C):
    #     shortest[i][i] = 0
    #     q = deque([(0, i)])
    #     while q:
    #         d, s = q.popleft()
    #         for new_s in knight_neighbors[s]:
    #             if shortest[i][new_s] > d + 1:
    #                 shortest[i][new_s] = d + 1
    #                 q.append((d + 1, new_s))

    shortest = [[float("inf")] * (R * C) for _ in range(R * C)]
    shortest[0][0] = 0
    q = deque([(0, 0)])
    while q:
        d, s = q.popleft()
        for new_s in knight_neighbors[s]:
            if shortest[0][new_s] > d + 1:
                shortest[0][new_s] = d + 1
                q.append((d + 1, new_s))
    # this is really clever, I didn't come up w it
    if R >= 2 and C >= 2 and shortest[0][C + 1] == 4:
        shortest[0][C + 1] = 2
    for i in range(R * C):
        shortest[i][i] = 0
        for j in range(i + 1, R * C):
            ir, ic = i // C, i % C
            jr, jc = j // C, j % C
            abs_r = abs(jr - ir)
            abs_c = abs(jc - ic)
            shortest[i][j] = shortest[j][i] = shortest[0][abs_r * C + abs_c]
    if R >= 2 and C >= 2:
        for r, c, nr, nc in [
            (0, 0, 1, 1),
            (0, C - 1, 1, C - 2),
            (R - 1, 0, R - 2, 1),
            (R - 1, C - 1, R - 2, C - 2),
        ]:
            i = r * C + c
            j = nr * C + nc
            if shortest[i][j] == 2:
                shortest[i][j] = 4

    shortest_with_king = [[float("inf")] * (R * C) for _ in range(R * C)]
    knight_total = [0] * (R * C)
    for i in range(R * C):
        for knight in knights:
            knight_total[i] += shortest[knight][i]

        shortest_with_king[i][i] = king_shortest[i]
        q = deque([(king_shortest[i], i)])
        while q:
            d, s = q.popleft()
            for new_s in knight_neighbors[s]:
                cand = min(shortest[i][new_s] + king_shortest[new_s], d + 1)
                if shortest_with_king[i][new_s] > cand:
                    shortest_with_king[i][new_s] = cand
                    q.append((d + 1, new_s))

    res = float("inf")
    for meet in range(R * C):
        res = min(res, knight_total[meet] + king_shortest[meet])
        for knight in knights:
            dist = (
                shortest_with_king[knight][meet]
                + knight_total[meet]
                - shortest[knight][meet]
            )
            res = min(res, dist)

    with open("camelot.out", "w") as f:
        f.write(f"{res}\n")


if __name__ == "__main__":
    main()
