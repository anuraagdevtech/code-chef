import sys
from collections import Counter


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    while True:
        n = int(next(tokens))
        if n == 0:
            break
        columns = {}
        pairs = Counter()
        answer = 0
        for _ in range(n):
            x, y = int(next(tokens)), int(next(tokens))
            if x in columns:
                key = tuple(sorted((columns[x], y)))
                answer += pairs[key]
                pairs[key] += 1
            else:
                columns[x] = y
        out.append(str(answer))
    sys.stdout.write('\n'.join(out)+'\n')

if __name__ == '__main__':
    main()
