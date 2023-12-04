"""
ID: toannq12
LANG: PYTHON3
TASK: stamps
"""

# this solution will timeout. I don't think it's feasible with Python...
def calc_continuous(K, stamps):
    dp = [float("inf")] * (K * max(stamps) + 2)
    dp[0] = 0
    for i in range(1, len(dp)):
        for stamp in stamps:
            if i >= stamp:
                dp[i] = min(dp[i - stamp] + 1, dp[i])
        if dp[i] > K:
            return i -1


def main():
    tmp = []
    with open("stamps.in", "r") as f:
        for line in f:
            tmp.extend(line.strip().split())
    tmp = [int(x) for x in tmp]
    K = tmp[0]
    stamps = tmp[2:]
    res = calc_continuous(K, stamps)
    with open("stamps.out", "w") as f:
        f.write(f"{res}\n")


if __name__ == "__main__":
    main()
