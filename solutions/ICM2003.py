import sys
import sys, math


def main() -> None:
    tokens = iter(map(float, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = []
    for _ in range(t):
        b = next(tokens)
        c = next(tokens)
        low = 0.0
        high = math.pi / 2
        for _ in range(55):
            x = (low + high) / 2
            if (2 * x + b) * math.sin(x) - (x * x + b * x + c) * math.cos(x) < 0:
                low = x
            else:
                high = x
        x = (low + high) / 2
        out.append(f'{(x * x + b * x + c) / math.sin(x):.10f}')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
