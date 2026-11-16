import sys


def solve(tokens):
    n, m = (next(tokens), next(tokens))
    wanted = [next(tokens) for _ in range(n)]
    result = []
    used = set()
    unused = set(range(1, m + 1))
    for want in wanted:
        if not unused:
            unused = set(range(1, m + 1))
            used.clear()
        if want in unused:
            pick = want
            unused.remove(pick)
        else:
            pick = unused.pop()
        used.add(pick)
        result.append(pick)
    return ' '.join(map(str, result))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
