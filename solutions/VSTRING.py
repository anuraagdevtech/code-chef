import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        limit = int(next(tokens))
        bits = next(tokens).decode()
        ones = [i for i, v in enumerate(bits) if v == '1']
        if len(ones) < 2:
            out.append('YES')
            continue
        gaps = [ones[i] - ones[i - 1] - 1 for i in range(1, len(ones))] + [n + ones[0] - ones[-1] - 1]
        out.append('YES' if sum((g > limit for g in gaps)) <= 1 else 'NO')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
