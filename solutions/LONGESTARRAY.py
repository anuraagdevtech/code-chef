#!/usr/bin/env python3
"""LONGESTARRAY: standalone Python 3 solution."""
import sys
def solve(it):
 n=next(it);a=[next(it) for _ in range(n)];bits=[];total=[0]*30
 for x in a:
  b=[]
  while x:
   z=x&-x;k=z.bit_length()-1;b.append(k);total[k]+=1;x-=z
  bits.append(b)
 active=sum(v>0 for v in total);c=[0]*30;have=bad=l=0;ans=-1
 for r,b in enumerate(bits):
  for k in b:
   if c[k]==0:have+=1
   c[k]+=1
   if c[k]==total[k]:bad+=1
  while bad:
   for k in bits[l]:
    if c[k]==total[k]:bad-=1
    c[k]-=1
    if not c[k]:have-=1
   l+=1
  if have==active:ans=max(ans,r-l+1)
 return str(ans)

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
