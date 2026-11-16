import sys
from math import gcd


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        a = [int(next(tokens)) for _ in range(n)]
        if n == 1:
            out.append('1')
            continue
        prefix = [0] * (n+1)
        suffix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = gcd(prefix[i], a[i])
        for i in range(n-1, -1, -1):
            suffix[i] = gcd(suffix[i+1], a[i])
        total = sum(a)
        out.append(str(min((total-v)//gcd(prefix[i], suffix[i+1])+1 for i,v in enumerate(a))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
