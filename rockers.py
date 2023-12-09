"""
ID: toannq12
LANG: PYTHON3
TASK: rockers
"""


def main():
    with open("rockers.in", "r") as f:
        N, T, M = [int(x) for x in f.readline().strip().split()]
        songs = [int(x) for x in f.readline().strip().split()]

    res = [0]
    remain = [T] * M
    count = [0]

    def dfs(i):
        res[0] = max(res[0], count[0])
        if not remain or i == N:
            return

        # select i
        old_vals = []
        while remain and remain[-1] < songs[i]:
            old_vals.append(remain.pop())

        if remain:
            remain[-1] -= songs[i]
            count[0] += 1
            dfs(i + 1)
            count[0] -= 1
            remain[-1] += songs[i]

        while old_vals:
            remain.append(old_vals.pop())

        # don't select i
        dfs(i + 1)

    dfs(0)
    with open("rockers.out", "w") as f:
        f.write(f"{res[0]}\n")


if __name__ == "__main__":
    main()
