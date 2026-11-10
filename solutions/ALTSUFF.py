#!/usr/bin/env python3
import sys
it=iter(sys.stdin.buffer.read().split());out=[]
for _ in range(int(next(it))):
 n=int(next(it));k=int(next(it));s=next(it).decode()
 a=[i for i in range(n) if s[i]=='0' and ((i and s[i-1]=='1') or (i+1<n and s[i+1]=='1'))]
 if not a:out.append('0'*n);continue
 k-=1;d=[n+1]*n;last=-2*n
 for i in range(n):
  if s[i]=='0' and ((i and s[i-1]=='1') or (i+1<n and s[i+1]=='1')):last=i
  d[i]=i-last
 last=3*n
 for i in range(n-1,-1,-1):
  if s[i]=='0' and ((i and s[i-1]=='1') or (i+1<n and s[i+1]=='1')):last=i
  d[i]=min(d[i],last-i)
 out.append(''.join('1' if v<=k and (k-v)%2==0 else '0' for v in d))
print('\n'.join(out))
