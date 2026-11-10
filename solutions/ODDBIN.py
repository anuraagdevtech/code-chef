#!/usr/bin/env python3
import sys
from functools import lru_cache
it=iter(map(int,sys.stdin.buffer.read().split()));out=[]
for _ in range(next(it)):
 m=next(it);odd=set()
 for _ in range(m):
  x=next(it)
  if x in odd:odd.remove(x)
  else:odd.add(x)
 @lru_cache(None)
 def solve(values):
  if not values:return 0
  if len(values)==1:return 1<<values[0].bit_count()
  bit=1<<(values[-1].bit_length()-1);low=set();high=[]
  for x in values:
   if x&bit:high.append(x^bit);x^=bit
   if x in low:low.remove(x)
   else:low.add(x)
  return solve(tuple(sorted(low)))+solve(tuple(high))
 out.append(str(solve(tuple(sorted(odd)))))
print('\n'.join(out))
