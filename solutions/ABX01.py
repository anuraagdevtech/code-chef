import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        a, n = int(next(tokens)), int(next(tokens))
        r = pow(a,n,9)
        out.append(str(r or 9))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
