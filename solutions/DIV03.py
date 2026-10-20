import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        a = [int(v) for v in data[pos:pos + 10]]     # difficulties 1..10
        k = int(data[pos + 10])
        pos += 11
        answer = 1
        for d in range(10, 0, -1):
            count = a[d - 1]
            if count == 0:
                continue            # empty tiers are free and never the answer
            if count <= k:
                k -= count
                continue
            answer = d              # budget runs out here, so this tier stays
            break
        out.append(str(answer))
    sys.stdout.write("\n".join(out) + "\n")


main()
