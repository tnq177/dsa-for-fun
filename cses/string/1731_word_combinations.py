def main():
    text = input().strip()
    matches = [[] for _ in range(len(text))]

    k = int(input())
    for _ in range(k):
        word = input().strip()
        if len(word) > len(text):
            continue

        pi = [0] * len(word)
        for i in range(1, len(word)):
            j = pi[i - 1]
            while j and word[j] != word[i]:
                j = pi[j - 1]
            if word[j] == word[i]:
                pi[i] = j + 1

        j = 0
        i = 0
        while len(text) - i >= len(word) - j:
            while j and word[j] != text[i]:
                j = pi[j - 1]
            if word[j] == text[i]:
                j += 1
                if j == len(word):
                    matches[i + 1 - len(word)].append(len(word))
                    j = pi[j - 1]
            i += 1

    MOD = 10**9 + 7
    dp = [0] * (len(text) + 1)
    for i in range(len(text)):
        prev = 1 if i == 0 else dp[i]
        if not prev:
            continue
        for word_len in matches[i]:
            dp[i + word_len] = (dp[i + word_len] + prev) % MOD

    print(dp[-1])


main()
