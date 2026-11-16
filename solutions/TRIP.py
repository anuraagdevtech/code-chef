import sys
from array import array


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    n,capacity = int(next(tokens)),int(next(tokens))
    position = array('q',(int(next(tokens)) for _ in range(n)))
    del tokens
    distance = array('i',[0])*n
    prefix = array('i',[0])*(n+1)
    prefix[1] = 1
    level_end = [0]
    left = 0
    mod = 1000000007
    for j in range(1,n):
        while position[j]-position[left] > capacity:
            left += 1
        level = distance[left]
        ways = (prefix[level_end[level]+1]-prefix[left])%mod
        distance[j] = level+1
        if distance[j] == len(level_end):
            level_end.append(j)
        else:
            level_end[distance[j]] = j
        prefix[j+1] = (prefix[j]+ways)%mod
    print(distance[-1]-1,(prefix[n]-prefix[n-1])%mod)

if __name__ == '__main__':
    main()
