def main():
    text = input()
    pi = [0] * len(text)
    for i in range(1, len(text)):
        j = pi[i - 1]
        while j and text[j] != text[i]:
            j = pi[j - 1]
        if text[j] == text[i]:
            pi[i] = j + 1

    res = []
    l = pi[-1]
    while l:
        res.append(l)
        l = pi[l - 1]

    print(*res[::-1])


main()
