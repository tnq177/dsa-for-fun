def main():
    _ = input()
    nums = input().strip().split()
    seen = set()
    for num in nums:
        seen.add(num)
    print(len(seen))

main()
