"""
ID: toannq12
LANG: PYTHON3
TASK: ariprog
"""
from collections import defaultdict


def main():
    with open("ariprog.in", "r") as f:
        N = int(f.readline().strip())
        M = int(f.readline().strip())

    cache = set()
    for p in range(M + 1):
        for q in range(p, M + 1):
            cache.add(p * p + q * q)

    nums = list(cache)
    nums.sort()
    res = defaultdict(list)
    for i in range(len(nums) - 1, N - 2, -1):
        end_num = nums[i]
        max_gap = end_num // (N - 1)
        # this is the key, don't loop from gap=1 to max_gap
        # rather loop through possible gap values only
        for j in range(i - 1, -1, -1):
            gap = end_num - nums[j]
            if gap > max_gap:
                break
            for k in range(N):
                if (end_num - k * gap) not in cache:
                    break
            else:
                res[gap].append(end_num - (N - 1) * gap)

    if not res:
        msg = "NONE\n"
    else:
        gaps = sorted(res.keys())
        msg = ""
        for gap in gaps:
            for num in res[gap][::-1]:
                msg += f"{num} {gap}\n"

    with open("ariprog.out", "w") as f:
        f.write(msg)


if __name__ == "__main__":
    main()
