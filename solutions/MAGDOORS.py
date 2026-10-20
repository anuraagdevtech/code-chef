import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        s = data[1 + i]
        waves = 0
        parity = 0
        for ch in s:
            # Effective state is the written digit flipped by the wave parity.
            if (ch - 48) ^ parity == 0:
                waves += 1
                parity ^= 1
        out.append(str(waves))
    sys.stdout.write("\n".join(out) + "\n")


main()
