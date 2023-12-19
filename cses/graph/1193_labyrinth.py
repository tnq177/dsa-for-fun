"""
inspired by https://codeforces.com/blog/entry/94548#comment-1094940
I've seen this before with some other USACO problems. Queue could be
slow with tuples or list, single numbers are better. For this reason,
we convert (r, c) to (r * C + c). The tricky part is finding the right
neighbors. If idx == C - 1 for example, the right neighbor doesn't exist.
If we simply go idx + 1, it actually goes to the first element in the
next row.
"""


def main():
    rows, cols = [int(x) for x in input().strip().split()]
    maze = [input() for _ in range(rows)]
    distance = [-2 if c == "#" else -1 for row in maze for c in row]

    level = []
    bp = {}
    bIdx = None
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == "A":
                idx = r * cols + c
                level.append(idx)
                distance[idx] = 0
                bp[idx] = None
            if maze[r][c] == "B":
                bIdx = r * cols + c

    dist = 0
    while level:
        dist += 1
        new_level = []
        while level:
            idx = level.pop()
            r, c = divmod(idx, cols)
            # left
            new_idx = idx - 1
            if c - 1 >= 0 and distance[new_idx] == -1:
                distance[new_idx] = dist
                bp[new_idx] = idx
                new_level.append(new_idx)
            # right
            new_idx = idx + 1
            if c + 1 < cols and distance[new_idx] == -1:
                distance[new_idx] = dist
                bp[new_idx] = idx
                new_level.append(new_idx)
            # up
            new_idx = idx - cols
            if r - 1 >= 0 and distance[new_idx] == -1:
                distance[new_idx] = dist
                bp[new_idx] = idx
                new_level.append(new_idx)
            # down
            new_idx = idx + cols
            if r + 1 < rows and distance[new_idx] == -1:
                distance[new_idx] = dist
                bp[new_idx] = idx
                new_level.append(new_idx)

            if distance[bIdx] != -1:
                level.clear()
                break

        if distance[bIdx] != -1:
            break
        level = new_level

    if distance[bIdx] == -1:
        print("NO")
        return

    path = []
    curr = bIdx
    while True:
        prev = bp[curr]
        if prev is None:
            break
        if curr == prev - cols:
            path.append("U")
        elif curr == prev + cols:
            path.append("D")
        elif curr == prev - 1:
            path.append("L")
        else:
            path.append("R")
        curr = prev

    print("YES")
    print(distance[bIdx])
    print("".join(path[::-1]))


main()
