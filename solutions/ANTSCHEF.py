import sys
from collections import Counter


def solve(tokens):
    n = next(tokens)
    lines = []
    distance_count = Counter()
    for _ in range(n):
        k = next(tokens)
        coords = [next(tokens) for _ in range(k)]
        lines.append(coords)
        distance_count.update((abs(coord) for coord in coords))
    collisions = sum((v > 1 for v in distance_count.values()))
    for coords in lines:
        negative_left = sum((coord < 0 for coord in coords))
        positive_left = len(coords) - negative_left
        for coord in sorted(coords, key=abs):
            if coord < 0:
                negative_left -= 1
            else:
                positive_left -= 1
            if distance_count[abs(coord)] > 1:
                collisions += negative_left if coord < 0 else positive_left
            else:
                collisions += positive_left if coord < 0 else negative_left
    return str(collisions)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
