#!/usr/bin/env python3
import sys
it=iter(sys.stdin.buffer.read().split());out=[]
for _ in range(int(next(it))):
 s=next(it).decode();n=len(s);ones=s.count('1');even=s[::2].count('1');target=2*ones%3
 if even%3==target:out.append('0');continue
 low=max(0,ones-n//2);high=min(ones,(n+1)//2)
 if low+(target-low)%3>high:out.append('-1');continue
 first=-1;last=-1;one=False
 for i in range(n-1):
  if s[i]==s[i+1]:continue
  effect=1 if (s[i]=='0')==(i%2==0) else -1
  if (even+effect)%3==target:one=True;break
  if first<0:first=i
  last=i
 out.append('1' if one else ('2' if last-first>=2 else '3'))
print('\n'.join(out))
