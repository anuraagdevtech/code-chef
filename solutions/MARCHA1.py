import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,target = int(next(tokens)),int(next(tokens))
        reachable = 1
        mask = (1 << (target+1))-1
        for _ in range(n):
            value = int(next(tokens))
            if value <= target:
                reachable |= (reachable << value)&mask
        out.append('Yes' if reachable >> target&1 else 'No')
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
