import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,m = int(next(tokens)),int(next(tokens))
        out.append(str(n*(m-1)+m*(n-1)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
