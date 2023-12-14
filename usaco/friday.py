"""
ID: toannq12
LANG: PYTHON3
TASK: friday
"""


def is_leap(yr):
    if yr % 400 == 0:
        return True
    elif yr % 100 == 0:
        return False
    elif yr % 4 == 0:
        return True
    else:
        return False


def num_days(m, y):
    if m == 2:
        return 28 if not is_leap(y) else 29
    elif m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30


def main():
    with open("friday.in", "r") as f:
        N = int(f.readlines()[0].strip())

    res = [0] * 7

    # Jan 13 1900 is a Saturday
    m = 1
    d = 13
    y = 1900
    idx = 0
    res[0] += 1

    while y < 1900 + N:
        elapsed = num_days(m, y)
        m += 1
        if m == 13:
            m = 1
            y += 1
        if y == 1900 + N:
            break
        idx = (idx + elapsed) % 7
        res[idx] += 1

    with open("friday.out", "w") as f:
        f.write(" ".join([str(x) for x in res]) + "\n")


if __name__ == "__main__":
    main()
