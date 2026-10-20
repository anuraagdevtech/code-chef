import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x = int(data[1 + i])
        # Output is case sensitive, so the capitalisation here matters.
        out.append("Easy" if x < 100 else "Medium" if x < 200 else "Hard")
    sys.stdout.write("\n".join(out) + "\n")


main()
