#!/usr/bin/env python3
"""SMALLESTDIFF: standalone Python 3 solution."""
import sys
def solve(it):
 n,m=next(it),next(it);a=sorted(next(it) for _ in range(n*m));transpose=n>m
 if transpose:n,m=m,n
 length=n+m-1;lo=n//2;hi=(n-1)//2;start=min(range(lo,len(a)-length-hi+1),key=lambda j:a[j+length-1]-a[j]);path=a[start:start+length];small=a[:start];large=a[start+length:];grid=[[0]*m for _ in range(n)];t=0
 for i in range(n):grid[i][0]=path[t];t+=1
 for j in range(1,m):grid[n-1][j]=path[t];t+=1
 for i in range(n-1):grid[i][1]=small.pop() if i%2==0 else large.pop()
 rest=iter(small+large)
 for i in range(n):
  for j in range(m):
   if not grid[i][j]:grid[i][j]=next(rest)
 if transpose:grid=[list(row) for row in zip(*grid)]
 return '\n'.join(' '.join(map(str,row)) for row in grid)

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
