import sys


def solve(tokens):
    n = next(tokens)
    values = [next(tokens) for _ in range(n)]
    stack = []
    beauties = set()
    for value in values:
        while stack and stack[-1] <= value:
            beauties.add(value - stack.pop())
        if stack:
            beauties.add(stack[-1] - value)
        stack.append(value)
    return str(len(beauties))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
