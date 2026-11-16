import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        chef = 0.0
        total = 0
        for _ in range(n):
            gold = next(tokens)
            chef_days = next(tokens)
            chefu_days = next(tokens)
            chef += gold * chefu_days / (chef_days + chefu_days)
            total += gold
        out.append(f'{chef:.10f} {total - chef:.10f}')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
