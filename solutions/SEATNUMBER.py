import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        deck = "Lower" if n <= 15 else "Upper"
        # Offset inside the deck, 1..15; the layout repeats per deck.
        p = (n - 1) % 15 + 1
        kind = "Double" if p <= 10 else "Single"
        out.append(f"{deck} {kind}")
    sys.stdout.write("\n".join(out) + "\n")


main()
