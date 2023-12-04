"""
ID: toannq12
LANG: PYTHON3
TASK: inflate
"""


def main():
    tmp = []
    with open("inflate.in", "r") as f:
        for line in f:
            tmp.append(tuple([int(x) for x in line.strip().split()]))
    M = tmp[0][0]
    classes = tmp[1:]

    dp = [0] * (M + 1)

    # this will pass, but why? shouldn't we solve the smaller problems first?
    # dp[remain - minute] could change later, no?
    for point, minute in classes:
        for remain in range(minute, len(dp)):
            dp[remain] = max(dp[remain], point + dp[remain - minute])

    # this will timeout, though this is easier to understand imo
    # for remain in range(1, M + 1):
    #     for point, minute in classes:
    #         if remain < minute:
    #             break
    #         dp[remain] = max(dp[remain], point + dp[remain - minute])

    with open("inflate.out", "w") as f:
        f.write(f"{dp[M]}\n")
