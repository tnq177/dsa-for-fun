"""
ID: toannq12
LANG: PYTHON3
TASK: ratios
"""


def close(*fobjs):
    for f in fobjs:
        f.close()


def main():
    fin = open("ratios.in", "r")
    fout = open("ratios.out", "w")
    tmp = [[int(x) for x in line.strip().split()] for line in fin]
    goal = tuple(tmp[0])
    m0, m1, m2 = [tuple(x) for x in tmp[1:]]

    if goal == (0, 0, 0):
        fout.write("0 0 0 0\n")
        close(fin, fout)
        return

    nonzero_idx = [i for i in range(3) if goal[i] != 0][0]
    idx1 = (nonzero_idx + 1) % 3
    idx2 = (nonzero_idx - 1) % 3
    mix = [0] * 3

    # the key here is to remove all overheads such as separating this code block below
    # into another function...
    for i0 in range(100):
        for i1 in range(100):
            for i2 in range(100):
                mix[0] = m0[0] * i0 + m1[0] * i1 + m2[0] * i2
                mix[1] = m0[1] * i0 + m1[1] * i1 + m2[1] * i2
                mix[2] = m0[2] * i0 + m1[2] * i1 + m2[2] * i2
                if mix[nonzero_idx] != 0 and mix[nonzero_idx] % goal[nonzero_idx] == 0:
                    multiple = mix[nonzero_idx] // goal[nonzero_idx]
                    if (
                        mix[idx1] == goal[idx1] * multiple
                        and mix[idx2] == goal[idx2] * multiple
                    ):
                        fout.write(f"{i0} {i1} {i2} {multiple}\n")
                        close(fin, fout)
                        return

    fout.write("NONE\n")
    close(fin, fout)


if __name__ == "__main__":
    main()
