import sys
import heapq


spf = list(range(1000001))
for i in range(2, 1001):
    if spf[i] == i:
        for j in range(i * i, 1000001, i):
            if spf[j] == j:
                spf[j] = i


def solve(tokens):
    n = next(tokens)
    values = sorted((next(tokens) for _ in range(n)))
    heaps = {}

    def factors(number):
        while number > 1:
            prime = spf[number]
            yield prime
            while number % prime == 0:
                number //= prime
    for i, number in enumerate(values):
        for prime in factors(number):
            heaps.setdefault(prime, []).append(i)
    alive = bytearray(b'\x01') * n
    first_alive = 0
    out = []
    q = next(tokens)
    for _ in range(q):
        number = next(tokens)
        best = n
        for prime in factors(number):
            heap = heaps.get(prime)
            if heap:
                while heap and (not alive[heap[0]]):
                    heapq.heappop(heap)
                if heap:
                    best = min(best, heap[0])
        if best == n:
            while not alive[first_alive]:
                first_alive += 1
            best = first_alive
        alive[best] = 0
        out.append(str(values[best]))
    return ' '.join(out)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
