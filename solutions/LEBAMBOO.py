import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        h = [int(next(tokens)) for _ in range(n)]
        d = [int(next(tokens))-v for v in h]
        if n == 1:
            answer = -d[0] if d[0] <= 0 else -1
        elif n == 2:
            answer = abs(d[0]) if sum(d) == 0 else -1
        else:
            total = sum(d)
            m, remainder = divmod(total, n-2)
            answer = m if remainder == 0 and m >= 0 and all(m >= x and (m-x)%2 == 0 for x in d) else -1
        out.append(str(answer))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
