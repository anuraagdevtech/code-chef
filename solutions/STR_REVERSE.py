import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        s = next(tokens)
        n = len(s)
        matched = 0
        for char in s:
            if matched < n and char == s[n-1-matched]:
                matched += 1
        out.append(str(n-matched))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
