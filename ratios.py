"""
ID: toannq12
LANG: PYTHON3
TASK: ratios
"""


def calc_mix(mixes, ratios):
    x = mixes[0][0] * ratios[0] + mixes[1][0] * ratios[1] + mixes[2][0] * ratios[2]
    y = mixes[0][1] * ratios[0] + mixes[1][1] * ratios[1] + mixes[2][1] * ratios[2]
    z = mixes[0][2] * ratios[0] + mixes[1][2] * ratios[1] + mixes[2][2] * ratios[2]
    return (x, y, z)


def calc_valid_goals(mixes, goal):
    MAX = float("inf")
    for i in range(3):
        if goal[i] == 0:
            continue
        max_sum = mixes[0][i] * 99 + mixes[1][i] * 99 + mixes[2][i] * 99
        MAX = min(MAX, max_sum // goal[i])

    valid = {}
    for i in range(1, MAX + 1):
        x, y, z = goal[0] * i, goal[1] * i, goal[2] * i
        valid[(x, y, z)] = i
    return valid


def find(mixes, goal):
    if goal == (0, 0, 0):
        return (0, 0, 0), 0

    valid = calc_valid_goals(mixes, goal)
    for i0 in range(100):
        for i1 in range(100):
            for i2 in range(100):
                mix = calc_mix(mixes, (i0, i1, i2))
                if mix in valid:
                    return (i0, i1, i2), valid[mix]

    return None, None


def main():
    with open("ratios.in", "r") as f:
        tmp = [[int(x) for x in line.strip().split()] for line in f]
        goal = tuple(tmp[0])
        mixes = [tuple(x) for x in tmp[1:]]

    ratio, multiple = find(mixes, goal)
    with open("ratios.out", "w") as f:
        if ratio is None:
            f.write("NONE\n")
        else:
            ratio = list(ratio)
            ratio.append(multiple)
            ratio = " ".join([str(x) for x in ratio])
            f.write(f"{ratio}\n")


if __name__ == "__main__":
    main()
