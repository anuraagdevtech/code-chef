import sys


def solve(tokens):
    text = next(tokens).decode()
    n = len(text)
    seen = set()
    base = n + 1
    for left in range(n):
        ones = odd_zeros = 0
        for right in range(left, n):
            if text[right] == '1':
                ones += 1
            elif ones & 1:
                odd_zeros += 1
            seen.add(((right - left + 1) * base + ones) * base + odd_zeros)
    return str(len(seen))


if __name__ == "__main__":
    tokens = iter(sys.stdin.buffer.read().split())
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
