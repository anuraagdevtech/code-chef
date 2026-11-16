import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        k = next(tokens)
        ranges = [(next(tokens), next(tokens)) for _ in range(n)]
        diff = [0] * 100002
        for l, r in ranges:
            diff[l] += 1
            diff[r + 1] -= 1
        height = base_count = 0
        score = [0] * 100001
        for i in range(1, 100001):
            height += diff[i]
            base_count += height == k
            score[i] = score[i - 1] + (height == k + 1) - (height == k)
        out.append(str(base_count + max((score[r] - score[l - 1] for l, r in ranges))))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
