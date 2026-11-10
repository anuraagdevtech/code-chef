#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
n=next(it);m=next(it);q=next(it)
for _ in range(q):
 s=next(it);k=1
 while m*k*(k+1)//2<s:k+=1
 extra=s-k*(k+1)//2;a=[1]*k
 for i in range(k,0,-1):v=min(m-1,extra//i);a[i-1]+=v;extra-=i*v
 out.append(f'1 {k}');out.append(' '.join(map(str,a)))
print('\n'.join(out))
