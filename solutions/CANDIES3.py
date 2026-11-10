#!/usr/bin/env python3
"""CANDIES3: standalone Python 3 solution."""
import sys
def solve(it):
 n,m=next(it),next(it);f=[0]*(m+2)
 for _ in range(n):f[next(it)]+=1
 c=[next(it) for _ in range(m)]
 for i in range(m-1,-1,-1):f[i]+=f[i+1]
 return str(max(c[p-1]*sum(f[j] for j in range(p,m+1,p)) for p in range(1,m+1)))

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
