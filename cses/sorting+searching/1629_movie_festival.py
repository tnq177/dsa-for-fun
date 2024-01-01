"""
same as https://leetcode.com/problems/non-overlapping-intervals/description/
the key is we remove the minimum number of intervals so that the rest
are disjoint.

how do we do it? classic sorting and scanning can tell us if we're seeing 2 overlapping
intervals or not. If there is, we gotta remove one of them. No choice.

The key is after we remove, we want to keep the one furthest to the past as possible,
i.e. end = min(end, new_end)
"""


def main():
    n = int(input())
    intervals = []
    for _ in range(n):
        start, end = [int(x) for x in input().strip().split()]
        intervals.append((start, end))
    intervals.sort(key=lambda x: x[0])

    res = 0
    prev_end = None
    for start, end in intervals:
        if prev_end is None:
            prev_end = end
        elif start < prev_end:
            res += 1
            prev_end = min(prev_end, end)
        else:
            prev_end = end

    print(n - res)


main()
