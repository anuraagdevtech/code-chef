#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
for _ in range(next(it)):
 n=next(it);k=next(it);length=k+2+(k-1)//2;blocks,rem=divmod(n,length)
 out.append(str(3*blocks+(3 if rem>k+1 else (1 if rem else 0))))
print('\n'.join(out))
