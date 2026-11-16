import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    beat = {'R': 'P', 'P': 'S', 'S': 'R'}
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        moves = next(tokens).decode()
        outcome = {c: c for c in 'RPS'}
        winners = []
        for c in reversed(moves):
            old = outcome.copy()
            for x in 'RPS':
                outcome[x] = old[c if beat[x] == c else x]
            winners.append(outcome[c])
        out.append(''.join(reversed(winners)))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
