#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
for _ in range(next(it)):
 n=next(it);out.append(' '.join(str(i^(i-1)) for i in range(1,n+1)))
print('\n'.join(out))
