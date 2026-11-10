#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
for _ in range(next(it)):
 n=next(it);k=next(it);a=[next(it) for _ in range(n)]
 ok=(a==a[::-1]) if n==k else (n%2==1 or k%2==1 or sum(a)%2==0)
 out.append('YES' if ok else 'NO')
print('\n'.join(out))
