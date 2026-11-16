import sys


def main():
    lines = iter(sys.stdin.buffer.read().splitlines())
    t = int(next(lines))
    out = []
    MOD = 1000000007
    for _ in range(t):
        n = int(next(lines))
        owners = [[] for _ in range(101)]
        for i in range(n):
            for shirt in map(int, next(lines).split()):
                owners[shirt].append(1 << i)
        ways = [0] * (1 << n)
        ways[0] = 1
        for people in owners:
            for mask in range((1 << n) - 1, -1, -1):
                if ways[mask]:
                    for bit in people:
                        if not mask & bit:
                            ways[mask | bit] = (ways[mask | bit] + ways[mask]) % MOD
        out.append(str(ways[-1]))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
