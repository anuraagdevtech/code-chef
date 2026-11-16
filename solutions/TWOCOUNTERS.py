import sys


def solve(tokens):
    n, m = (next(tokens), next(tokens))
    times = [next(tokens) for _ in range(m)]
    types = [next(tokens) for _ in range(m)]
    events = dict(zip(times, types))
    NEG = -10 ** 9
    best = [NEG, NEG, 0, NEG, NEG]
    for minute in range(1, n + 1):
        best = [best[1], max(best[0], best[2]), max(best[1], best[3]), max(best[2], best[4]), best[3]]
        kind = events.get(minute)
        if kind == 1:
            best = [NEG, NEG, max(best[:3]), best[3] + 1, best[4] + 1]
        elif kind == 2:
            best = [best[0] + 1, best[1] + 1, max(best[2:]), NEG, NEG]
    return str(max(best))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    minute = int(next(tokens))
    out = [solve(tokens) for _ in range(minute)]
    sys.stdout.write('\n'.join(out))
