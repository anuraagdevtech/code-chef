#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
for _ in range(next(it)):
 n=next(it);k=next(it)-n;l=1
 while l<n and k>=l:k-=l;l+=1
 a=list(range(1,l+1))
 if l<n:a.append(a[l-k-1]);a.extend([a[-1]]*(n-l-1))
 out.append(' '.join(map(str,a)))
print('\n'.join(out))
