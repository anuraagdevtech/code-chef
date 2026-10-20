import sys

FLIP = {"Left": "Right", "Right": "Left"}


def main() -> None:
    lines = sys.stdin.read().split("\n")
    idx = 0
    t = int(lines[idx].strip()); idx += 1
    out = []
    for _ in range(t):
        n = int(lines[idx].strip()); idx += 1
        turns, roads = [], []
        for _ in range(n):
            # Road names contain spaces, so split on the first " on " only.
            turn, road = lines[idx].strip().split(" on ", 1)
            idx += 1
            turns.append(turn)
            roads.append(road)
        out.append(f"Begin on {roads[-1]}")
        # Turn i entered road i on the way out; coming back it leads to i - 1.
        for i in range(n - 1, 0, -1):
            out.append(f"{FLIP[turns[i]]} on {roads[i - 1]}")
        out.append("")                 # blank line after every test case
    sys.stdout.write("\n".join(out) + "\n")


main()
