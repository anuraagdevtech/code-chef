#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
for _ in range(next(it)):
 a=next(it);b=next(it);c=next(it);out.append(str(1<<(a^b).bit_count()))
print('\n'.join(out))
