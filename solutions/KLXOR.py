import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n, k = int(next(tokens)), int(next(tokens))
        s = next(tokens)
        prefix = [0]*(n+1)
        for i, digit in enumerate(s):
            prefix[i+1] = prefix[i] ^ (digit-48)
        width = n-k+1
        out.append(str(sum(prefix[j+width]^prefix[j] for j in range(k))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
