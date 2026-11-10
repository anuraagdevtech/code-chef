#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
mod=10**9+7;mx=100000;f=[1]*(mx+1);iv=[1]*(mx+1);p2=[1]*(mx+1);ip2=[1]*(mx+1);half=(mod+1)//2
for i in range(1,mx+1):f[i]=f[i-1]*i%mod;p2[i]=p2[i-1]*2%mod;ip2[i]=ip2[i-1]*half%mod
iv[mx]=pow(f[mx],-1,mod)
for i in range(mx,0,-1):iv[i-1]=iv[i]*i%mod
def choose(n,k):return 0 if k<0 or k>n else f[n]*iv[k]%mod*iv[n-k]%mod
for _ in range(next(it)):
 n=next(it);counts=[0]*(n+1)
 for _ in range(n):counts[next(it)]+=1
 size=0;tail=0;ans=0
 for v in range(1,n+1):
  old=tail
  for _ in range(counts[v]):
   tail=(tail+choose(size,v-1)*ip2[size+1])%mod;size+=1
  ans=(ans+tail-old)%mod
  tail=(tail-choose(size,v)*ip2[size])%mod
 out.append(str(ans*p2[n]%mod))
print('\n'.join(out))
