"""CodeChef SEGDIR — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n = int(next(it))
        groups = {}
        for _ in range(n):
            l, r, speed = int(next(it)), int(next(it)), int(next(it))
            groups.setdefault(speed,[]).extend(((l,0),(r,1)))
        valid = True
        for events in groups.values():
            active = 0
            for _, kind in sorted(events):
                active += 1 if kind == 0 else -1
                if active > 2:
                    valid = False
        out.append('YES' if valid else 'NO')
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
