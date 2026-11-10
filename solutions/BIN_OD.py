"""CodeChef BIN_OD — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n, q = int(next(it)), int(next(it))
        a = [int(next(it)) for _ in range(n)]
        groups = {}
        answers = [0]*q
        for idx in range(q):
            k, l1, r1, l2, r2 = (int(next(it)) for _ in range(5))
            groups.setdefault(k, []).append((idx,l1,r1,l2,r2))
        for k, queries in groups.items():
            pref = [0]*(n+1)
            count = 0
            for i, x in enumerate(a, 1):
                count += (x >> k) & 1
                pref[i] = count
            for idx,l1,r1,l2,r2 in queries:
                x, y = pref[r1]-pref[l1-1], pref[r2]-pref[l2-1]
                answers[idx] = x*(r2-l2+1-y) + y*(r1-l1+1-x)
        out.extend(map(str, answers))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
