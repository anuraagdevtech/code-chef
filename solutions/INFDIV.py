"""Remainder expectation DP with harmonic quotient blocks.

Store arithmetic-progression prefix sums only up to the largest remainder
that each quotient can produce. This keeps their total storage O(n log n).
"""
import sys
from array import array
from math import isqrt

MOD = 1000000007


def expectations(limit):
    inverse = [0,1]+[0]*max(0,limit-1)
    for i in range(2,limit+1):
        inverse[i] = MOD-(MOD//i)*inverse[MOD % i] % MOD
    values = [0]*(limit+1)
    maxq = isqrt(limit)
    sums = [None]+[array('I',[0])*(limit//(q+1)+1) for q in range(1,maxq+1)]
    for value in range(1,limit+1):
        root = isqrt(value)
        total = 1
        for divisor in range(1,root+1):
            total += values[value % divisor]
        for quotient in range(1,value//(root+1)+1):
            left = max(root+1,value//(quotient+1)+1)
            right = value//quotient
            low = value-quotient*right
            high = value-quotient*left
            row = sums[quotient]
            total += row[high]
            if low >= quotient:
                total -= row[low-quotient]
        current = total % MOD*inverse[value] % MOD
        values[value] = current
        for quotient in range(1,min(maxq,limit//value-1)+1):
            row = sums[quotient]
            row[value] = (current+(row[value-quotient] if value >= quotient else 0)) % MOD
    return values


def solve():
    n,m = map(int,sys.stdin.buffer.read().split())
    if m < n:
        print(n*expectations(m)[m] % MOD)
        return
    remainders = [m % r for r in range(1,n+1)]
    values = expectations(max(remainders))
    print((1+sum(values[r] for r in remainders)) % MOD)


if __name__ == '__main__':
    solve()
