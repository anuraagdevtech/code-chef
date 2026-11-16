import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,m = int(next(tokens)),int(next(tokens))
        size = n*m
        answer = []
        for step in range(1,size+1):
            each = (size-1)//step+1
            overlap = 0
            for index in range(0,size,step):
                row,col = divmod(index,m)
                overlap += (col*n+row)%step == 0
            answer.append(2*each-overlap)
        out.append(' '.join(map(str,answer)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
