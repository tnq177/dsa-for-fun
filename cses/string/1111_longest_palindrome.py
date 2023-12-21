def main():
    s = input().strip()
    s = "#" + "#".join(s) + "#"

    # radius of palindrome at each position
    max_radius = [1] * len(s)
    # the range of the largest palindrome we're seeing
    left = right = 0
    best_left = best_right = None
    for i in range(1, len(s)):
        if i > right:
            # we're outside the largest palinedrome, run the naive check
            j, k = i - 1, i + 1
            while j >= 0 and k < len(s) and s[j] == s[k]:
                max_radius[i] += 1
                j -= 1
                k += 1
            left, right = j + 1, k - 1
        else:
            # we find the position j in the opposite side of the center
            # of the current largest palindrome
            # i should start with at least max_radius[j]
            j = left + right - i
            # but it cannot go outside the palindrome, hence the right - i
            max_radius[i] = min(right - i, max_radius[j])
            j, k = i - max_radius[i], i + max_radius[i]
            while j >= 0 and k < len(s) and s[j] == s[k]:
                max_radius[i] += 1
                j -= 1
                k += 1

            if i + max_radius[i] - 1 > right:
                # we've found a largest palindrome
                left, right = i - max_radius[i] + 1, i + max_radius[i] - 1

        if best_left is None or (best_right - best_left) < (right - left):
            best_left, best_right = left, right

    res = [s[i] for i in range(best_left, best_right + 1) if s[i] != "#"]
    print("".join(res))


main()
