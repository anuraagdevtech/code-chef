import sys


def main():
    operations, state, mul, add = map(int, sys.stdin.buffer.read().split())
    bits = bytearray(1 << 28)
    total = 0
    for _ in range(operations):
        number = state >> 1
        byte = number >> 3
        mask = 1 << (number & 7)
        present = bits[byte] & mask
        if state & 1:
            if not present:
                bits[byte] |= mask
                total += number
        elif present:
            bits[byte] ^= mask
            total -= number
        state = mul * state + add & 4294967295
    print(total)


if __name__ == "__main__":
    main()
