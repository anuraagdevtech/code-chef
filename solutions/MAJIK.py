#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
for _ in range(next(it)):
 n=next(it);p=next(it);q=next(it);a=sorted(next(it) for _ in range(n));b=sorted((abs(x) for x in a[1:-1]),reverse=True)
 out.append(str(a[-1]-a[0]+sum(b[:p+q])))
print('\n'.join(out))
