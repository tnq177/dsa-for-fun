"""
ID: toannq12
LANG: PYTHON3
TASK: skidesign
"""


def main():
    with open("skidesign.in", "r") as f:
        N = int(f.readline().strip())
        hills = [int(f.readline().strip()) for _ in range(N)]

    min_cost = float("inf")
    for min_height in range(84):
        cost = 0
        for h in hills:
            if h < min_height:
                cost += (min_height - h) ** 2
            elif h - min_height > 17:
                cost += (h - min_height - 17) ** 2
        min_cost = min(min_cost, cost)

    with open("skidesign.out", "w") as f:
        f.write(f"{min_cost}\n")


if __name__ == "__main__":
    main()
