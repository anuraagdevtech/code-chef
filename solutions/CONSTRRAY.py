import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for tok in data[1:1 + t]:
        n = int(tok)
        if n % 2:
            # D_{N-i} = D_i forces i and N-i to share parity.
            out.append("-1")
            continue
        half = n // 2
        front = [1] + [2 if i % 2 else -2 for i in range(2, half + 1)]
        out.append(" ".join(map(str, front + [0] * half)))
    sys.stdout.write("\n".join(out) + "\n")


main()
