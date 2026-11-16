import sys


def solve(tokens):
    n = next(tokens)
    values = [next(tokens) for _ in range(n)]
    bits = []
    total = [0] * 30
    for x in values:
        own_bits = []
        while x:
            z = x & -x
            k = z.bit_length() - 1
            own_bits.append(k)
            total[k] += 1
            x -= z
        bits.append(own_bits)
    active = sum((v > 0 for v in total))
    inside = [0] * 30
    have = bad = left = 0
    best = -1
    for right, own_bits in enumerate(bits):
        for k in own_bits:
            if inside[k] == 0:
                have += 1
            inside[k] += 1
            if inside[k] == total[k]:
                bad += 1
        while bad:
            for k in bits[left]:
                if inside[k] == total[k]:
                    bad -= 1
                inside[k] -= 1
                if not inside[k]:
                    have -= 1
            left += 1
        if have == active:
            best = max(best, right - left + 1)
    return str(best)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
