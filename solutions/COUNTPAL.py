import sys


def main() -> None:
    s = sys.stdin.buffer.read().strip()
    n = len(s)
    palindrome = bytearray(n)
    ways = [0]*(n+1)
    ways[0] = 1
    for right in range(n):
        total = 0
        for left in range(right+1):
            palindrome[left] = s[left] == s[right] and (right-left < 2 or palindrome[left+1])
            if palindrome[left]:
                total += ways[left]
        ways[right+1] = total%1000000007
    print(ways[n])

if __name__ == '__main__':
    main()
