#!/usr/bin/env python3
"""KEEPOUT: standalone Python 3 solution."""
import sys
def solve(it):
 n,m=next(it),next(it);a=[next(it) for _ in range(n)];v=[0]+sorted(a)+[m];pos={x:i for i,x in enumerate(v)};le=[i-1 for i in range(n+2)];ri=[i+1 for i in range(n+2)];best=max(v[i+1]-v[i] for i in range(n+1));out=[]
 for x in reversed(a):
  out.append(best);i=pos[x];l,r=le[i],ri[i];best=max(best,v[r]-v[l]);ri[l]=r;le[r]=l
 return ' '.join(map(str,reversed(out)))

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
