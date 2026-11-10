#!/usr/bin/env python3
"""DIST_VALS: standalone Python 3 solution."""
import sys
def solve(it):
 n=next(it); a=[next(it) for _ in range(n)]; st=[]; vals=set()
 for x in a:
  while st and st[-1]<=x:vals.add(x-st.pop())
  if st:vals.add(st[-1]-x)
  st.append(x)
 return str(len(vals))

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
