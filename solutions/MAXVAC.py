import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        need = int(next(tokens))
        calendar = next(tokens).decode()
        runs = [len(v) for v in calendar.split('1')]
        base = sum((v // need for v in runs))
        gain = max([0] + [(runs[i] + runs[i + 1] + 1) // need - runs[i] // need - runs[i + 1] // need for i in range(len(runs) - 1)])
        out.append(str(base + gain))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
