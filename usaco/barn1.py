"""
ID: toannq12
LANG: PYTHON3
TASK: barn1
"""
from functools import lru_cache


def main():
    with open("barn1.in", "r") as f:
        MSC = f.readline().strip().split()
        M, _, C = [int(x) for x in MSC]
        stalls = []
        for _ in range(C):
            stalls.append(int(f.readline().strip()))
    stalls.sort()

    # initially we use 1 board to cover everything
    length = stalls[-1] - stalls[0] + 1
    board_used = 1

    # we can reduce the length of boards used by not covering the gaps
    # in which there are no cows
    gaps = []
    for i in range(1, len(stalls)):
        if stalls[i] > stalls[i - 1] + 1:
            gaps.append(stalls[i] - stalls[i - 1] - 1)
    gaps.sort()

    # we do it by not covering the largest->smallest gaps
    while board_used < M and gaps:
        length -= gaps.pop()
        board_used += 1

    with open("barn1.out", "w") as f:
        f.write(f"{length}\n")


if __name__ == "__main__":
    main()
