#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()));cases=[(next(it),next(it),next(it),next(it)) for _ in range(next(it))];p=1000000007;limit=max((n+m for n,m,a,b in cases),default=0);f=[1]*(limit+1)
for i in range(1,limit+1):f[i]=f[i-1]*i%p
iv=[1]*(limit+1);iv[limit]=pow(f[limit],p-2,p)
for i in range(limit,0,-1):iv[i-1]=iv[i]*i%p
def choose(n,k):return f[n]*iv[k]%p*iv[n-k]%p
out=[]
for n,m,a,b in cases:
 answer=0
 for x in range(n-a+1):answer=(answer+choose(x+b-1,x)*choose(n-x+m-b,n-x))%p
 out.append(str(answer))
print('\n'.join(out))
