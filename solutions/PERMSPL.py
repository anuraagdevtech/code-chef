import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        p = [int(next(tokens)) for _ in range(n)]
        degree = [0]*n
        inversions = 0
        for i in range(n):
            for j in range(i+1,n):
                if p[i] > p[j]:
                    degree[i] += 1
                    degree[j] += 1
                    inversions += 1
        reachable = 1
        mask = (1 << (inversions+1))-1
        for d in degree:
            reachable |= (reachable << d)&mask
        out.append('YES' if reachable >> inversions&1 else 'NO')
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
