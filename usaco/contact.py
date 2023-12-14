"""
ID: toannq12
LANG: PYTHON3
TASK: contact
"""

from collections import Counter, defaultdict
from functools import cmp_to_key


def cmp(p1, p2):
    if len(p1) < len(p2):
        return -1
    elif p1 == p2:
        return 0
    elif len(p1) == len(p2):
        return -1 if p1 < p2 else 1
    else:
        return 1


def main():
    with open("contact.in", "r") as f:
        seq = [line.strip() for line in f.readlines()]
    A, B, N = [int(x) for x in seq[0].split()]
    seq = "".join(seq[1:])

    count = Counter()
    for i in range(len(seq)):
        for l in range(A, B + 1):
            j = i + l - 1
            if j >= len(seq):
                break
            count[seq[i : j + 1]] += 1
    freq2seq = defaultdict(list)
    for seq in count:
        freq = count[seq]
        freq2seq[freq].append(seq)

    freqs = list(freq2seq.keys())
    freqs.sort(reverse=True)
    freqs = freqs[:N]
    with open("contact.out", "w") as f:
        for freq in freqs:
            f.write(f"{freq}\n")
            seqs = freq2seq[freq]
            seqs.sort(key=cmp_to_key(cmp))
            msg = ""
            for i in range(0, len(seqs), 6):
                msg += " ".join(seqs[i : i + 6]) + "\n"
            f.write(f"{msg}")


if __name__ == "__main__":
    main()
