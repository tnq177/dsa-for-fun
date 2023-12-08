"""
ID: toannq12
LANG: PYTHON3
TASK: camelot
"""
from collections import deque


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

    q = deque([(0, king)])
    king_shortest = [float("inf")] * (R * C)
    king_shortest[king] = 0
    while q:
        d, s = q.popleft()
        r, c = s // C, s % C
        for dr, dc in KING_DIRS:
            nr, nc = r + dr, c + dc
            new_s = nr * C + nc
            if 0 <= nr < R and 0 <= nc < C and king_shortest[new_s] > d + 1:
                king_shortest[new_s] = d + 1
                q.append((d + 1, new_s))

    shortest = [[float("inf")] * (R * C) for _ in range(R * C)]
    shortest_with_king = [[float("inf")] * (R * C) for _ in range(R * C)]
    for i in range(R * C):
        q = deque([(0, i)])
        shortest[i][i] = 0
        shortest_with_king[i][i] = king_shortest[i]

        while q:
            d, s = q.popleft()
            r, c = s // C, s % C
            for dr, dc in KNIGHT_DIRS:
                nr, nc = r + dr, c + dc
                new_s = nr * C + nc
                if 0 <= nr < R and 0 <= nc < C:
                    if shortest[i][new_s] > d + 1:
                        shortest[i][new_s] = d + 1
                        q.append((d + 1, new_s))
                    if shortest_with_king[i][new_s] > d + 1 + king_shortest[new_s]:
                        shortest_with_king[i][new_s] = d + 1 + king_shortest[new_s]

        q = deque([(king_shortest[i], i)])
        while q:
            d, s = q.popleft()
            r, c = s // C, s % C
            for dr, dc in KNIGHT_DIRS:
                nr, nc = r + dr, c + dc
                new_s = nr * C + nc
                if 0 <= nr < R and 0 <= nc < C and shortest_with_king[i][new_s] > d + 1:
                    shortest_with_king[i][new_s] = d + 1
                    q.append((d + 1, new_s))

    knight_total = [0] * (R * C)
    for knight in knights:
        for i in range(R * C):
            knight_total[i] += shortest[knight][i]

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
