#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
mod=10**9+7
for _ in range(next(it)):
 p=next(it).bit_count();out.append(str((pow(3,p,mod)-3*pow(2,p,mod)+3)%mod))
print('\n'.join(out))
