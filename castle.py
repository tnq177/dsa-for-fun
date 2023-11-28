"""
ID: toannq12
LANG: PYTHON3
TASK: castle
"""


def calc_val2wall():
    res = {}
    for n in range(2):
        for e in range(2):
            for s in range(2):
                for w in range(2):
                    val = 2 if n else 0
                    val += 4 if e else 0
                    val += 8 if s else 0
                    val += 1 if w else 0
                    res[val] = [n, e, s, w]
    return res


def main():
    val2wall = calc_val2wall()

    with open("castle.in", "r") as f:
        tmp = f.readline().strip().split()
        cols, rows = [int(x) for x in tmp]
        castle = []
        for _ in range(rows):
            tmp = f.readline().strip().split()
            castle.append([int(x) for x in tmp])

    room_idxs = [[-1] * cols for _ in range(rows)]
    curr_idx = -1
    idx2area = {}
    for r in range(rows):
        for c in range(cols):
            if room_idxs[r][c] != -1:
                continue

            curr_idx += 1
            room_idxs[r][c] = curr_idx
            area = 0
            stack = [(r, c)]
            while stack:
                cr, cc = stack.pop()
                area += 1
                has_walls = val2wall[castle[cr][cc]]
                for i, (dr, dc) in enumerate([(-1, 0), (0, 1), (1, 0), (0, -1)]):
                    if not has_walls[i]:
                        nr, nc = cr + dr, cc + dc
                        if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and room_idxs[nr][nc] == -1
                        ):
                            room_idxs[nr][nc] = curr_idx
                            stack.append((nr, nc))
            idx2area[curr_idx] = area

    result = [f"{curr_idx + 1}"]
    result.append(f"{max(idx2area.values())}")
    max_area = 0
    max_r = max_c = -1
    max_wall = None
    directions = "NESW"
    for c in range(cols):
        for r in range(rows - 1, -1, -1):
            has_walls = val2wall[castle[r][c]]
            for i, (dr, dc) in enumerate([(-1, 0), (0, 1), (1, 0), (0, -1)]):
                if not has_walls[i]:
                    continue
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and room_idxs[nr][nc] != room_idxs[r][c]
                ):
                    area = idx2area[room_idxs[nr][nc]] + idx2area[room_idxs[r][c]]
                    if area > max_area:
                        max_area = area
                        max_r, max_c = r, c
                        max_wall = directions[i]
    result.append(f"{max_area}")
    result.append(f"{max_r + 1} {max_c + 1} {max_wall}")

    with open("castle.out", "w") as f:
        f.write("\n".join(result) + "\n")


if __name__ == "__main__":
    main()
