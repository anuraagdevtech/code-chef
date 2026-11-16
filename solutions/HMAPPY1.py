import sys
from collections import deque


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    n, q, k = (int(next(tokens)) for _ in range(3))
    bits = [int(next(tokens)) for _ in range(n)]
    queries = next(tokens)
    bits += bits
    starts = [0] * len(bits)
    run = 0
    for i, x in enumerate(bits):
        run = run + 1 if x else 0
        starts[i] = i - run + 1
    window = deque()
    answers = []
    for i, x in enumerate(bits):
        length = i - starts[i] + 1 if x else 0
        while window and window[-1][1] <= length:
            window.pop()
        window.append((i, length))
        left = i - n + 1
        while window and window[0][0] < left:
            window.popleft()
        if left >= 0:
            while len(window) > 1 and min(window[0][1], window[0][0] - left + 1) <= window[1][1]:
                window.popleft()
            answers.append(min(k, window[0][1], window[0][0] - left + 1))
    start = 0
    out = []
    for ch in queries:
        if ch == 33:
            start = (start - 1) % n
        else:
            out.append(str(answers[start]))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
