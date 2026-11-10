#!/usr/bin/env python3
"""SIMPLEARRAY: standalone Python 3 solution."""
import sys
def solve(it):
 n,k=next(it),next(it);c=[0]*k
 for _ in range(n):c[next(it)%k]+=1
 m=1000000007;ans=c[0]+1
 for r in range(1,(k+1)//2):ans=ans*(pow(2,c[r],m)+pow(2,c[k-r],m)-1)%m
 if k%2==0:ans=ans*(c[k//2]+1)%m
 return str(ans)

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
