import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    s1 = s2 = 0
    best_lead, best_player = 0, 1
    for i in range(n):
        s1 += int(data[1 + 2 * i])
        s2 += int(data[2 + 2 * i])
        # The lead is measured on cumulative totals, not the round's scores.
        lead = abs(s1 - s2)
        if lead > best_lead:
            best_lead = lead
            best_player = 1 if s1 > s2 else 2
    print(best_player, best_lead)


main()
