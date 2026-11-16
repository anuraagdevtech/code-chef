import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(tokens)
    taste = [next(tokens) for _ in range(n)]
    out = []
    for _ in range(next(tokens)):
        k = next(tokens)
        values = []
        for x in taste:
            t = next(tokens)
            if t:
                values.append(t * x)
        if k > len(values):
            out.append('0')
            continue
        if k == 1:
            out.append(str(sum(values)))
            continue
        prefix = [0]
        for x in values:
            prefix.append(prefix[-1] + x)
        count = len(values)
        answer = 0
        for bit in range(prefix[-1].bit_length() - 1, -1, -1):
            mask = answer | 1 << bit
            reachable = [0] * (count + 1)
            reachable[0] = 1
            for right in range(1, count + 1):
                possibilities = 0
                for left in range(right):
                    if prefix[right] - prefix[left] & mask == mask:
                        possibilities |= reachable[left] << 1
                reachable[right] = possibilities
            if reachable[count] >> k & 1:
                answer = mask
        out.append(str(answer))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
