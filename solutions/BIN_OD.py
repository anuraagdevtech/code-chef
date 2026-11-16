import sys
from collections import defaultdict


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n, q = int(next(tokens)), int(next(tokens))
        a = [int(next(tokens)) for _ in range(n)]
        groups = defaultdict(list)
        for index in range(q):
            bit, l1, r1, l2, r2 = (int(next(tokens)) for _ in range(5))
            groups[bit].append((index,l1,r1,l2,r2))
        answer = [0]*q
        for bit, queries in groups.items():
            prefix = [0]*(n+1)
            for i, value in enumerate(a):
                prefix[i+1] = prefix[i]+((value >> bit)&1)
            for index,l1,r1,l2,r2 in queries:
                ones1 = prefix[r1]-prefix[l1-1]
                ones2 = prefix[r2]-prefix[l2-1]
                answer[index] = ones1*(r2-l2+1-ones2)+(r1-l1+1-ones1)*ones2
        out.extend(map(str, answer))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
