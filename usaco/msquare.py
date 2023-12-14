"""
ID: toannq12
LANG: PYTHON3
TASK: msquare
"""
from collections import deque


def A(state):
    return state[4:] + state[:4]


def B(state):
    return state[3:4] + state[:3] + state[7:8] + state[4:7]


def C(state):
    return tuple(
        [
            state[0],
            state[5],
            state[1],
            state[3],
            state[4],
            state[6],
            state[2],
            state[7],
        ]
    )


def get_shortest_path(target):
    maps = {"A": A, "B": B, "C": C}
    seen = set()
    init = tuple(range(1, 5)) + tuple(range(8, 4, -1))
    seen.add(init)
    q = deque([(init, 0, "")])
    while q:
        state, dist, path = q.popleft()
        if state == target:
            return dist, path

        for func in "ABC":
            new_state = maps[func](state)
            if new_state not in seen:
                seen.add(new_state)
                q.append((new_state, dist + 1, path + func))


def main():
    with open("msquare.in", "r") as f:
        target = tuple([int(x) for x in f.readline().strip().split()])
        target = target[:4] + target[4:][::-1]
    dist, path = get_shortest_path(target)
    msg = f"{dist}\n"
    if not path:
        msg += "\n"
    else:
        i = 0
        while i < len(path):
            msg += path[i : i + 60] + "\n"
            i += 60
    with open("msquare.out", "w") as f:
        f.write(msg)


if __name__ == "__main__":
    main()
