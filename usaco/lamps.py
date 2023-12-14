"""
ID: toannq12
LANG: PYTHON3
TASK: lamps
"""
from functools import lru_cache
from collections import deque


@lru_cache
def get_new_state(state, button):
    if button == 1:
        new_state = [flip(c) for c in state]
    elif button == 2:
        new_state = [c if (i + 1) % 2 == 0 else flip(c) for i, c in enumerate(state)]
    elif button == 3:
        new_state = [c if (i + 1) % 2 == 1 else flip(c) for i, c in enumerate(state)]
    else:
        new_state = [flip(c) if (i + 1) % 3 == 1 else c for i, c in enumerate(state)]
    return "".join(new_state)


def flip(c):
    return "1" if c == "0" else "0"


def valid(state, ons, offs):
    for i in ons:
        if state[i] == "0":
            return False
    for i in offs:
        if state[i] == "1":
            return False
    return True


def main():
    with open("lamps.in", "r") as f:
        N = int(f.readline().strip())
        C = int(f.readline().strip())
        ons = f.readline().strip().split()[:-1]
        ons = [int(x) - 1 for x in ons]
        offs = f.readline().strip().split()[:-1]
        offs = [int(x) - 1 for x in offs]

    q = ["1" * N]
    for _ in range(C):
        new_q = set()
        for state in q:
            for button in range(1, 5):
                new_state = get_new_state(state, button)
                new_q.add(new_state)
        q = list(new_q)

    q = [state for state in q if valid(state, ons, offs)]
    q.sort()
    with open("lamps.out", "w") as f:
        if not q:
            f.write("IMPOSSIBLE\n")
        else:
            for state in q:
                f.write(f"{state}\n")


if __name__ == "__main__":
    main()
