"""
ID: toannq12
LANG: PYTHON3
TASK: namenum
"""


def get_trie():
    trie = {}
    with open("dict.txt", "r") as f:
        for line in f:
            name = line.strip()
            if not name:
                continue
            curr = trie
            for i, c in enumerate(name):
                if c not in curr:
                    curr[c] = {}
                if i == len(name) - 1:
                    curr[c]["end"] = True
                curr = curr[c]
    return trie


def main():
    trie = get_trie()
    with open("namenum.in", "r") as f:
        num = f.readline().strip()

    maps = {
        "2": "ABC",
        "3": "DEF",
        "4": "GHI",
        "5": "JKL",
        "6": "MNO",
        "7": "PRS",
        "8": "TUV",
        "9": "WXY",
    }

    res = []

    def dfs(i, name, curr):
        if i == len(num):
            if "end" in curr:
                res.append("".join(name))
            return

        chars = maps[num[i]]
        for c in chars:
            if c in curr:
                name.append(c)
                dfs(i + 1, name, curr[c])
                name.pop()

    dfs(0, [], trie)
    res.sort()
    with open("namenum.out", "w") as f:
        if not res:
            f.write("NONE\n")
        else:
            for name in res:
                f.write(f"{name}\n")


if __name__ == "__main__":
    main()
