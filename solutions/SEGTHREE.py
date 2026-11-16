import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        cost = [[0] * 3 for _ in range(3)]
        for i in range(n):
            residue = next(tokens) % 3
            for v in range(3):
                cost[i % 3][v] += (v - residue) % 3
        best = min((cost[0][residue] + cost[1][b] + cost[2][(-residue - b) % 3] for residue in range(3) for b in range(3)))
        out.append(str(best))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
