import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    MOD = 1000000007
    transition = ({49: 0, 50: 1}, {50: 2}, {49: 0})
    for _ in range(int(next(tokens))):
        first, second = (next(tokens), next(tokens))
        ways = {(0, 0): 1}
        for x, y in zip(first[:-1], second[:-1]):
            next_ways = {}
            for (u, v), count in ways.items():
                for c, d in ((x, y), (y, x)):
                    if c in transition[u] and d in transition[v]:
                        state = (transition[u][c], transition[v][d])
                        next_ways[state] = (next_ways.get(state, 0) + count) % MOD
            ways = next_ways
        out.append(str(ways.get((0, 0), 0) * 2 % MOD))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
