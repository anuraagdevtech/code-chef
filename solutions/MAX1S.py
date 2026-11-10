#!/usr/bin/env python3
"""MAX1S: standalone Python 3 solution."""
import sys
def solve(it):
 s=next(it);n=len(s);total=best=cur=0
 for i,c in enumerate(s,1):
  w=i*(n-i+1)
  if c==49:total+=w;w=-w
  cur=max(0,cur+w);best=max(best,cur)
 return str(total+best)

if __name__ == '__main__':
 it=iter(sys.stdin.buffer.read().split())
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
