"""
ID: toannq12
LANG: PYTHON3
TASK: fence9
"""


def main():
    with open("fence9.in", "r") as f:
        x0, y0, z0 = [int(x) for x in f.readline().strip().split()]

    count = 0
    for y in range(1, y0):
        y_left = y_right = y
        if x0 == 0:
            x_left = 1
        else:
            # (y_left - 0) / (x_left - 0) = y0/x0
            x_left = int(x0 * y_left / y0) + 1

        if x0 == z0:
            x_right = x0 - 1
        else:
            # (y_right - 0)/(x_right - z0) = (y - 0) / (x0 - z)
            x_right = int((x0 - z0) * y_right / y0 + z0)
            if ((x0 - z0) * y_right) % y0 == 0:
                x_right -= 1

        count += x_right - x_left + 1

    with open("fence9.out", "w") as f:
        f.write(f"{count}\n")


if __name__ == "__main__":
    main()
