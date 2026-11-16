import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    MOD = 7051954
    for _ in range(int(next(tokens))):
        n, length, start, target = (int(next(tokens)) for _ in range(4))
        master = next(tokens)
        low = max(0, start - n)
        high = min(length, start + n)
        ways = [0] * (high - low + 1)
        ways[start - low] = 1
        last = {}
        for ch in master:
            step = 1 if ch == 43 else -1
            created = [0] * len(ways)
            if step == 1:
                for j in range(1, len(ways)):
                    created[j] = ways[j - 1]
            else:
                for j in range(len(ways) - 1):
                    created[j] = ways[j + 1]
            old = last.get(ch)
            for j in range(len(ways)):
                ways[j] = (ways[j] + created[j] - (old[j] if old else 0)) % MOD
            last[ch] = created
        out.append(str(ways[target - low] if low <= target <= high else 0))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
