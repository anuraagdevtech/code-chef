import sys
from collections import Counter


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        s = next(tokens)
        n = len(s)
        f = sorted(list(Counter(s).values())+[0]*26, reverse=True)[:26]
        best = 0
        for d in range(1,27):
            if n%d == 0:
                target = n//d
                best = max(best, sum(min(c,target) for c in f[:d]))
        out.append(str(n-best))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
