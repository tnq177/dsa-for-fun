def main():
    n = int(input())
    maze = [input() for _ in range(n)]
    if maze[0][0] == "*":
        print(0)
        return

    MOD = 10**9 + 7
    dp = [0] * n
    for i, c in enumerate(maze[0]):
        if c == "*":
            break
        dp[i] = 1

    for row in maze[1:]:
        new_dp = []
        for j, c in enumerate(row):
            if c == "*":
                new_dp.append(0)
            else:
                left = 0 if j == 0 else new_dp[-1]
                top = 0 if dp is None else dp[j]
                new_dp.append((top + left) % MOD)
        dp = new_dp

    print(dp[-1])


main()
