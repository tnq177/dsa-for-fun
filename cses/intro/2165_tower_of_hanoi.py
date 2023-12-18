def main():
    k = int(input())

    res = [0]
    msg = []
    def move(n, fr, to):
        if n == 1:
            res[0] += 1
            msg.append(f"{fr} {to}")
        else:
            other = 6 - fr - to
            move(n - 1, fr, other)
            move(1, fr, to)
            move(n - 1, other, to)

    move(k, 1, 3)
    print(res[0])
    print(*msg, sep="\n")

main()
