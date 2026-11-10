#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
for _ in range(next(it)):
 n=next(it);a=sorted(next(it) for _ in range(n));b=[0]*n
 b[::2]=a[:(n+1)//2][::-1];b[1::2]=a[(n+1)//2:][::-1]
 ok=all((b[i-1]<b[i]>b[i+1]) or (b[i-1]>b[i]<b[i+1]) for i in range(1,n-1))
 if not ok:
  b[::2]=a[n//2:];b[1::2]=a[:n//2]
  ok=all((b[i-1]<b[i]>b[i+1]) or (b[i-1]>b[i]<b[i+1]) for i in range(1,n-1))
 out.append(' '.join(map(str,b)) if ok else '-1')
print('\n'.join(out))
