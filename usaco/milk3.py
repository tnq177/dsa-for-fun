"""
ID: toannq12
LANG: PYTHON3
TASK: milk3
"""


def main():
    with open("milk3.in", "r") as f:
        capacities = f.readline().strip().split()
        capacities = [int(x) for x in capacities]

    all_states = set()

    def dfs(state):
        for i in range(3):
            if state[i] == 0:
                continue
            for j in range(3):
                if i == j:
                    continue
                # pour i to j
                new_state = [0] * 3
                new_state[3 - i - j] = state[3 - i - j]
                if state[i] + state[j] <= capacities[j]:
                    new_state[i] = 0
                    new_state[j] = state[i] + state[j]
                else:
                    new_state[i] = state[i] + state[j] - capacities[j]
                    new_state[j] = capacities[j]

                new_state = tuple(new_state)
                if new_state not in all_states:
                    all_states.add(new_state)
                    dfs(new_state)

    dfs((0, 0, capacities[-1]))
    res = [state[-1] for state in all_states if state[0] == 0]
    res = list(set(res))
    res.sort()
    res = " ".join([str(x) for x in res]) + "\n"
    with open("milk3.out", "w") as f:
        f.write(res)


if __name__ == "__main__":
    main()
