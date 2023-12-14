"""
ID: toannq12
LANG: PYTHON3
TASK: buylow
"""

from collections import defaultdict


def main():
    nums = []
    with open("buylow.in", "r") as f:
        for line in f:
            nums.extend([int(x) for x in line.strip().split()])
    nums = nums[1:]

    bp = defaultdict(list)
    dp = [0] * len(nums)
    max_seq_len = 0
    for i in range(len(nums)):
        max_count = 1
        for j in range(i):
            if nums[j] > nums[i]:
                max_count = max(max_count, dp[j] + 1)
        dp[i] = max_count
        max_seq_len = max(max_seq_len, dp[i])
        for j in range(i):
            if nums[j] > nums[i] and dp[j] + 1 == max_count:
                bp[i].append(j)

    curr = defaultdict(set)
    for i in range(len(nums)):
        if dp[i] == max_seq_len:
            curr[nums[i]].add(i)

    print(curr)
    layers = [curr]
    while len(layers) < max_seq_len:
        new_curr = defaultdict(set)
        for num in curr:
            for i in curr[num]:
                for j in bp[i]:
                    new_curr[nums[j]].add(j)
        layers.append(new_curr)
        print(new_curr)
        curr = new_curr

    formatted = []
    for layer in layers:
        tmp = []
        for num in layer:
            idxs = list(layer[num])
            idxs.sort()
            tmp.append([num] + [idxs[0], idxs[-1]])
        formatted.append(tmp)
    layers = formatted

    dp_count = [1] * len(layers[0])
    print(layers[0])
    for layer_idx in range(1, len(layers)):
        new_dp_count = []
        for num, min_i, max_i in layers[layer_idx]:
            count = 0
            for j, (prev_num, prev_min_i, prev_max_i) in enumerate(
                layers[layer_idx - 1]
            ):
                if num > prev_num and prev_max_i > min_i:
                    count += dp_count[j]
            new_dp_count.append(count)
        print('---')
        print(layers[layer_idx])
        print(new_dp_count)
        dp_count = new_dp_count

    count = sum(dp_count)
    with open("buylow.out", "w") as f:
        f.write(f"{max_seq_len} {count}\n")


if __name__ == "__main__":
    main()
