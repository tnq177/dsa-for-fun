"""
ID: toannq12
LANG: PYTHON3
TASK: fence
"""
from collections import defaultdict, Counter, deque


def fopen():
    fin = open("fence.in", "r")
    fout = open("fence.out", "w")
    return fin, fout


def fclose(*fobjs):
    for f in fobjs:
        f.close()


def main():
    fences = defaultdict(list)
    fence_count = defaultdict(Counter)
    fin, fout = fopen()
    F = int(fin.readline())

    count = Counter()
    for _ in range(F):
        a, b = map(int, fin.readline().strip().split())
        fences[a].append(b)
        fences[b].append(a)
        fence_count[a][b] += 1
        fence_count[b][a] += 1
        count[a] += 1
        count[b] += 1

    new_fences = {}
    for node in fences:
        next_nodes = fences[node]
        next_nodes.sort()
        new_fences[node] = deque(next_nodes)
    fences = new_fences

    odd = [v for v in count if count[v] % 2 != 0]
    if odd:
        # Eulerian path
        start = min(odd)
    else:
        # all even vertices, Eulerian cycle, choose the smallest one
        start = min(count.keys())

    stack = [start]
    res = []
    while stack:
        node = stack[-1]
        while fences[node] and fence_count[node][fences[node][0]] == 0:
            fences[node].popleft()
        if not fences[node]:
            res.append(stack.pop())
        else:
            next_node = fences[node].popleft()
            fence_count[node][next_node] -= 1
            fence_count[next_node][node] -= 1
            stack.append(next_node)

    res = res[::-1]
    for node in res:
        fout.write(f"{node}\n")
    fclose(fin, fout)


if __name__ == "__main__":
    main()
