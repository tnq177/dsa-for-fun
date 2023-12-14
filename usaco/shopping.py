"""
ID: toannq12
LANG: PYTHON3
TASK: shopping
"""

from collections import defaultdict


def main():
    offers = defaultdict(list)
    remain = {}
    codes = []
    with open("shopping.in", "r") as f:
        S = int(f.readline().strip())
        for _ in range(S):
            tmp = [int(x) for x in f.readline().strip().split()]
            price = tmp[-1]
            code_count = []
            for i in range(1, len(tmp) - 1, 2):
                code_count.append((tmp[i], tmp[i + 1]))
            code_count.sort(key=lambda x: x[0])
            tmp = []
            for code, count in code_count:
                tmp.append(code)
                tmp.append(count)
            offers[tuple(tmp)].append(price)

        B = int(f.readline().strip())
        for _ in range(B):
            c, k, p = [int(x) for x in f.readline().strip().split()]
            remain[c] = k
            codes.append(c)
            offers[(c, 1)].append(p)

    code2idx = {c: i for i, c in enumerate(codes)}
    keys = list(offers.keys())
    new_offers = {}
    for k in keys:
        prices = offers[k]
        prices.sort()
        tmp = []
        for i in range(0, len(k), 2):
            tmp.append(code2idx[k[i]])
            tmp.append(k[i + 1])
        new_offers[tuple(tmp)] = prices[0]

    offers = new_offers
    # the key is to use number as state instead of tuple
    # also precalculate these powers
    powers = [6**code_idx for code_idx in range(len(code2idx) + 1)]
    cache = {}

    def dfs(state):
        if state == 0:
            return 0

        if state in cache:
            return cache[state]

        costs = []
        for offer in offers:
            new_state = state
            good = True
            price = offers[offer]
            for i in range(0, len(offer), 2):
                item_code = offer[i]
                item_count = offer[i + 1]
                state_count = state % powers[item_code + 1]
                state_count //= powers[item_code]
                if state_count < item_count:
                    good = False
                    break
                new_state -= powers[item_code] * item_count

            if good:
                costs.append(price + dfs(new_state))

        cache[state] = min(costs)
        return cache[state]

    state = 0
    for code in remain:
        state += remain[code] * powers[code2idx[code]]
    with open("shopping.out", "w") as f:
        f.write(f"{dfs(state)}\n")


if __name__ == "__main__":
    main()
