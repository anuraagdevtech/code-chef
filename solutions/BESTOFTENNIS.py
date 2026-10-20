import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # They stop the moment the winner clinches, so the winner's score is
        # exactly the majority (n + 1) // 2. The loser's score is irrelevant.
        out.append(str(2 * max(x, y) - 1))
    sys.stdout.write("\n".join(out) + "\n")


main()
