import sys
from collections import Counter


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        a = [int(next(tokens)) for _ in range(n)]
        order = sorted(range(n), key=a.__getitem__)
        f = max(Counter(a).values())
        b = [0]*n
        for i, index in enumerate(order):
            b[index] = a[order[(i+f)%n]]
        out.append(str(sum(x != y for x,y in zip(a,b))))
        out.append(' '.join(map(str,b)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
