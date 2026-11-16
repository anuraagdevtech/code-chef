import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        s = next(tokens)
        parity = answer = 0
        for i, digit in enumerate(s):
            if i % 2 == 0:
                parity ^= digit - 48
            answer = (2 * answer + parity) % 998244353
        out.append(str(answer))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
