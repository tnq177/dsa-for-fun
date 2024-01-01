def main():
    n = int(input())
    preorder = [int(x) for x in input().strip().split()]
    inorder = [int(x) for x in input().strip().split()]
    inval2idx = {x: i for i, x in enumerate(inorder)}

    post = [None] * n
    stack = [(0, n - 1, 0, n - 1, 0, n - 1)]
    while stack:
        pre_i, pre_j, in_i, in_j, pos_i, pos_j = stack.pop()
        # pre: root, left, right
        # in: left, root, right
        # post: left, right, root
        root_val = preorder[pre_i]
        left_size = inval2idx[root_val] - in_i
        right_size = pre_j - pre_i - left_size
        post[pos_j] = root_val

        if left_size > 0:
            stack.append(
                (
                    pre_i + 1,
                    pre_i + left_size,
                    in_i,
                    in_i + left_size - 1,
                    pos_i,
                    pos_i + left_size - 1,
                )
            )
        if right_size > 0:
            stack.append(
                (
                    pre_i + left_size + 1,
                    pre_j,
                    in_i + left_size + 1,
                    in_j,
                    pos_i + left_size,
                    pos_j - 1,
                )
            )
    print(*post, sep=" ")


main()
