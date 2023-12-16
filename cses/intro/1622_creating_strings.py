from collections import Counter


def main():
    count = Counter(input().strip())
    res = []

    def dfs(path):
        if not count:
            res.append("".join(path))
            return

        chars = list(count.keys())
        chars.sort()
        for ch in chars:
            path.append(ch)
            count[ch] -= 1
            if count[ch] == 0:
                del count[ch]
            dfs(path)
            count[ch] += 1
            path.pop()

    dfs([])
    print(len(res))
    print(*res, sep="\n")


main()
