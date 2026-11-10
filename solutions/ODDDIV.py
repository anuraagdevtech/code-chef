"""CodeChef ODDDIV — standalone Python 3 solution."""
import sys


limit = 100000
values = [0]*(limit+1)
for d in range(1,limit+1,2):
    for multiple in range(d,limit+1,d):
        values[multiple] += d
pref = [0]*(limit+1)
for i in range(1,limit+1):
    pref[i] = pref[i-1]+values[i]


def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        l,r = int(next(it)),int(next(it))
        out.append(str(pref[r]-pref[l-1]))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
