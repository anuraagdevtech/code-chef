#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
for _ in range(next(it)):
 n=next(it);k=next(it);r=n%k;candidates=[r//2]
 if n>=k:candidates.append((r+k)//2)
 out.append(str(max(candidates,key=lambda x:(x%k)*((n-x)%k))))
print('\n'.join(out))
