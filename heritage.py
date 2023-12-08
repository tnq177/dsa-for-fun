"""
ID: toannq12
LANG: PYTHON3
TASK: heritage
"""


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def main():
    with open("heritage.in", "r") as f:
        inorder = f.readline().strip()
        preorder = f.readline().strip()

    cache = {c: i for i, c in enumerate(inorder)}
    root = TreeNode(None)
    stack = [(0, len(inorder) - 1, 0, len(preorder) - 1, root, True)]
    while stack:
        ii, ij, pi, pj, parent, is_left = stack.pop()
        if ii > ij:
            continue
        node = TreeNode(val=preorder[pi])
        if is_left:
            parent.left = node
        else:
            parent.right = node
        k = cache[preorder[pi]]
        left_size = k - 1 - ii + 1
        stack.append((ii, k - 1, pi + 1, pi + left_size, node, True))
        stack.append((k + 1, ij, pi + left_size + 1, pj, node, False))

    def postorder(tree):
        if not tree:
            return []
        return postorder(tree.left) + postorder(tree.right) + [tree.val]

    res = postorder(root.left)
    res = "".join(res)
    with open("heritage.out", "w") as f:
        f.write(f"{res}\n")


if __name__ == "__main__":
    main()
