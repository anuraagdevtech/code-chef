import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        k = next(tokens)
        target = next(tokens)
        digits = []
        ok = True
        for i in range(n):
            residue = target % k
            if residue == 0:
                digit = 0
            elif residue == 1:
                digit = 1
            elif residue == k - 1:
                digit = -1
            else:
                ok = False
                digit = 0
            digits.append(digit)
            target = (target - digit) // k
        out.append(' '.join(map(str, digits)) if ok and target == 0 else '-2')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
