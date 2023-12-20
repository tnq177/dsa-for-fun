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
    RC = R * C
    MAX = 10**9
    q = deque([])
    clear = q.clear
    append = q.append
    popleft = q.popleft

    king_c = ord(data[2]) - ord("A")
    king_r = R - int(data[3])
    king = king_r * C + king_c

    knights = []
    for i in range(4, len(data), 2):
        c = ord(data[i]) - ord("A")
        r = R - int(data[i + 1])
        knights.append(r * C + c)

    if not knights:
        return 0

    king_shortest = [0] * RC
    for idx in range(RC):
        r, c = divmod(idx, C)
        abs_r = abs(r - king_r)
        abs_c = abs(c - king_c)
        king_shortest[idx] = min(
            abs_r + abs(abs_c - abs_r),
            abs_c + abs(abs_r - abs_c),
        )

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

    knight_neighbors = [[] for _ in range(RC)]
    for s, neighbors in enumerate(knight_neighbors):
        r, c = divmod(s, C)
        for dr, dc in KNIGHT_DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                neighbors.append(nr * C + nc)

    shortest = [[MAX] * RC for _ in range(RC)]
    shortest_0 = shortest[0]
    shortest_0[0] = 0
    clear()
    append((0, 0))
    while q:
        d, s = popleft()
        for new_s in knight_neighbors[s]:
            if shortest_0[new_s] > d + 1:
                shortest_0[new_s] = d + 1
                append((d + 1, new_s))
    # this is really clever, I didn't come up w it
    if R >= 2 and C >= 2 and shortest_0[C + 1] == 4:
        shortest_0[C + 1] = 2
    for i, shortest_i in enumerate(shortest):
        shortest_i[i] = 0
        for j in range(i + 1, RC):
            ir, ic = i // C, i % C
            jr, jc = j // C, j % C
            abs_r = abs(jr - ir)
            abs_c = abs(jc - ic)
            shortest_i[j] = shortest[j][i] = shortest_0[abs_r * C + abs_c]
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

    knight_shortest = [shortest[knight] for knight in knights]
    knight_total = [sum(i) for i in zip(*knight_shortest)]
    shortest_with_king = [[MAX] * RC for _ in range(RC)]
    for i, (with_king, no_king) in enumerate(zip(shortest_with_king, shortest)):
        with_king[i] = king_shortest[i]
        clear()
        append((king_shortest[i], i))
        while q:
            d, s = popleft()
            for new_s in knight_neighbors[s]:
                cand = min(no_king[new_s] + king_shortest[new_s], d + 1)
                if with_king[new_s] > cand:
                    with_king[new_s] = cand
                    append((d + 1, new_s))

    res = MAX
    for meet, (total_d, king_d) in enumerate(zip(knight_total, king_shortest)):
        res = min(res, total_d + king_d)
        for k, k_shortest in zip(knights, knight_shortest):
            dist = total_d - k_shortest[meet] + shortest_with_king[k][meet]
            res = min(res, dist)

    return res


if __name__ == "__main__":
    with open("camelot.out", "w") as f:
        f.write(f"{main()}\n")
