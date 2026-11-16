import sys


def solve(tokens):
    n = next(tokens)
    tagged = []
    floor_value = 0
    for i in range(n):
        a, b = (next(tokens), next(tokens))
        tagged.extend(((a, i), (b, i)))
        floor_value = max(floor_value, min(a, b))
    tagged.sort()
    best = 10 ** 30
    for j, (value, i) in enumerate(tagged):
        if value < floor_value:
            continue
        k = j - 1
        while k >= 0 and tagged[k][1] == i:
            k -= 1
        if k >= 0:
            best = min(best, value - tagged[k][0])
    return str(best)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
