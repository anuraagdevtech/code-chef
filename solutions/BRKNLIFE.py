import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n, m = int(next(tokens)), int(next(tokens))
        s = next(tokens).decode()
        a = next(tokens).decode()
        matched = 0
        result = []
        for char in s:
            if char == '?':
                char = 'b' if matched < m and a[matched] == 'a' else 'a'
            result.append(char)
            if matched < m and char == a[matched]:
                matched += 1
        out.append(''.join(result) if matched < m else '-1')
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
