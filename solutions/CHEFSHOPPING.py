#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
for _ in range(next(it)):
 n=next(it);l=[next(it) for _ in range(n)];r=[next(it) for _ in range(n)]
 out.append(str(sum(min(r[i],l[i+1]) for i in range(n-1))))
print('\n'.join(out))
