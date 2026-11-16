import sys
from collections import Counter


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        s = next(tokens)
        f = Counter(s)
        pairs = sum(v//2 for v in f.values())
        odd = sum(v%2 for v in f.values())
        out.append('YES' if pairs >= max(1, odd) else 'NO')
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
