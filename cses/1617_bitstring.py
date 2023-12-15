def main():
    n = int(input())
    MOD = 10**9 + 7
    res = 1
    for _ in range(n):
        res = (res * 2) % MOD
    print(res)


main()
