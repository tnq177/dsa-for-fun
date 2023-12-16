"""
take 2/1 x times and 1/2 y times, we have
a = 2x + y
b = x + 2y
easy to find x, y and understand the conditions below
"""


def main():
    t = int(input())
    for _ in range(t):
        a, b = [int(x) for x in input().strip().split()]
        c1 = (2 * b) >= a
        c2 = (2 * a) >= b
        c3 = (2 * b - a) % 3 == 0
        c4 = (2 * a - b) % 3 == 0
        if c1 and c2 and c3 and c4:
            print("YES")
        else:
            print("NO")


main()
