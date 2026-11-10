#!/usr/bin/env python3
"""MAXCYCSHIFT: standalone Python 3 solution."""
import sys
from collections import Counter

def solve(it):
 n=next(it);a=[next(it) for _ in range(n)];p=[0]
 for x in a+a:p.append(p[-1]^x)
 c=Counter(p[1:n+1]);best=len(c)
 for i in range(1,n):
  x=p[i];c[x]-=1
  if not c[x]:del c[x]
  x=p[i+n];c[x]+=1;best=max(best,len(c))
 return str(best)

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
