"""
ID: toannq12
LANG: PYTHON3
TASK: game1
"""


def main():
    with open("game1.in", "r") as f:
        tmp = []
        for line in f:
            tmp.extend([int(x) for x in line.strip().split()])
        N = tmp[0]
        points = tmp[1:]

    l2r = []
    cs = 0
    for p in points:
        cs += p
        l2r.append(cs)

    def range_sum(i, j):
        left = 0 if i == 0 else l2r[i - 1]
        return l2r[j] - left

    dp = [[0] * N for _ in range(N)]
    for length in range(1, N + 1):
        for i in range(N):
            j = length + i - 1
            if j >= N:
                break
            if i == j:
                dp[i][j] = points[i]
            else:
                # pick i
                pi = points[i] + range_sum(i + 1, j) - dp[i + 1][j]
                pj = points[j] + range_sum(i, j - 1) - dp[i][j - 1]
                dp[i][j] = max(pi, pj)

    p1 = dp[0][N - 1]
    p2 = l2r[-1] - p1
    with open("game1.out", "w") as f:
        f.write(f"{p1} {p2}\n")


if __name__ == "__main__":
    main()
