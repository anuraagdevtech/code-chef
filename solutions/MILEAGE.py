import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x, y, a, b = map(int, data[1 + 5 * i:6 + 5 * i])
        # Cost is n*x/a vs n*y/b; n cancels, then cross-multiply to stay exact.
        petrol, diesel = x * b, y * a
        out.append("PETROL" if petrol < diesel else "DIESEL" if diesel < petrol else "ANY")
    sys.stdout.write("\n".join(out) + "\n")


main()
