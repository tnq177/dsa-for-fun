"""
ID: toannq12
LANG: PYTHON3
TASK: humble
"""
from collections import deque


def humble(primes, N):
    nums = [1]
    # for each prime, this is the index in nums of the smallest number
    # it's not been multiplied with yet
    num_idxs = [0] * len(primes)
    while len(nums) < N + 1:
        min_num = min(nums[num_idx] * primes[i] for i, num_idx in enumerate(num_idxs))
        nums.append(min_num)
        for i, num_idx in enumerate(num_idxs):
            num = primes[i] * nums[num_idx]
            if num == min_num:
                num_idxs[i] += 1
    return nums[-1]


def main():
    tmp = []
    with open("humble.in", "r") as f:
        for line in f:
            tmp.extend([int(x) for x in line.strip().split()])
    K, N = tmp[:2]
    primes = tmp[2:]

    res = humble(primes, N)
    with open("humble.out", "w") as f:
        f.write(f"{res}\n")


if __name__ == "__main__":
    main()
