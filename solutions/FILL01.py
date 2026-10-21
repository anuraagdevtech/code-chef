import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        k = int(data[2 + 3 * i])
        plan = data[3 + 3 * i]
        naps = 0
        # Leftovers cannot be pooled across runs, so divide each run alone.
        for run in plan.split(b"1"):
            naps += len(run) // k
        out.append(str(naps))
    sys.stdout.write("\n".join(out) + "\n")


main()
