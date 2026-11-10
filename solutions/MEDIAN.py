#!/usr/bin/env python3
import sys
from functools import lru_cache
it=iter(map(int,sys.stdin.buffer.read().split()));out=[]
for _ in range(next(it)):
 n=next(it);a=[next(it) for _ in range(n)];mx=max(a);initial=sum(1<<i for i,x in enumerate(a) if x==mx);full=(1<<n)-1
 @lru_cache(None)
 def solve(mask):
  if mask==full:return 0
  if mask.bit_count()*2>=n:return 1
  best=n;candidates=set()
  for l in range(n):
   balance=0;right=-1
   for r in range(l,n):
    balance+=1 if mask>>r&1 else -1
    if balance>=0:right=r
   if right>=l:
    new=mask|(((1<<(right-l+1))-1)<<l)
    if new!=mask:candidates.add(new)
  # Superset states can only improve future possibilities.
  ordered=sorted(candidates,key=int.bit_count,reverse=True);kept=[]
  for state in ordered:
   if any(state|other==other for other in kept):continue
   kept.append(state);best=min(best,1+solve(state))
   if best==2:break
  return best
 out.append(str(solve(initial)))
print('\n'.join(out))
