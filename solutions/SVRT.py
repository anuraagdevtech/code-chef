import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n, k = int(next(tokens)), int(next(tokens))
        d = (n+k-1)//k
        out.append(f'{d} {n-k*(d-1)}')
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
