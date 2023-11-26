"""
ID: toannq12
LANG: PYTHON3
TASK: milk
"""


def main():
    with open("milk.in", "r") as f:
        NM = f.readline().strip().split()
        N, M = [int(x) for x in NM]
        price_amount = []
        for _ in range(M):
            pa = f.readline().strip().split()
            pa = [int(x) for x in pa]
            price_amount.append(pa)

    price_amount.sort(key=lambda x: x[0], reverse=True)
    cost = 0
    remain = N
    while remain > 0:
        price, amount = price_amount.pop()
        bought = min(amount, remain)
        cost += bought * price
        remain -= bought

    with open("milk.out", "w") as f:
        f.write(f"{cost}\n")


if __name__ == "__main__":
    main()
