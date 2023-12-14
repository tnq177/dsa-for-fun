"""
ID: toannq12
LANG: PYTHON3
TASK: wormhole
"""
from collections import namedtuple, defaultdict


Point = namedtuple("Point", ["x", "y"])


def has_cycle(pairs, next_right):
    pairing = {}
    max_idx = 0
    for i, j in pairs:
        pairing[i] = j
        pairing[j] = i
        max_idx = max(max_idx, i)
        max_idx = max(max_idx, j)

    for i in range(max_idx + 1):
        curr = i
        seen = set()
        seen.add(curr)
        found_cycle = False
        while True:
            if curr not in next_right:
                break
            nxt = next_right[curr]
            nxt_nxt = pairing[nxt]
            if nxt_nxt in seen:
                found_cycle = True
                break
            seen.add(nxt_nxt)
            curr = nxt_nxt
        if found_cycle:
            return True

    return False


def pairing_iter(pairs, remains, res, points, next_right):
    if len(pairs) == len(points) // 2:
        for p1, p2 in pairs:
            if next_right.get(p1, -1) == p2 or next_right.get(p2, -1) == p1:
                res[0] += 1
                return
        if has_cycle(pairs, next_right):
            res[0] += 1
            return

    point_idxs = list(remains)
    for j in range(1, len(point_idxs)):
        p1 = point_idxs[0]
        p2 = point_idxs[j]
        pairs.append((p1, p2))
        remains.remove(p1)
        remains.remove(p2)
        pairing_iter(pairs, remains, res, points, next_right)
        remains.add(p1)
        remains.add(p2)
        pairs.pop()


def get_next_right(points):
    cache = defaultdict(list)
    for i, p in enumerate(points):
        cache[p.y].append(i)

    next_right = {}
    for y in cache:
        idxs = cache[y]
        idxs.sort(key=lambda i: points[i].x)
        for i in range(len(idxs) - 1):
            next_right[idxs[i]] = idxs[i + 1]

    return next_right


def main():
    with open("wormhole.in", "r") as f:
        N = int(f.readline().strip())
        points = []
        for _ in range(N):
            xy = f.readline().strip().split()
            xy = tuple([int(z) for z in xy])
            points.append(Point(xy[0], xy[1]))

    next_right = get_next_right(points)
    remains = set(range(len(points)))
    res = [0]
    pairing_iter([], remains, res, points, next_right)
    with open("wormhole.out", "w") as f:
        f.write(f"{res[0]}\n")


if __name__ == "__main__":
    main()
