import sys


def solve(tokens):
    black, white = (next(tokens), next(tokens))
    n = black + white
    if n == 1:
        return 'B' if black else 'W'
    if not black or not white:
        return '-1'
    if white >= 2:
        colors = 'B' * black + 'W' * white
    else:
        colors = 'W' + 'B' * black
    return colors + '\n' + '\n'.join(('1 ' + str(i) for i in range(2, n + 1)))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
