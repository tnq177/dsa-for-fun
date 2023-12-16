def two_knights(n):
    if n == 1:
        return 0
    # there are n * n spots, choose 2
    total = n * n * (n * n - 1) // 2
    """
    only count attack down
    1. (r + 1, c - 2)
    - (R - 1) such (r + 1)
    - (C - 2) such (c - 2)
    - hence (R - 1) * (C - 2)

    similarly for:
    (r + 1, c + 2)
    (r + 2, c - 1)
    (r + 2, c + 1)
    """
    R = C = n
    attack = 2 * (C - 2) * (R - 1) + 2 * (R - 2) * (C - 1)
    return total - attack


def main():
    n = int(input())
    for i in range(1, n + 1):
        print(two_knights(i))


main()
