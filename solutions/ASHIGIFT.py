#!/usr/bin/env python3
"""ASHIGIFT: standalone Python 3 solution."""
import sys
def solve(it):
 next(it);b=next(it);ev=[(next(it),0,next(it),0) for _ in range(b)];c=next(it)
 ev += [(next(it),1,next(it),next(it)) for _ in range(c)];ev.sort();need=1
 for _,kind,x,y in reversed(ev):
  if kind==0:need+=x
  else:need=min(need,max(x,need-y))
 return str(need)

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
