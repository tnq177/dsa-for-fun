"""
ID: toannq12
LANG: PYTHON3
TASK: palsquare
"""


def digit2base(d):
    if d < 10:
        return str(d)
    else:
        return chr(ord("A") + d - 10)


def dec2base(num, B):
    if num == 0:
        return ["0"]
    res = []
    while num:
        res.append(digit2base(num % B))
        num //= B
    return res[::-1]


def is_pali(arr):
    i, j = 0, len(arr) - 1
    while i < j:
        if arr[i] != arr[j]:
            return False
        i += 1
        j -= 1
    return True


def main():
    with open("palsquare.in", "r") as f:
        B = int(f.readline().strip())

    with open("palsquare.out", "w") as f:
        for num in range(1, 301):
            square = num * num
            num_b = dec2base(num, B)
            square_b = dec2base(square, B)
            if is_pali(square_b):
                num_b = "".join(num_b)
                square_b = "".join(square_b)
                f.write(f"{num_b} {square_b}\n")


if __name__ == "__main__":
    main()
