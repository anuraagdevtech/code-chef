#!/usr/bin/env python3
"""MAKEPAL3: standalone Python 3 solution."""
import sys
def solve(it):
 n=next(it);a=[next(it) for _ in range(n)];prev=ans=0
 for i in range(n//2):
  d=a[i]-a[-1-i];ans+=abs(d) if d*prev<0 else max(0,abs(d)-abs(prev));prev=d
 return str(ans)

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
