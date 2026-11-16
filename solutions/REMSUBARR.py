import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        perm = [next(tokens) for _ in range(n)]
        position = [0] * (n + 1)
        for i, value in enumerate(perm):
            position[value] = i
        leftmost = rightmost = position[n]
        best = 1
        for value in range(n - 1, 1, -1):
            leftmost = min(leftmost, position[value])
            rightmost = max(rightmost, position[value])
            if rightmost - leftmost + 1 == n - value + 1:
                best = n - value + 1
        out.append(str(best))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
