import sys
from collections import Counter


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        freq = Counter(int(next(tokens)) for _ in range(n))
        answer = 1
        for f in freq.values():
            answer = answer * (f+1) % 1000000007
        out.append(str((answer-1) % 1000000007))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
