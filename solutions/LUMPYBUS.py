import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, ones, twos = int(data[pos]), int(data[pos + 1]), int(data[pos + 2])
        amounts = sorted(int(x) for x in data[pos + 3:pos + 3 + n])
        pos += 3 + n
        served = 0
        for a in amounts:
            # Maximising the twos minimises the ones needed, so one try decides.
            use_two = min(twos, a // 2)
            need_one = a - 2 * use_two
            if need_one > ones:
                continue
            twos -= use_two
            ones -= need_one
            served += 1
        out.append(str(served))
    sys.stdout.write("\n".join(out) + "\n")


main()
