import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(tokens)
    next(tokens)
    seniority = [next(tokens) for _ in range(n)]
    stack = []
    product = 1
    for i in range(n - 1, -1, -1):
        while stack and seniority[stack[-1]] >= seniority[i]:
            stack.pop()
        if stack:
            product = product * (stack[-1] - i + 1) % 1000000007
        stack.append(i)
    print(product)


if __name__ == "__main__":
    main()
