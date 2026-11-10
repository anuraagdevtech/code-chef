#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()));out=[]
for _ in range(next(it)):
 states,width=next(it),next(it);n=states*width;a=[next(it) for _ in range(n)];a+=a[:width];wins=[0]*width;s=sum(a[:width])
 for i in range(n):
  wins[i%width]+=s>width//2;s+=a[i+width]-a[i]
 out.append(str(int(max(wins)>states//2)))
print('\n'.join(out))
