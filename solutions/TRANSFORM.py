import sys

# The cycle normal -> huge -> small -> normal, written from the start state.
CYCLE = ("NORMAL", "HUGE", "SMALL")


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = [CYCLE[int(data[1 + i]) % 3] for i in range(t)]
    sys.stdout.write("\n".join(out) + "\n")


main()
