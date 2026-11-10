#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split())); out=[]
for _ in range(next(it)):
 n,m=next(it),next(it); bits=1
 for _ in range(n): bits |= bits << next(it)
 out.append('Yes' if bits>>m&1 else 'No')
print('\n'.join(out))
