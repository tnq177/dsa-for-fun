import heapq as H


def main():
    n, k = [int(x) for x in input().strip().split()]
    nums = [int(x) for x in input().strip().split()]
    top = []
    bottom = []
    top_idxs = set()
    bottom_idxs = set()
    for i in range(k):
        H.heappush(bottom, (-nums[i], i))
        bottom_idxs.add(i)

    while len(bottom_idxs) > len(top_idxs):
        x, i = H.heappop(bottom)
        bottom_idxs.remove(i)
        H.heappush(top, (-x, i))
        top_idxs.add(i)

    if len(bottom_idxs) == len(top_idxs):
        res = [-bottom[0][0]]
    else:
        res = [top[0][0]]

    for idx in range(k, len(nums)):
        num = nums[idx]
        removed_idx = idx - k
        if removed_idx in top_idxs:
            top_idxs.remove(removed_idx)
        if removed_idx in bottom_idxs:
            bottom_idxs.remove(removed_idx)

        while top and top[0][1] <= removed_idx:
            H.heappop(top)
        while bottom and bottom[0][1] <= removed_idx:
            H.heappop(bottom)

        H.heappush(top, (num, idx))
        top_idxs.add(idx)
        x, i = H.heappop(top)
        top_idxs.remove(i)
        H.heappush(bottom, (-x, i))
        bottom_idxs.add(i)

        while len(bottom_idxs) > len(top_idxs):
            x, i = H.heappop(bottom)
            if i <= removed_idx:
                continue
            bottom_idxs.remove(i)
            H.heappush(top, (-x, i))
            top_idxs.add(i)

        while top and top[0][1] <= removed_idx:
            H.heappop(top)
        while bottom and bottom[0][1] <= removed_idx:
            H.heappop(bottom)

        if len(bottom_idxs) == len(top_idxs):
            res.append(-bottom[0][0])
        else:
            res.append(top[0][0])

    print(*res)


main()
