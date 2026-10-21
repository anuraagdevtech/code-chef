import sys


def main() -> None:
    s = sys.stdin.buffer.read().strip()
    waiting_c = waiting_h = waiting_e = 0
    moves = 0
    for ch in s:
        if ch == 0x43:                 # 'C'
            waiting_c += 1
        elif ch == 0x48 and waiting_c:  # 'H'
            waiting_c -= 1
            waiting_h += 1
        elif ch == 0x45 and waiting_h:  # 'E'
            waiting_h -= 1
            waiting_e += 1
        elif ch == 0x46 and waiting_e:  # 'F'
            waiting_e -= 1
            moves += 1
    sys.stdout.write(f"{moves}\n")


main()
