#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()));out=[];p=1000000007
for _ in range(next(it)):
 n,k=next(it),next(it);a,b=1,0
 for _ in range(n):a,b=b,(a*k+b*(k-1))%p
 out.append(str(a))
print('\n'.join(out))
