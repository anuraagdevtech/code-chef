import sys


def solve(tokens):
    n, m = (next(tokens), next(tokens))
    college_rank = [next(tokens) for _ in range(n)]
    student_rank = [next(tokens) for _ in range(m)]
    prefs = []
    for _ in range(m):
        k = next(tokens)
        prefs.append([next(tokens) - 1 for _ in range(k)])
    used = set()
    for i in sorted(range(m), key=student_rank.__getitem__):
        choice = min((college for college in prefs[i] if college not in used), key=college_rank.__getitem__, default=-1)
        if i == 0:
            return str(choice + 1)
        if choice >= 0:
            used.add(choice)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
