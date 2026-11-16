import sys


def solve(tokens):
    next(tokens)
    dishes = next(tokens)
    events = [(next(tokens), 0, next(tokens), 0) for _ in range(dishes)]
    clans = next(tokens)
    events += [(next(tokens), 1, next(tokens), next(tokens)) for _ in range(clans)]
    events.sort()
    need = 1
    for _, kind, first, second in reversed(events):
        if kind == 0:
            need += first
        else:
            need = min(need, max(first, need - second))
    return str(need)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
