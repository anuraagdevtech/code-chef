"""CodeChef BYTEISLE — standalone Python 3 solution."""
import sys
from bisect import bisect_left,bisect_right



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n = int(next(it))
        intervals = [(int(next(it)),int(next(it))) for _ in range(n)]
        diff = [0]*(n+2)
        for l,r in intervals:
            diff[l] += 1
            diff[r+1] -= 1
        active = 0
        candidates = []
        for k in range(n+1):
            active += diff[k]
            if active == k:
                candidates.append(k)
        size = len(candidates)
        out.append(str(size))
        bit = [0]+[(i & -i) for i in range(1,size+1)]
        successor = list(range(size+1))
        def find(x):
            while successor[x] != x:
                successor[x] = successor[successor[x]]
                x = successor[x]
            return x
        def prefix(x):
            total = 0
            while x:
                total += bit[x]
                x -= x & -x
            return total
        remaining = size
        answer = []
        for l,r in intervals:
            left,right = bisect_left(candidates,l),bisect_right(candidates,r)
            count = prefix(right)-prefix(left)
            if count == remaining:
                answer.append('1')
            else:
                answer.append('0')
                idx = find(left)
                while idx < right:
                    remaining -= 1
                    j = idx+1
                    while j <= size:
                        bit[j] -= 1
                        j += j & -j
                    successor[idx] = find(idx+1)
                    idx = find(idx)
        out.append(''.join(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
