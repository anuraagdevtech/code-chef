import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        values = [next(tokens) for _ in range(n)]
        candidates = {0, 1, n - 1}
        if n > 2:
            step = values[1] - values[0]
            for i in range(2, n):
                if values[i] - values[i - 1] != step:
                    candidates.update((i - 1, i))
                    break
        valid = []
        for skip in candidates:
            rest = [x for i, x in enumerate(values) if i != skip]
            if len(rest) < 3 or all((rest[i] - rest[i - 1] == rest[1] - rest[0] for i in range(2, len(rest)))):
                valid.append(values[skip])
        out.append(str(min(valid, default=-1)))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
