import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + 2 * i])
        s = data[2 + 2 * i]
        odd_ones = sum(1 for j in range(0, n, 2) if s[j] == 0x31)
        even_ones = sum(1 for j in range(1, n, 2) if s[j] == 0x31)
        odd_zeros = (n + 1) // 2 - odd_ones
        even_zeros = n // 2 - even_ones
        # Type A edges pair an odd zero with an even one; type B the reverse.
        a = min(odd_zeros, even_ones)
        b = min(even_zeros, odd_ones)
        half = n // 2
        if n % 2 == 0 and a < half:
            # The path's perfect matching is unique and all type A.
            out.append(str(min(a + b, half - 1)))
        else:
            out.append(str(min(a + b, half)))
    sys.stdout.write("\n".join(out) + "\n")


main()
