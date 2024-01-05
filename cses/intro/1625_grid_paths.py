def main():
    UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
    MOVE = {
        UP: lambda rc: (rc[0] - 1, rc[1]),
        RIGHT: lambda rc: (rc[0], rc[1] + 1),
        DOWN: lambda rc: (rc[0] + 1, rc[1]),
        LEFT: lambda rc: (rc[0], rc[1] - 1),
    }

    path = [-1] * 48
    for i, c in enumerate(input().strip()):
        if c == "U":
            path[i] = UP
        elif c == "D":
            path[i] = DOWN
        elif c == "L":
            path[i] = LEFT
        elif c == "R":
            path[i] = RIGHT

    seen = [False] * 49
    seen[0] = True
    res = [0]

    def search(path_id, grid_id, prev_grid_id):
        if grid_id == 42:
            # print('-----')
            # print(*path[path_id:])
            # for i in range(0, 49, 7):
            #     print(*[1 if x else 0 for x in seen[i:i+7]])
            return 1 if path_id == 48 else 0

        r, c = divmod(grid_id, 7)
        if path[path_id] != -1:
            nr, nc = MOVE[path[path_id]]((r, c))
            new_idx = nr * 7 + nc
            if 0 <= nr < 7 and 0 <= nc < 7 and not seen[new_idx]:
                seen[new_idx] = True
                total = search(path_id + 1, new_idx, grid_id)
                seen[new_idx] = False
            else:
                total = 0
            return total
        else:
            can_go = []
            total = 0
            for direction in range(4):
                nr, nc = MOVE[direction]((r, c))
                new_idx = nr * 7 + nc
                if new_idx == prev_grid_id:
                    continue
                if 0 <= nr < 7 and 0 <= nc < 7 and not seen[new_idx]:
                    can_go.append(new_idx)
                else:
                    left, right = (direction - 1) % 4, (direction + 1) % 4
                    left_nr, left_nc = MOVE[left]((r, c))
                    left_idx = left_nr * 7 + left_nc
                    right_nr, right_nc = MOVE[right]((r, c))
                    right_idx = right_nr * 7 + right_nc
                    if (
                        0 <= left_nr < 7
                        and 0 <= left_nc < 7
                        and not seen[left_idx]
                        and 0 <= right_nr < 7
                        and 0 <= right_nc < 7
                        and not seen[right_idx]
                    ):
                        can_go = []
                        break
            if not can_go:
                return total
            for new_idx in can_go:
                seen[new_idx] = True
                total += search(path_id + 1, new_idx, grid_id)
                seen[new_idx] = False

        return total

    res = 0
    if path[0] == -1 or path[0] == RIGHT:
        org = path[0]
        path[0] = RIGHT
        res += search(0, 0, -1)
        path[0] = org

    ids = [0, -1, -2, -3, -4]
    legit = all(path[i] in {DOWN, -1} for i in ids)
    legit = legit and path[1] in {RIGHT, -1} and path[-5] in {LEFT, -1}

    for down_ids, side_ids in [
        ((0, -1, -2, -3, -4), (1, -5)),
        ((0, 1, -1, -2, -3), (2, -4)),
    ]:
        legit = all(path[i] in {DOWN, -1} for i in down_ids)
        legit = (
            legit
            and path[side_ids[0]] in {RIGHT, -1}
            and path[side_ids[1]] in {LEFT, -1}
        )
        if not legit:
            continue
        down_orgs = [path[i] for i in down_ids]
        side_orgs = [path[i] for i in side_ids]
        for i in side_ids:
            path[i] = DOWN
        path[side_ids[0]] = RIGHT
        path[side_ids[1]] = LEFT
        res += 2 * search(0, 0, -1)
        for side_id, side_org in zip(side_ids, side_orgs):
            path[side_id] = side_org
        for down_id, down_org in zip(down_ids, down_orgs):
            path[down_id] = down_org

    print(res)


main()
