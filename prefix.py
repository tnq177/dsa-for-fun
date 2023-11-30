"""
ID: toannq12
LANG: PYTHON3
TASK: prefix
"""
from functools import lru_cache


def main():
    primitives = []
    S = []
    flag = True
    with open("prefix.in", "r") as f:
        for line in f:
            line = line.strip()
            if line == ".":
                flag = False
                continue
            if flag:
                primitives.extend(line.strip().split())
            else:
                S.append(line.strip())
    S = "".join(S)

    dp = [False] * len(S)
    for i in range(len(dp)):
        if i != 0 and not dp[i - 1]:
            continue
        for p in primitives:
            if S[i : i + len(p)] == p:
                dp[i + len(p) - 1] = True

    max_len = 0
    for i in range(len(S)):
        if dp[i]:
            max_len = i + 1

    with open("prefix.out", "w") as f:
        f.write(f"{max_len}\n")


if __name__ == "__main__":
    main()
