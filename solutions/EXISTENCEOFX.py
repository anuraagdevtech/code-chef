import sys


def solve(tokens):
    a, b, c = (next(tokens), next(tokens), next(tokens))
    carry = 0
    for position in range(29):
        bit_a = a >> position & 1
        bit_b = b >> position & 1
        bit_c = c >> position & 1
        x = bit_a ^ bit_b ^ bit_c ^ carry
        carry = (bit_a ^ x) + (bit_b ^ x) + carry >> 1
    return 'YES' if carry == 0 else 'NO'


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
