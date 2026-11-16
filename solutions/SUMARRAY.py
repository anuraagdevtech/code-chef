import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        k = next(tokens)
        half = n // 2
        smallest = 3 * half
        largest = 199999 * half
        if k < smallest or k > largest or (k - smallest) % 2:
            out.append('-1')
            continue
        result = [1] * half + [2] * half
        steps = (k - smallest) // 2
        for i in range(n):
            take = min(steps, 49999)
            result[i] += 2 * take
            steps -= take
        out.append(' '.join(map(str, result)))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
