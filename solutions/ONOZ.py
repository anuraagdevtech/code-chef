import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        h, m = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        count = 0
        for hour in range(h):
            hs = str(hour)                 # no leading zeros, as displayed
            for minute in range(m):
                s = hs + str(minute)
                if s.count(s[0]) == len(s):
                    count += 1
        out.append(str(count))
    sys.stdout.write("\n".join(out) + "\n")


main()
