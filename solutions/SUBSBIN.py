import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        bits = next(tokens).decode()
        ones = bits.count('1')
        zeros = n - ones
        if min(ones, zeros) == 0:
            out.append(f'{n} 0')
            continue
        imbalance = abs(ones - zeros)
        minority = '0' if ones > zeros else '1'
        operations = []
        for _ in range(imbalance):
            i = next((i for i in range(len(bits) - 1) if bits[i] != bits[i + 1]))
            operations.append(f'{i + 1} {i + 2} {minority}')
            bits = bits[:i] + minority + bits[i + 2:]
        operations.append(f'1 {len(bits)} 0')
        out.append(f'1 {len(operations)}')
        out.extend(operations)
    print('\n'.join(out))


if __name__ == "__main__":
    main()
