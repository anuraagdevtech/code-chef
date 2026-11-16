import sys
import heapq


def solve(tokens):
    n = next(tokens)
    values = [next(tokens) for _ in range(n)]
    seen = set(values)
    mex = 0
    while mex in seen:
        mex += 1
    MOD = 1000000007
    if mex == 0:
        return str(pow(2, n - 1, MOD))
    last = [-1] * mex
    heap = [(-1, value) for value in range(mex)]
    heapq.heapify(heap)
    prefix = [1]
    ways = 0
    for i, value in enumerate(values):
        if value < mex:
            last[value] = i
            heapq.heappush(heap, (i, value))
        while heap[0][0] != last[heap[0][1]]:
            heapq.heappop(heap)
        limit = heap[0][0]
        ways = prefix[limit] if limit >= 0 else 0
        prefix.append((prefix[-1] + ways) % MOD)
    return str(ways)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
