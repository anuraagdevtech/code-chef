import sys


def leaders_upto(n: int) -> int:
    """Count of j in [1, n] with j = 1 (mod 5) - the block leaders."""
    return (n + 4) // 5 if n >= 1 else 0


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, k = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Shifting down only moves someone who starts a block of five.
        out.append(str(leaders_upto(n) - leaders_upto(k)))
    sys.stdout.write("\n".join(out) + "\n")


main()
