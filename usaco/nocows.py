"""
ID: toannq12
LANG: PYTHON3
TASK: nocows
"""
MOD = 9901


def main():
    with open("nocows.in", "r") as f:
        N, K = [int(x) for x in f.readline().strip().split()]

    cache = {}
    # how the heck did I solve this problem years ago...
    def num_trees_height_k_or_less(n, k):
        if n % 2 == 0:
            return 0
        if n == 1:
            return 1
        if k == 1:
            return 1 if n == 1 else 0
        if (n, k) in cache:
            return cache[(n, k)]

        total = 0
        for left in range(1, n - 1, 2):
            right = n - 1 - left
            num_left = num_trees_height_k_or_less(left, k - 1) % MOD
            num_right = num_trees_height_k_or_less(right, k - 1) % MOD
            total = (total + num_left * num_right) % MOD
        cache[(n, k)] = total
        return total

    result = (num_trees_height_k_or_less(N, K) - num_trees_height_k_or_less(N, K - 1)) % MOD
    with open("nocows.out", "w") as f:
        f.write(f"{result}\n")


if __name__ == "__main__":
    main()
