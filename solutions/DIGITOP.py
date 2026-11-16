import sys
from collections import Counter


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n, budget = int(next(tokens)), int(next(tokens))
        a = [next(tokens) for _ in range(n)]
        b = [next(tokens) for _ in range(n)]
        if any(len(x) != len(y) for x,y in zip(a,b)):
            out.append('NO')
            continue
        source = Counter(digit for word in a for digit in word)
        target = Counter(digit for word in b for digit in word)
        needed = sum(max(0, count-source[digit]) for digit,count in target.items())
        out.append('YES' if needed <= budget else 'NO')
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
