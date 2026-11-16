import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        x, r, m = (int(next(tokens)) for _ in range(3))
        r *= 60
        out.append('YES' if r + max(0, r-x) <= 60*m else 'NO')
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
