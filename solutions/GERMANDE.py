import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        states, width = (next(tokens), next(tokens))
        n = states * width
        votes = [next(tokens) for _ in range(n)]
        votes += votes[:width]
        wins = [0] * width
        ones = sum(votes[:width])
        for i in range(n):
            wins[i % width] += ones > width // 2
            ones += votes[i + width] - votes[i]
        out.append(str(int(max(wins) > states // 2)))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
