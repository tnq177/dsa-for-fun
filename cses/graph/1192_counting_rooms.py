def main():
    rows, cols = [int(x) for x in input().strip().split()]
    floor = [list(input().strip()) for _ in range(rows)]

    count = 0
    for r in range(rows):
        for c in range(cols):
            if floor[r][c] == "#":
                continue
            floor[r][c] = "#"
            count += 1
            stack = [(r, c)]
            while stack:
                cr, cc = stack.pop()
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < rows and 0 <= nc < cols and floor[nr][nc] == ".":
                        floor[nr][nc] = "#"
                        stack.append((nr, nc))

    print(count)


main()
