#!/usr/bin/env python3
"""CONSTANARRAY: standalone Python 3 solution."""
import sys
def solve(it):
 n,m=next(it),next(it);a=[next(it) for _ in range(n)];ans=[];used=set();unused=set(range(1,m+1))
 for x in a:
  if not unused:unused=set(range(1,m+1));used.clear()
  if x in unused:y=x;unused.remove(y)
  else:y=unused.pop()
  used.add(y);ans.append(y)
 return ' '.join(map(str,ans))

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
