"""
Iterative version, even slower
"""
GRID_SIZE=9

path = []
seen = [[-1] * GRID_SIZE for _ in range(GRID_SIZE)]
for i in range(GRID_SIZE):
    seen[i][0] = seen[i][-1] = 4
    seen[0][i] = seen[-1][i] = 4

diff_map = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1)
}
path.append((1, 1))
seen[1][1] = 0
res = 0
while path:
    r, c = path[-1]
    if seen[r][c] == 4:
        seen[r][c] = -1
        path.pop()
        continue

    if seen[r + 1][c] == seen[r - 1][c] == -1 and seen[r][c - 1] != -1 and seen[r][c + 1] != -1:
        seen[r][c] = -1
        path.pop()
        continue

    if seen[r][c - 1] == seen[r][c + 1] == -1 and seen[r - 1][c] != -1 and seen[r + 1][c] != -1:
        seen[r][c] = -1
        path.pop()
        continue

    if r == 7 and c == 1:
        if len(path) == 49:
            res += 1
        seen[r][c] = -1
        path.pop()
        continue

    if c > 2 and seen[r][c - 1] == -1 and seen[r][c - 1] != -1 and (seen[r - 1][c - 1] != -1 or seen[r + 1][c - 1] != -1):
        seen[r][c] = 4
        seen[r][c - 1] = 0
        path.append((r, c - 1))
        continue
    if c < 6 and seen[r][c + 1] == -1 and seen[r][c + 2] != -1 and (seen[r - 1][c + 1] != -1 or seen[r + 1][c + 1] != -1):
        seen[r][c] = 4
        seen[r][c + 1] = 0
        path.append((r, c + 1))
        continue
    if r > 2 and seen[r - 1][c] == -1 and seen[r - 2][c] != -1 and (seen[r - 1][c - 1] != -1 or seen[r - 1][c + 1] != -1):
        seen[r][c] = 4
        seen[r - 1][c] = 0
        path.append((r - 1, c))
        continue
    if r < 6 and seen[r + 1][c] == -1 and seen[r + 2][c] != -1 and (seen[r + 1][c - 1] != -1 or seen[r + 1][c + 1] != -1):
        seen[r][c] = 4
        seen[r + 1][c] = 0
        path.append((r + 1, c))
        continue

    can_go = False
    nr = nr = None
    while True and seen[r][c] != 4:
        dr, dc = diff_map[seen[r][c]]
        seen[r][c] += 1
        nr, nc = r + dr, c + dc
        if 0 < nr < GRID_SIZE - 1 and 0 < nc < GRID_SIZE - 1 and seen[nr][nc] == -1:
            can_go = True
            break
    if not can_go:
        seen[r][c] = -1
        path.pop()
    else:
        seen[nr][nc] = 0
        path.append((nr, nc))

print(res)