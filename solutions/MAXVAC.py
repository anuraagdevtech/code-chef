#!/usr/bin/env python3
import sys
it=iter(sys.stdin.buffer.read().split());out=[]
for _ in range(int(next(it))):
 n=int(next(it));x=int(next(it));s=next(it).decode();runs=[len(v) for v in s.split('1')];ans=sum(v//x for v in runs)
 gain=max([0]+[(runs[i]+runs[i+1]+1)//x-runs[i]//x-runs[i+1]//x for i in range(len(runs)-1)])
 out.append(str(ans+gain))
print('\n'.join(out))
