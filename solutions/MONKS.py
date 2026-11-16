import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        a = sorted(int(next(tokens)) for _ in range(n))
        total = sum(a)
        keep = 1
        for k, value in enumerate(a, 1):
            if k*value <= total:
                keep = k
            else:
                break
        out.append(str(n-keep))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
