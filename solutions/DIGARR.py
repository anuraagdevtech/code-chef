import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        # data[pos] is D, which Python does not need.
        s = data[pos + 1]
        pos += 2
        # Divisible by 5 iff some digit can be moved to the last position.
        out.append("Yes" if b"0" in s or b"5" in s else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
