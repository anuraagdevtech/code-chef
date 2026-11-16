import sys
from array import array


def main() -> None:
    values = list(map(int,sys.stdin.buffer.read().split()))
    limit = max(values[1:])
    balance = array('b',[0])*(2*limit+1)
    prefix = array('q',[0])*(2*limit+1)
    for s in range(1,2*limit+1):
        digit = s%10
        balance[s] = balance[s//10]+(digit if digit%2 == 0 else -digit)
        prefix[s] = prefix[s-1]+abs(balance[s])
    answer = array('q',[0])*(limit+1)
    for n in range(1,limit+1):
        answer[n] = answer[n-1]+prefix[2*n]+prefix[2*n-1]-2*prefix[n]
    sys.stdout.write('\n'.join(str(answer[n]) for n in values[1:])+'\n')

if __name__ == '__main__':
    main()
