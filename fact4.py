"""
ID: toannq12
LANG: PYTHON3
TASK: fact4
"""


def main():
    with open("fact4.in", "r") as f:
        N = int(f.readline().strip())

    count2 = count5 = 0
    for i in range(1, N + 1):
        while i % 2 == 0:
            i //= 2
            count2 += 1
        while i % 5 == 0:
            i //= 5
            count5 += 1

    remove2 = remove5 = min(count2, count5)
    res = 1
    for i in range(1, N + 1):
        while i % 2 == 0 and remove2:
            i //= 2
            remove2 -= 1
        while i % 5 == 0 and remove5:
            i //= 5
            remove5 -= 1
        res = (res * i) % 10

    with open("fact4.out", "w") as f:
        f.write(f"{res}\n")


if __name__ == "__main__":
    main()
