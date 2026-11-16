import sys
from collections import Counter


def solve(tokens):
    n, limit = (int(next(tokens)), int(next(tokens)))
    left = Counter(next(tokens).decode())
    chars = sorted(left)
    out = []
    if max(left.values()) - min(left.values()) > limit:
        return '-1'
    for _ in range(n):
        largest = max(left.values())
        for char in chars:
            if left[char] and largest - (left[char] - 1) <= limit:
                left[char] -= 1
                out.append(char)
                break
    return ''.join(out)


if __name__ == "__main__":
    tokens = iter(sys.stdin.buffer.read().split())
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
