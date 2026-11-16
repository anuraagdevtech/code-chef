import sys
from bisect import bisect_left


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        intervals = [(int(next(tokens)),int(next(tokens))) for _ in range(n)]
        difference = [0]*(n+2)
        for left,right in intervals:
            difference[left] += 1
            difference[right+1] -= 1
        valid = []
        coverage = 0
        for k in range(n+1):
            coverage += difference[k]
            if coverage == k:
                valid.append(k)
        count = len(valid)
        parent = list(range(count+1))
        def find(i):
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i
        last = count-1
        answer = []
        for left,right in intervals:
            first = find(0)
            if left <= valid[first] and valid[last] <= right:
                answer.append('1')
            else:
                answer.append('0')
                i = find(bisect_left(valid,left))
                while i < count and valid[i] <= right:
                    parent[i] = find(i+1)
                    i = find(i)
                while parent[last] != last:
                    last -= 1
        out.append(str(count%1000000007))
        out.append(''.join(answer))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
