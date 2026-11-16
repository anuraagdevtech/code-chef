import sys


def solve(tokens):
    n, m = (next(tokens), next(tokens))
    queue = [next(tokens) - 1 for _ in range(m)]
    total = [0] * n
    for value in queue:
        total[value] += 1
    inside = [0] * n
    left = best = 0
    for right, value in enumerate(queue):
        inside[value] += 1
        while inside[value] == total[value]:
            inside[queue[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return str(m - best)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
