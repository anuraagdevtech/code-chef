"""CodeChef CAB — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n, k = int(next(it)), int(next(it))
        counts = [(k >> i) & 1 for i in range(26)]
        needed = sum(counts)
        if needed > n or n > k:
            out.append('-1')
            continue
        for i in range(25, 0, -1):
            split = min(counts[i], n-needed)
            counts[i] -= split
            counts[i-1] += 2*split
            needed += split
        out.append(''.join(chr(97+i)*c for i,c in enumerate(counts)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
