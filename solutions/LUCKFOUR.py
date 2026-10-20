import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    # Counting on the text avoids a digit loop and its n = 0 edge case.
    out = [str(data[1 + i].count(b"4")) for i in range(t)]
    sys.stdout.write("\n".join(out) + "\n")


main()
