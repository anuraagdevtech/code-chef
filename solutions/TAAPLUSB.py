import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        answer = n/2 - (1 - 10.0**(-n))/18
        out.append(f'{answer:.10f}')
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
