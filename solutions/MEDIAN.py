import sys
from functools import lru_cache


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        values = [next(tokens) for _ in range(n)]
        largest = max(values)
        initial = sum((1 << i for i, x in enumerate(values) if x == largest))
        full = (1 << n) - 1

        @lru_cache(None)
        def solve(mask):
            if mask == full:
                return 0
            if mask.bit_count() * 2 >= n:
                return 1
            best = n
            candidates = set()
            for start in range(n):
                balance = 0
                right = -1
                for end in range(start, n):
                    balance += 1 if mask >> end & 1 else -1
                    if balance >= 0:
                        right = end
                if right >= start:
                    new = mask | (1 << right - start + 1) - 1 << start
                    if new != mask:
                        candidates.add(new)
            ordered = sorted(candidates, key=int.bit_count, reverse=True)
            kept = []
            for state in ordered:
                if any((state | other == other for other in kept)):
                    continue
                kept.append(state)
                best = min(best, 1 + solve(state))
                if best == 2:
                    break
            return best
        out.append(str(solve(initial)))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
