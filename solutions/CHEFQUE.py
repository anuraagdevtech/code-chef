#!/usr/bin/env python3
"""CHEFQUE: standalone Python 3 solution."""
import sys
def main():
 q,s,a,b=map(int,sys.stdin.buffer.read().split());bits=bytearray(1<<28);ans=0
 for _ in range(q):
  x=s>>1;j=x>>3;mask=1<<(x&7);present=bits[j]&mask
  if s&1:
   if not present:bits[j]|=mask;ans+=x
  elif present:bits[j]^=mask;ans-=x
  s=(a*s+b)&4294967295
 print(ans)

if __name__ == '__main__':
 main()
