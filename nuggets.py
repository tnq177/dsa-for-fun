"""
ID: toannq12
LANG: PYTHON3
TASK: nuggets
"""

from functools import reduce


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def main():
    with open("nuggets.in", "r") as f:
        nums = [int(line.strip()) for line in f]
    nums = nums[1:]
    res = float("-inf")

    _gcd = reduce(gcd, nums)
    if _gcd > 1:
        # difference if any 2 consecutive numbers in the future
        # is a multiple of _gcd
        # if _gcd > 1, there will always be impossible numbers in between
        res = 0
    else:
        # given the 2 primes M & N, the maximum number we cannot make is MN - M - N
        # hence we only have to search within the range 256 * 256
        max_num = max(nums)
        dp = [False] * (max_num * max_num + 1)
        for num in nums:
            dp[num] = True
        for i in range(len(dp)):
            if dp[i]:
                for num in nums:
                    if i + num < len(dp):
                        dp[i + num] = True
            else:
                res = max(res, i)

    with open("nuggets.out", "w") as f:
        f.write(f"{res}\n")


if __name__ == "__main__":
    main()
