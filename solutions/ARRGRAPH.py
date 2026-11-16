import sys
from math import gcd


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        a = [int(next(tokens)) for _ in range(n)]
        seen = [False]*n
        seen[0] = True
        stack = [0]
        while stack:
            u = stack.pop()
            for v in range(n):
                if not seen[v] and gcd(a[u],a[v]) == 1:
                    seen[v] = True
                    stack.append(v)
        changes = 0
        if not all(seen):
            changes = 1
            a[0] = 43 if 47 in a else 47
        out.append(str(changes))
        out.append(' '.join(map(str,a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
