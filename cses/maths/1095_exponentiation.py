MOD = 10**9 + 7


def exp(a, b):
    if b == 0:
        return 1
    if a == 0:
        return 0
    prod = 1
    while b > 1:
        if b % 2 == 0:
            b //= 2
            a = (a * a) % MOD
        else:
            prod = (prod * a) % MOD
            b -= 1

    return (a * prod) % MOD


def main():
    n = int(input().strip())
    for _ in range(n):
        a, b = [int(x) for x in input().strip().split()]
        print(exp(a, b))


main()
