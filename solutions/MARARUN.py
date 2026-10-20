import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        d_days, d_km, a, b, c = map(int, data[1 + 5 * i:6 + 5 * i])
        total = d_days * d_km
        # Prizes increase with distance, so take the longest race he can finish.
        out.append(str(c if total >= 42 else b if total >= 21 else a if total >= 10 else 0))
    sys.stdout.write("\n".join(out) + "\n")


main()
