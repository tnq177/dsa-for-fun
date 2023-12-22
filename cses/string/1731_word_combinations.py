def main():
    text = input()
    text = [ord(c) - ord("a") for c in text]
    k = int(input())
    trie = {}
    for _ in range(k):
        word = input()
        curr = trie
        for c in word:
            curr = curr.setdefault(ord(c) - ord("a"), {})
        curr[-1] = True

    MOD = 10**9 + 7
    dp = [0] * (len(text) + 1)
    dp[0] = 1

    for i, prev in enumerate(dp):
        if not prev:
            continue
        curr = trie
        j = i
        while j < len(text) and text[j] in curr:
            curr = curr[text[j]]
            j += 1
            if -1 in curr:
                dp[j] = (dp[j] + prev) % MOD

    print(dp[-1])


main()
