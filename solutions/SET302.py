"""CodeChef SET302 — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n, h = int(next(it)), int(next(it))
        a = [int(next(it)) for _ in range(n)]
        lo, hi = max(1, (sum(a)+h-1)//h), max(a)
        while lo < hi:
            mid = (lo+hi)//2
            if sum((x+mid-1)//mid for x in a) <= h:
                hi = mid
            else:
                lo = mid+1
        out.append(str(lo))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
