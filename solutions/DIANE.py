import sys


def solve(tokens):
    target = next(tokens)
    quotient, remainder = divmod(target, 99998)
    result = []
    if quotient:
        result = [99999] * quotient + [100000]
    if remainder:
        if result:
            result.append(1)
        result.extend([remainder + 1, remainder + 2])
    if not result:
        result = [1]
    return str(len(result)) + '\n' + ' '.join(map(str, result))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
