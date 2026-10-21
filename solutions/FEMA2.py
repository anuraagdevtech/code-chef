import sys
from collections import deque


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        row = data[pos + 2]
        pos += 3
        matched = 0
        sheets = 0
        magnets, irons = deque(), deque()
        for idx in range(n):
            cell = row[idx]
            if cell == 0x58:              # 'X' cuts the row into blocks
                magnets.clear()
                irons.clear()
                continue
            if cell == 0x3A:              # ':' costs the same as one cell
                sheets += 1
                continue
            if cell == 0x5F:              # '_'
                continue
            # Distance plus sheets between two pieces is a difference of these.
            w = idx + 1 + sheets
            if cell == 0x4D:              # 'M'
                while irons and w - irons[0] > k:
                    irons.popleft()
                if irons:
                    irons.popleft()       # oldest == window expires soonest
                    matched += 1
                else:
                    magnets.append(w)
            else:                         # 'I'
                while magnets and w - magnets[0] > k:
                    magnets.popleft()
                if magnets:
                    magnets.popleft()
                    matched += 1
                else:
                    irons.append(w)
        out.append(str(matched))
    sys.stdout.write("\n".join(out) + "\n")


main()
