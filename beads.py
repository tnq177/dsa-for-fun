"""
ID: toannq12
LANG: PYTHON3
TASK: beads
"""


def count_continuous(beads):
    """
    keep continuous count of red/blue
    if it's a white, it can be either red/blue so increase both
    otherwise increase one and reset the other
    """
    red = blue = 0
    cs = []
    for b in beads:
        if b == "w":
            red += 1
            blue += 1
        elif b == "r":
            red += 1
            blue = 0
        else:
            blue += 1
            red = 0
        cs.append(max(red, blue))
    return cs


def main():
    with open("beads.in", "r") as f:
        _ = int(f.readline().strip())
        beads = f.readline().strip()

    """
    because we split in the middle,
    we'll need to count from the other end too.
    instead, we just concat 2 copies of the beads and count
    if the result is larger than original beads' length, it means
    the whole beads could be painted 1 color
    """
    beads = beads + beads
    l2r = count_continuous(beads)
    r2l = count_continuous(beads[::-1])[::-1]
    res = 0
    for i in range(len(beads) - 1):
        res = max(res, l2r[i] + r2l[i + 1])
    res = min(res, len(beads) // 2)

    with open("beads.out", "w") as f:
        f.write(f"{res}\n")


if __name__ == "__main__":
    main()
