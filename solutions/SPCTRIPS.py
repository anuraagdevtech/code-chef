import sys


def main() -> None:
    values = list(map(int,sys.stdin.buffer.read().split()))
    limit = max(values[1:])
    divisor_prefix = [0]*(limit+1)
    for d in range(1,limit+1):
        for multiple in range(d,limit+1,d):
            divisor_prefix[multiple] += 1
    for i in range(1,limit+1):
        divisor_prefix[i] += divisor_prefix[i-1]
    out = []
    for n in values[1:]:
        answer = 0
        left = 1
        end = n//2
        while left <= end:
            quotient = n//left
            right = min(end,n//quotient)
            answer += (right-left+1)*divisor_prefix[quotient-1]
            left = right+1
        out.append(str(answer))
    sys.stdout.write('\n'.join(out)+'\n')

if __name__ == '__main__':
    main()
