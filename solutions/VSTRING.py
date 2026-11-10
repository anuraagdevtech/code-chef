#!/usr/bin/env python3
import sys
it=iter(sys.stdin.buffer.read().split());out=[]
for _ in range(int(next(it))):
 n=int(next(it));c=int(next(it));s=next(it).decode();pos=[i for i,v in enumerate(s) if v=='1']
 if len(pos)<2:out.append('YES');continue
 gaps=[pos[i]-pos[i-1]-1 for i in range(1,len(pos))]+[n+pos[0]-pos[-1]-1]
 out.append('YES' if sum(g>c for g in gaps)<=1 else 'NO')
print('\n'.join(out))
