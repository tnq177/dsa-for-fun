def main():
    def count_neighbors(r, c, inpath):
        count = 0
        for dr, dc in (
            (-2, -1),
            (-2, 1),
            (-1, -2),
            (-1, 2),
            (1, -2),
            (1, 2),
            (2, -1),
            (2, 1),
        ):
            nr, nc = r + dr, c + dc
            if 0 <= nr < 8 and 0 <= nc < 8 and (nr, nc) not in inpath:
                count += 1
        return count

    def dfs(path, inpath):
        if len(path) == 64:
            return

        r, c = path[-1]
        next_moves = []
        for dr, dc in (
            (-2, -1),
            (-2, 1),
            (-1, -2),
            (-1, 2),
            (1, -2),
            (1, 2),
            (2, -1),
            (2, 1),
        ):
            nr, nc = r + dr, c + dc
            if 0 <= nr < 8 and 0 <= nc < 8 and (nr, nc) not in inpath:
                ncount = count_neighbors(nr, nc, inpath)
                next_moves.append((ncount, nr, nc))
        next_moves.sort(key=lambda x: x[0])

        for _, nr, nc in next_moves:
            path.append((nr, nc))
            inpath.add((nr, nc))
            dfs(path, inpath)
            if len(path) == 64:
                return
            inpath.remove((nr, nc))
            path.pop()

    c, r = [int(x) for x in input().strip().split()]
    path = [(r - 1, c - 1)]
    inpath = set([(r - 1, c - 1)])
    dfs(path, inpath)
    res = [[0] * 8 for _ in range(8)]
    for i, (r, c) in enumerate(path):
        res[r][c] = i + 1
    for row in res:
        print(*row)


main()
