def main():
    n = int(input())

    power5 = 1
    power = 0
    while power5 * 5 <= n:
        power5 *= 5
        power += 1

    res = 0
    cumsum_power5 = 0
    while power >= 1:
        count = n // power5
        # there are `count` multiple of power5, each has `power` 5 factors
        res += power * count
        # but this overlaps with previous higher power5
        res -= cumsum_power5
        power -= 1
        power5 //= 5
        cumsum_power5 += count

    print(res)


main()
