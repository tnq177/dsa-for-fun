"""
ID: toannq12
LANG: PYTHON3
TASK: crypt1
"""


def inset(num, digits):
    while num:
        if (num % 10) not in digits:
            return False
        num //= 10
    return True


def main():
    with open("crypt1.in", "r") as f:
        N = int(f.readline().strip())
        digits = f.readline().strip().split()
        digits = [int(d) for d in digits]

    digits = set(digits)
    res = 0
    for d1 in digits:
        for d2 in digits:
            for d3 in digits:
                for d4 in digits:
                    for d5 in digits:
                        num1 = d1 * 100 + d2 * 10 + d3
                        num2 = d4 * 10 + d5
                        p1 = num1 * d4
                        p2 = num1 * d5
                        total = num1 * (10 * d4 + d5)
                        if (
                            not (100 <= num1 < 1000)
                            or not (10 <= num2 < 100)
                            or not (100 <= p1 < 1000)
                            or not (100 <= p2 < 1000)
                            or not (1000 <= total < 10000)
                        ):
                            continue

                        if all(inset(num, digits) for num in [p1, p2, total]):
                            res += 1

    with open("crypt1.out", "w") as f:
        f.write(f"{res}\n")


if __name__ == "__main__":
    main()
