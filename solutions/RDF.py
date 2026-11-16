import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    cases = [(next(tokens), next(tokens)) for _ in range(next(tokens))]
    largest = max((n for n, k in cases), default=0)
    by_steps = {}
    answers = [0.0] * len(cases)
    for i, (n, k) in enumerate(cases):
        if k < 70:
            by_steps.setdefault(k, []).append((i, n))
    expected = [float(i) for i in range(largest + 1)]
    for k in range(min(69, max(by_steps, default=0)) + 1):
        for i, n in by_steps.get(k, []):
            answers[i] = expected[n]
        total = 0.0
        next_expected = [0.0] * (largest + 1)
        for n in range(1, largest + 1):
            total += expected[n - 1]
            next_expected[n] = total / n
        expected = next_expected
    print('\n'.join(('%.10f' % x for x in answers)))


if __name__ == "__main__":
    main()
