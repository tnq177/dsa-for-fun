"""
ID: toannq12
LANG: PYTHON3
TASK: ride
"""

MOD = 47


def string2num(line):
    res = 1
    for c in line:
        num = ord(c) - ord("A") + 1
        res = (res * num) % MOD
    return res


def main():
    with open("ride.in", "r") as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]

    a = string2num(lines[0])
    b = string2num(lines[1])
    with open("ride.out", "w") as f:
        if a == b:
            f.write("GO\n")
        else:
            f.write("STAY\n")


if __name__ == "__main__":
    main()
