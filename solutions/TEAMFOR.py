import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        prog, eng = data[2 + 3 * i], data[3 + 3 * i]
        both = only_p = only_e = none = 0
        for a, c in zip(prog, eng):
            if a == 0x31 and c == 0x31:
                both += 1
            elif a == 0x31:
                only_p += 1
            elif c == 0x31:
                only_e += 1
            else:
                none += 1
        # Specialist pairs first; they spend no all-rounder.
        teams = min(only_p, only_e)
        spare = abs(only_p - only_e) + none
        teams += both if spare >= both else spare + (both - spare) // 2
        out.append(str(teams))
    sys.stdout.write("\n".join(out) + "\n")


main()
