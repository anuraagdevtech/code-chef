import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        s = next(tokens)
        palindrome = bytearray(n)
        best = list(range(n+1))
        for right in range(n):
            optimum = right+1
            for left in range(right+1):
                palindrome[left] = s[left] == s[right] and (right-left < 2 or palindrome[left+1])
                if palindrome[left]:
                    optimum = min(optimum,best[left]+1)
            best[right+1] = optimum
        out.append(str(best[n]))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
