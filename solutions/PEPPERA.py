#!/usr/bin/env python3
import sys
it=iter(sys.stdin.buffer.read().split());out=[]
for _ in range(int(next(it))):
 n=int(next(it)); rows=[next(it).decode() for _ in range(n)]; weights=[abs(s[:n//2].count('1')-s[n//2:].count('1')) for s in rows]; history=[1]
 for w in weights: history.append(history[-1]|history[-1]<<w)
 total=sum(weights); target=total//2
 while not (history[-1]>>target&1):target-=1
 chosen=set()
 for i in range(n-1,-1,-1):
  if not history[i]>>target&1:chosen.add(i);target-=weights[i]
 for i,s in enumerate(rows):
  positive=s[:n//2].count('1')>=s[n//2:].count('1')
  out.append(s if positive==(i in chosen) else s[::-1])
print('\n'.join(out))
