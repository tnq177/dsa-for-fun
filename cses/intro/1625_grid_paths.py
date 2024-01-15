def main():
    path = {}
    for i, c in enumerate(input().strip()):
        if c == "U":
            path[i] = (-1, 0)
        elif c == "D":
            path[i] = (1, 0)
        elif c == "L":
            path[i] = (0, -1)
        elif c == "R":
            path[i] = (0, 1)

    GRID_SIZE = 9
    seen = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]
    for i in range(GRID_SIZE):
        seen[0][i] = True
        seen[-1][i] = True
        seen[i][0] = True
        seen[i][-1] = True

    seen[1][1] = True

    res = [0]

    def check1(r, c):
        return (
            c > 2
            and not seen[r][c - 1]
            and seen[r][c - 2]
            and (seen[r - 1][c - 1] or seen[r + 1][c - 1]),
            r,
            c - 1,
        )

    def check2(r, c):
        return (
            c < 6
            and not seen[r][c + 1]
            and seen[r][c + 2]
            and (seen[r - 1][c + 1] or seen[r + 1][c + 1]),
            r,
            c + 1,
        )

    def check3(r, c):
        return (
            r > 2
            and not seen[r - 1][c]
            and seen[r - 2][c]
            and (seen[r - 1][c - 1] or seen[r - 1][c + 1]),
            r - 1,
            c,
        )

    def check4(r, c):
        return (
            r < 6
            and not seen[r + 1][c]
            and seen[r + 2][c]
            and (seen[r + 1][c - 1] or seen[r + 1][c + 1]),
            r + 1,
            c,
        )

    def search(path_id, r, c):
        if (
            seen[r + 1][c]
            and seen[r - 1][c]
            and not seen[r][c - 1]
            and not seen[r][c + 1]
        ):
            return
        if (
            seen[r][c - 1]
            and seen[r][c + 1]
            and not seen[r + 1][c]
            and not seen[r - 1][c]
        ):
            return
        if r == 7 and c == 1:
            if path_id == 48:
                res[0] += 1
            return

        if path_id in path:
            dr, dc = path[path_id]
            nr, nc = r + dr, c + dc
            if not seen[nr][nc]:
                seen[nr][nc] = True
                search(path_id + 1, nr, nc)
                seen[nr][nc] = False
        else:
            for act in (check1, check2, check3, check4):
                yes, nr, nc = act(r, c)
                if yes:
                    seen[nr][nc] = True
                    search(path_id + 1, nr, nc)
                    seen[nr][nc] = False
                    return
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if not seen[nr][nc]:
                    seen[nr][nc] = True
                    search(path_id + 1, nr, nc)
                    seen[nr][nc] = False

    search(0, 1, 1)
    print(res[0])


main()
