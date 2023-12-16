def main():
    board = [input().strip() for _ in range(8)]

    res = [0]
    cols = set(range(8))
    sub_diag = set(range(-7, 8))
    sum_diag = set(range(15))

    def dfs(r):
        if r == 8:
            res[0] += 1
            return
        possible_cols = list(cols)
        for c in possible_cols:
            if board[r][c] == "*":
                continue
            if (r - c) not in sub_diag:
                continue
            if (r + c) not in sum_diag:
                continue
            sub_diag.remove(r - c)
            sum_diag.remove(r + c)
            cols.remove(c)
            dfs(r + 1)
            cols.add(c)
            sum_diag.add(r + c)
            sub_diag.add(r - c)

    dfs(0)

    print(f"{res[0]}\n")


main()
