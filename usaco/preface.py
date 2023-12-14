"""
ID: toannq12
LANG: PYTHON3
TASK: preface
"""

from collections import Counter

DIGITS = [
    ("I", 1),
    ("IV", 4),
    ("V", 5),
    ("IX", 9),
    ("X", 10),
    ("XL", 40),
    ("L", 50),
    ("XC", 90),
    ("C", 100),
    ("CD", 400),
    ("D", 500),
    ("CM", 900),
    ("M", 1000),
]


def num2roman(num):
    i = len(DIGITS) - 1
    res = []
    while num:
        if num < DIGITS[i][1]:
            i -= 1
        elif num == DIGITS[i][1]:
            res.append(DIGITS[i][0])
            num = 0
        else:
            res.append(DIGITS[i][0] * (num // DIGITS[i][1]))
            num %= DIGITS[i][1]
            i -= 1

    return "".join(res)


def main():
    with open("preface.in", "r") as f:
        N = int(f.readline().strip())

    count = Counter()
    for num in range(1, N + 1):
        count.update(num2roman(num))

    with open("preface.out", "w") as f:
        for (roman, _) in DIGITS:
            if count[roman] > 0:
                f.write(f"{roman} {count[roman]}\n")


if __name__ == "__main__":
    main()
