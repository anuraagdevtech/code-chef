import sys
from bisect import bisect_left


def solve(tokens):
    n = next(tokens)
    first = [next(tokens) for _ in range(n)]
    first_color = [next(tokens) for _ in range(n)]
    second = [next(tokens) for _ in range(n)]
    second_color = [next(tokens) for _ in range(n)]
    active = set(second_color)
    groups = {}
    for value, color in zip(first, first_color):
        if color in active:
            groups.setdefault(color, []).append(value)
    for value, color in zip(second, second_color):
        groups.setdefault(color, []).append(value)
    for pool in groups.values():
        pool.sort()
    pointer = {}
    previous = -1
    ok = True
    for value, color in zip(first, first_color):
        if color in active:
            pool = groups[color]
            j = bisect_left(pool, previous, pointer.get(color, 0))
            if j == len(pool):
                ok = False
                break
            value = pool[j]
            pointer[color] = j + 1
        if value < previous:
            ok = False
            break
        previous = value
    return 'Yes' if ok else 'No'


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
