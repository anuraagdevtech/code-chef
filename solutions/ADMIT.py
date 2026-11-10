#!/usr/bin/env python3
"""ADMIT: standalone Python 3 solution."""
import sys
def solve(it):
 n,m=next(it),next(it);r=[next(it) for _ in range(n)];s=[next(it) for _ in range(m)];prefs=[]
 for _ in range(m):k=next(it);prefs.append([next(it)-1 for _ in range(k)])
 used=set()
 for i in sorted(range(m),key=s.__getitem__):
  v=min((x for x in prefs[i] if x not in used),key=r.__getitem__,default=-1)
  if i==0:return str(v+1)
  if v>=0:used.add(v)

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
