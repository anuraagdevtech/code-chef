#!/usr/bin/env python3
import sys
it=iter(sys.stdin.buffer.read().split());out=[]
for _ in range(int(next(it))):
 n=int(next(it));q=int(next(it));a=next(it);b=next(it);p=[0]
 for i in range(n):p.append((p[-1]+(b[i]-a[i])*(1 if i%2==0 else -1))%26)
 for _ in range(q):l=int(next(it));r=int(next(it));out.append('YES' if p[r]==p[l-1] else 'NO')
print('\n'.join(out))
