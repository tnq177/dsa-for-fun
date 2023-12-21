def main():
    text = input().strip()
    pattern = input().strip()

    # build a prefix function pi
    # pi[i] is the length of the longest proper prefix
    pi = [0] * len(pattern)
    for i in range(1, len(pattern)):
        j = pi[i - 1]
        while j and pattern[j] != pattern[i]:
            j = pi[j - 1]
        if pattern[j] == pattern[i]:
            pi[i] = j + 1

    # now search for the pattern within the text
    # we keep 2 pointers, 1 in pattern 1 in text
    # we've matched pattern[:j] with text[:i]
    # (i.e. the part up to text[:i] that matches pattern[:j])
    # we have to compare pattern[j] with text[i] now
    # if they don't match, we have to move j to the
    # longest prefix in pattern that match with text[:i]
    # that is j = pi[j - 1]
    res = 0
    j = 0
    for i, c in enumerate(text):
        while j and pattern[j] != c:
            j = pi[j - 1]
        if pattern[j] == text[i]:
            j += 1
            if j == len(pattern):
                j = pi[j - 1]
                res += 1

    print(res)


main()
