"""
Lesson to speed up:
- don't use float("inf")
- remove all commented out code
- cache chained-dotted methods
- try to minimize list comprehension such as with shortest below (no additional loop to set shortest[i][i])
- sometimes it's faster to do 1-indexed. For example in this problem,
    if we care about 0-indexed, we need to do a-=1, b-=1 which adds more computation
    to the m-loop. And m can be n^2 --> a lot of computations
- use enumerate in the triple-loop below somehow makes it faster ??!!
"""
import sys

MAX = 10**16
inp = sys.stdin.readline


def map_input():
    return map(int, inp().split())


def main():
    n, m, q = map_input()
    shortest = [[0 if i == j else MAX for i in range(n + 1)] for j in range(n + 1)]
    for _ in range(m):
        a, b, w = map_input()
        shortest[a][b] = shortest[b][a] = min(shortest[a][b], w)

    for c, dc in enumerate(shortest):
        for a, da in enumerate(shortest):
            for b in range(1, n + 1):
                if da[b] > da[c] + dc[b]:
                    da[b] = da[c] + dc[b]

    for _ in range(q):
        a, b = map_input()
        print(shortest[a][b] if shortest[a][b] != MAX else -1)


if __name__ == "__main__":
    main()
