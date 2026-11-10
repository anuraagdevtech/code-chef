#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
mx=100000;sieve=bytearray(b'\1')*(mx+1);sieve[0:2]=b'\0\0'
for p in range(2,317):
 if sieve[p]:sieve[p*p:mx+1:p]=b'\0'*((mx-p*p)//p+1)
for _ in range(next(it)):
 n=next(it);k=next(it);single=[1]+[p for p in range(n//2+1,n+1) if sieve[p]]
 if k<=len(single):out.append('YES');out.append(' '.join(map(str,single[:k])))
 elif n-k<=len(single):
  removed=set(single[:n-k]);out.append('YES');out.append(' '.join(str(i) for i in range(1,n+1) if i not in removed))
 else:out.append('NO')
print('\n'.join(out))
