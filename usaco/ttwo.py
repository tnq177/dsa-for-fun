"""
ID: toannq12
LANG: PYTHON3
TASK: ttwo
"""


def update(r, c, d, dirs, obstacles):
    dr, dc = dirs[d]
    nr, nc = r + dr, c + dc
    if 0 <= nr < 10 and 0 <= nc < 10 and (nr, nc) not in obstacles:
        return nr, nc, d
    d = (d + 1) % 4
    return r, c, d


def simulate(state, dirs, obstacles):
    state = tuple(state)
    seen = set()
    seen.add(state)
    count = 0
    while True:
        cr, cc, cd, fr, fc, fd = state
        if (cr, cc) == (fr, fc):
            return count
        cr, cc, cd = update(cr, cc, cd, dirs, obstacles)
        fr, fc, fd = update(fr, fc, fd, dirs, obstacles)
        count += 1
        state = (cr, cc, cd, fr, fc, fd)
        if state in seen:
            return 0
        seen.add(state)


def main():
    dirs = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

    # cow_r, cow_c, cow_dir, farm_r, farm_c, farm_dir
    state = [0] * 6
    obstacles = set()
    with open("ttwo.in", "r") as f:
        for r in range(10):
            line = f.readline().strip()
            for c, ch in enumerate(line):
                if ch == "*":
                    obstacles.add((r, c))
                if ch == "C":
                    state[0] = r
                    state[1] = c
                if ch == "F":
                    state[3] = r
                    state[4] = c

    count = simulate(state, dirs, obstacles)
    with open("ttwo.out", "w") as f:
        f.write(f"{count}\n")


if __name__ == "__main__":
    main()
