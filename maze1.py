"""
ID: toannq12
LANG: PYTHON3
TASK: maze1
"""
from collections import deque


def main():
    with open("maze1.in", "r") as f:
        cols, rows = [int(x) for x in f.readline().strip().split()]
        maze = []
        for _ in range(2 * rows + 2):
            maze.append(f.readline()[: 2 * cols + 1])
        maze = [line for line in maze if line]

    dist = [[float("inf")] * cols for _ in range(rows)]
    q = deque([])
    # find the exits
    maze_rows, maze_cols = len(maze), len(maze[0])
    for mc in range(maze_cols):
        if maze[0][mc] == " ":
            q.append((0, mc // 2, 0))
            dist[0][mc // 2] = 0
        if maze[-1][mc] == " ":
            q.append((rows - 1, mc // 2, 0))
            dist[rows - 1][mc // 2] = 0
    for mr in range(maze_rows):
        if maze[mr][0] == " ":
            q.append((mr // 2, 0, 0))
            dist[mr // 2][0] = 0
        if maze[mr][-1] == " ":
            q.append((mr // 2, cols - 1, 0))
            dist[mr // 2][cols - 1] = 0

    res = float("-inf")
    while q:
        r, c, d = q.popleft()
        if d > dist[r][c]:
            continue
        res = max(res, d)
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            m_r = r * 2 + 1
            m_c = c * 2 + 1
            m_nr = nr * 2 + 1
            m_nc = nc * 2 + 1
            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and maze[(m_r + m_nr) // 2][(m_c + m_nc) // 2] == " "
                and dist[nr][nc] > d + 1
            ):
                dist[nr][nc] = d + 1
                q.append((nr, nc, dist[nr][nc]))

    with open("maze1.out", "w") as f:
        f.write(f"{res + 1}\n")


if __name__ == "__main__":
    main()
