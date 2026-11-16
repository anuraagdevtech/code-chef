import sys


def solve(tokens):
    n, m = (next(tokens), next(tokens))
    posts = [next(tokens) for _ in range(n)]
    points = [0] + sorted(posts) + [m]
    index_of = {post: i for i, post in enumerate(points)}
    left = [i - 1 for i in range(n + 2)]
    right = [i + 1 for i in range(n + 2)]
    best = max((points[i + 1] - points[i] for i in range(n + 1)))
    out = []
    for post in reversed(posts):
        out.append(best)
        i = index_of[post]
        l, r = (left[i], right[i])
        best = max(best, points[r] - points[l])
        right[l] = r
        left[r] = l
    return ' '.join(map(str, reversed(out)))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
