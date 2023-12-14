"""
ID: toannq12
LANG: PYTHON3
TASK: spin
"""


def fopen():
    fin = open("spin.in", "r")
    fout = open("spin.out", "w")
    return fin, fout


def fclose(*fobjs):
    for f in fobjs:
        f.close()


def main():
    fin, fout = fopen()
    speeds = []
    wheels = []
    for i, line in enumerate(fin):
        tmp = [int(x) for x in line.strip().split()]
        speeds.append(tmp[0])
        wedges = []
        for j in range(2, len(tmp), 2):
            wedges.append((tmp[j], tmp[j + 1]))
            if wedges[-1][1] == 0:
                fout.write("none\n")
                fclose(fin, fout)
                return
        wheels.append(wedges)

    t = 0
    seen = set()
    while True:
        state = [0] * 5
        for wid in range(5):
            state[wid] = (wheels[wid][0][0] + speeds[wid] * t) % 360
        state = tuple(state)
        if state in seen:
            break
        seen.add(state)
        thru = [0] * 360
        for wid in range(5):
            for start, angle in wheels[wid]:
                start = (start + speeds[wid] * t) % 360
                for i in range(start, start + angle + 1):
                    thru[i % 360] += 1
                    if thru[i % 360] >= 5:
                        fout.write(f"{t}\n")
                        fclose(fin, fout)
                        return
        t += 1
    fout.write("none\n")
    fclose(fin, fout)


if __name__ == "__main__":
    main()
