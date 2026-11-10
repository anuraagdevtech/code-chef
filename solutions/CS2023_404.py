#!/usr/bin/env python3
"""CS2023_404: standalone Python 3 solution."""
import sys
def solve(it):
 int(next(it));s=next(it);m=1000000007;a=1;b=c=d=0
 for x in s:
  if x==52:b=(b+a)%m;d=(d+c)%m
  elif x==48:c=(c+b)%m
  else:a,b,c,d=2*a%m,(2*b+a)%m,(2*c+b)%m,(2*d+c)%m
 return str(d)

if __name__ == '__main__':
 it=iter(sys.stdin.buffer.read().split())
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
