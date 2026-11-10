"""CodeChef STR_REVERSE — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        s = next(it)
        target = s[::-1]
        j = 0
        for c in s:
            if j < len(s) and c == target[j]:
                j += 1
        out.append(str(len(s)-j))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
