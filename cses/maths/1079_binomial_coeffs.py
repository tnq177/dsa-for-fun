"""
References:
* https://cp-algorithms.com/combinatorics/binomial-coefficients.html
* https://cp-algorithms.com/algebra/module-inverse.html#mod-inv-all-num
* https://cp-algorithms.com/algebra/extended-euclid-algorithm.html
* https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm#Iterative_algorithm_3
"""


def egcd(a, b):
    # find (g, x, y) such that ax + by = g = gcd(a, b)
    if a == 0:
        return b, 0, 1
    b_div_a, b_mod_a = b // a, b % a
    g, x, y = egcd(b_mod_a, a)
    return (g, y - b_div_a * x, x)


def modinv(a, b):
    # find x that (x * a) % b == 1
    g, x, _ = egcd(a, b)
    if g != 1:
        raise ValueError("gcd(a, b) != 1")
    return x % b


def main():
    MOD = 10**9 + 7
    mod = [1] * (10**6 + 1)
    inv_mod = [1] * (10**6 + 1)
    for i in range(1, 10**6 + 1):
        mod[i] = (i * mod[i - 1]) % MOD
        if i == 1:
            inv_mod[i] = 1
        else:
            inv_i = modinv(i, MOD)
            inv_mod[i] = (inv_mod[i - 1] * inv_i) % MOD

    n = int(input().strip())
    for _ in range(n):
        a, b = [int(x) for x in input().strip().split()]
        b1 = mod[a]
        b2 = inv_mod[b]
        b3 = inv_mod[a - b]
        b12 = (b1 * b2) % MOD
        b123 = (b12 * b3) % MOD
        print(b123)


main()
