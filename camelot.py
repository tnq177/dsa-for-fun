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
    q = deque([(0, 0)])
    shortest[0][0] = 0
    while q:
        d, s = q.popleft()
        r, c = s // C, s % C
        for dr, dc in KNIGHT_DIRS:
            nr, nc = r + dr, c + dc
            new_s = nr * C + nc
            if 0 <= nr < R and 0 <= nc < C and shortest[0][new_s] > d + 1:
                shortest[0][new_s] = d + 1
                q.append((d + 1, new_s))
    if R > 1:
        shortest[0][C + 1] = 2
    for i in range(R * C):
        ir, ic = i // C, i % C
        for j in range(i, R * C):
            jr, jc = j // C, j % C
            abs_r, abs_c = abs(jr - ir), abs(jc - ic)
            shortest[i][j] = shortest[j][i] = shortest[0][abs_r * C + abs_c]
    if R >= 2 and C >= 2:
        for corner_x, corner_y, to_x, to_y in [
            (0, 0, 1, 1),
            (0, C - 1, 1, C - 2),
            (R - 1, 0, R - 2, 1),
            (R - 1, C - 1, R - 2, C - 2),
        ]:
            i = corner_x * C + corner_y
            j = to_x * C + to_y
            shortest[i][j] = 4

    total_knight = [0] * (R * C)
    for meet in range(R * C):
        for knight in knights:
            total_knight[meet] += shortest[knight][meet]

    res = float("inf")
    for meet in range(R * C):
        res = min(res, total_knight[meet] + king_shortest[meet])
        for pick in range(R * C):
            for knight in knights:
                dist = (
                    total_knight[meet]
                    - shortest[knight][meet]
                    + shortest[knight][pick]
                    + shortest[pick][meet]
                    + king_shortest[pick]
                )
                res = min(res, dist)
    print(res)


if __name__ == "__main__":
    main()
