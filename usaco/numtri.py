"""
ID: toannq12
LANG: PYTHON3
TASK: numtri
"""


def main():
    dp = None
    with open("numtri.in", "r") as f:
        R = int(f.readline().strip())
        for _ in range(R):
            nums = f.readline().strip().split()
            nums = [int(x) for x in nums]
            if dp is None:
                dp = nums
            else:
                new_dp = []
                for i, num in enumerate(nums):
                    if i == 0:
                        new_dp.append(num + dp[0])
                    elif i == len(nums) - 1:
                        new_dp.append(num + dp[-1])
                    else:
                        new_dp.append(max(dp[i], dp[i - 1]) + num)
                dp = new_dp

    with open("numtri.out", "w") as f:
        f.write(f"{max(dp)}\n")


if __name__ == "__main__":
    main()
