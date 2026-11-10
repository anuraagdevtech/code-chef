"""Burnside's lemma with row partitions and a column cycle-index DP."""
import sys
from math import gcd

MOD = 1000000007


def solve():
    n,m = sorted(map(int,sys.stdin.buffer.read().split()))
    if n == 1:
        print(m+1)
        return
    inv = [0,1]+[0]*(m-1)
    for i in range(2,m+1):
        inv[i] = MOD-(MOD//i)*inv[MOD % i] % MOD
    answer = 0
    cycles = []

    def visit(remaining,minimum,weight):
        nonlocal answer
        if not remaining:
            fixed = [0]*(m+1)
            for j in range(1,m+1):
                fixed[j] = pow(2,sum(count*gcd(length,j) for length,count in cycles),MOD)
            dp = [0]*(m+1)
            dp[0] = 1
            for k in range(1,m+1):
                dp[k] = sum(fixed[j]*dp[k-j] for j in range(1,k+1)) % MOD*inv[k] % MOD
            answer = (answer+weight*dp[m]) % MOD
            return
        for length in range(minimum,remaining+1):
            w = weight
            for count in range(1,remaining//length+1):
                w = w*inv[length]*inv[count] % MOD
                cycles.append((length,count))
                visit(remaining-length*count,length+1,w)
                cycles.pop()

    visit(n,1,1)
    print(answer)


if __name__ == '__main__':
    solve()
