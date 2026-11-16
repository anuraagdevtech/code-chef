import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        r, c, k = (int(next(tokens)) for _ in range(3))
        rows = min(8,r+k)-max(1,r-k)+1
        cols = min(8,c+k)-max(1,c-k)+1
        out.append(str(rows*cols))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
