import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        k = int(next(tokens))
        bits = next(tokens).decode()
        seeds = [i for i in range(n) if bits[i] == '0' and (i and bits[i - 1] == '1' or (i + 1 < n and bits[i + 1] == '1'))]
        if not seeds:
            out.append('0' * n)
            continue
        k -= 1
        distance = [n + 1] * n
        last = -2 * n
        for i in range(n):
            if bits[i] == '0' and (i and bits[i - 1] == '1' or (i + 1 < n and bits[i + 1] == '1')):
                last = i
            distance[i] = i - last
        last = 3 * n
        for i in range(n - 1, -1, -1):
            if bits[i] == '0' and (i and bits[i - 1] == '1' or (i + 1 < n and bits[i + 1] == '1')):
                last = i
            distance[i] = min(distance[i], last - i)
        out.append(''.join(('1' if v <= k and (k - v) % 2 == 0 else '0' for v in distance)))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
