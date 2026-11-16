import sys


def main() -> None:
    values = list(map(int,sys.stdin.buffer.read().split()))
    queries = list(zip(values[1::2],values[2::2]))
    limit = max(r for _,r in queries)
    sums = [0]*(limit+1)
    for d in range(1,limit+1,2):
        for multiple in range(d,limit+1,d):
            sums[multiple] += d
    for n in range(1,limit+1):
        sums[n] += sums[n-1]
    sys.stdout.write('\n'.join(str(sums[r]-sums[l-1]) for l,r in queries)+'\n')

if __name__ == '__main__':
    main()
