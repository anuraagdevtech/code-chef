import sys
import heapq


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    n, k = (next(tokens), next(tokens))
    values = [next(tokens) for _ in range(n)]
    prefix = [0]
    for x in values:
        prefix.append(prefix[-1] + x)
    heap = [(-(prefix[n] - prefix[i]), i, n) for i in range(n)]
    heapq.heapify(heap)
    out = []
    for _ in range(k):
        negated, left, right = heapq.heappop(heap)
        out.append(str(-negated))
        if right - 1 > left:
            heapq.heappush(heap, (-(prefix[right - 1] - prefix[left]), left, right - 1))
    print(' '.join(out))


if __name__ == "__main__":
    main()
