#!/usr/bin/env python3
import sys
it=iter(sys.stdin.buffer.read().split());out=[]
beat={'R':'P','P':'S','S':'R'}
for _ in range(int(next(it))):
 n=int(next(it));s=next(it).decode();mp={c:c for c in 'RPS'};a=[]
 for c in reversed(s):
  old=mp.copy()
  for x in 'RPS':mp[x]=old[c if beat[x]==c else x]
  a.append(mp[c])
 out.append(''.join(reversed(a)))
print('\n'.join(out))
