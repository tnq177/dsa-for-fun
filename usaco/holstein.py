"""
ID: toannq12
LANG: PYTHON3
TASK: holstein
"""


def is_enough(feed_idxs, feeds, target):
    total = [0] * len(feeds[0])
    for feed_idx in feed_idxs:
        feed = feeds[feed_idx]
        for i, f in enumerate(feed):
            total[i] += f

    for a, b in zip(total, target):
        if a < b:
            return False
    return True


def main():
    with open("holstein.in", "r") as f:
        V = int(f.readline().strip())
        target = f.readline().strip().split()
        target = [int(x) for x in target]
        feeds = []
        G = int(f.readline().strip())
        for _ in range(G):
            tmp = f.readline().strip().split()
            feeds.append([int(x) for x in tmp])

    res = [None]
    curr_set = [[]]
    for _ in range(1, G + 1):
        if res[0] is not None:
            break
        new_set = []
        for prev_set in curr_set:
            if res[0] is not None:
                break
            if not prev_set:
                candidates = range(G)
            else:
                candidates = range(prev_set[-1] + 1, G)
            for cand in candidates:
                new_set.append(prev_set + [cand])
                if is_enough(new_set[-1], feeds, target):
                    res[0] = new_set[-1][:]
                    break
        curr_set = new_set

    res = res[0]
    msg = "{} {}\n".format(len(res), " ".join([str(x + 1) for x in res]))
    with open("holstein.out", "w") as f:
        f.write(msg)


if __name__ == "__main__":
    main()
