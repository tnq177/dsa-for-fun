"""
ID: toannq12
LANG: PYTHON3
TASK: sort3
"""
from collections import Counter


def main():
    with open("sort3.in", "r") as f:
        N = int(f.readline().strip())
        nums = [int(f.readline().strip()) for _ in range(N)]

    num1in2 = num1in3 = num2in3 = num2in1 = num3in1 = num3in2 = 0
    count = Counter(nums)
    for i, num in enumerate(nums):
        if i < count[1]:
            if num == 2:
                num2in1 += 1
            if num == 3:
                num3in1 += 1
        elif count[1] <= i < count[2] + count[1]:
            if num == 1:
                num1in2 += 1
            if num == 3:
                num3in2 += 1
        else:
            if num == 1:
                num1in3 += 1
            if num == 2:
                num2in3 += 1

    res = 0
    swap = min(num1in2, num2in1)
    res += swap
    num1in2 -= swap
    num2in1 -= swap

    swap = min(num1in3, num3in1)
    res += swap
    num1in3 -= swap
    num3in1 -= swap

    swap = min(num2in3, num3in2)
    res += swap
    num2in3 -= swap
    num3in2 -= swap

    # after above swap, there remains 1in2, 2in3, 3in1
    # or 1in3, 2in1, 3in2...
    # these must be the same so we can do the cycle swap
    # and each cycle swap takes 2 swaps
    res += 2 * (num2in1 + num3in1)
    with open("sort3.out", "w") as f:
        f.write(f"{res}\n")


if __name__ == "__main__":
    main()
