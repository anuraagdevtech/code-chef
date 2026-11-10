#!/usr/bin/env python3
"""STROPERS: standalone Python 3 solution."""
import sys
def solve(it):
 s=next(it).decode(); n=len(s); seen=set(); base=n+1
 for l in range(n):
  ones=odd=0
  for r in range(l,n):
   if s[r]=='1':ones+=1
   elif ones&1:odd+=1
   seen.add(((r-l+1)*base+ones)*base+odd)
 return str(len(seen))

if __name__ == '__main__':
 it=iter(sys.stdin.buffer.read().split())
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
