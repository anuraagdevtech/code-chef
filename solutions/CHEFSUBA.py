import sys
from collections import deque


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    n, k, q = (int(next(tokens)) for _ in range(3))
    k = min(k, n)
    bits = [int(next(tokens)) for _ in range(n)]
    queries = next(tokens)
    bits += bits
    prefix = [0]
    for x in bits:
        prefix.append(prefix[-1] + x)
    frame_sum = [prefix[i + k] - prefix[i] for i in range(2 * n - k + 1)]
    width = n - k + 1
    window = deque()
    answers = []
    for i, x in enumerate(frame_sum):
        while window and frame_sum[window[-1]] <= x:
            window.pop()
        window.append(i)
        while window[0] <= i - width:
            window.popleft()
        if i >= width - 1:
            answers.append(frame_sum[window[0]])
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
