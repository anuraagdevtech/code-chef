import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        rows = [next(tokens).decode() for _ in range(n)]
        difference = [row[:n//2].count('1')-row[n//2:].count('1') for row in rows]
        amounts = [abs(d) for d in difference]
        target = sum(amounts)//2
        mask = (1 << (target+1))-1
        reachable = 1
        history = [reachable]
        for value in amounts:
            reachable |= (reachable << value)&mask
            history.append(reachable)
        chosen = set()
        value = reachable.bit_length()-1
        for i in range(n-1,-1,-1):
            if not (history[i] >> value)&1:
                chosen.add(i)
                value -= amounts[i]
        for i,row in enumerate(rows):
            desired = -amounts[i] if i in chosen else amounts[i]
            out.append(row if difference[i] == desired else row[::-1])
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
