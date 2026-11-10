#!/usr/bin/env python3
"""WRDVLS: standalone Python 3 solution."""
import sys
def solve(it):
 n=next(it);p={}
 for i in range(n):p.setdefault(next(it),[]).append(i)
 ans=0
 for x,v in p.items():
  if len(v)<x:continue
  v=[-1]+v+[n]
  for j in range(1,len(v)-x):ans+=x*(v[j]-v[j-1])*(v[j+x]-v[j+x-1])
 return str(ans)

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
