#!/usr/bin/env python3
"""SUMXOR2: standalone Python 3 solution."""
import sys
def main():
 it=iter(map(int,sys.stdin.buffer.read().split()));n=next(it);counts=[0]*30
 for _ in range(n):
  x=next(it)
  while x:
   v=x&-x;counts[v.bit_length()-1]+=1;x-=v
 mod=998244353;inv=[0,1]+[0]*(n-1)
 for k in range(2,n+1):inv[k]=mod-(mod//k)*inv[mod%k]%mod
 comb=[1]*(n+1)
 for k in range(1,n+1):comb[k]=comb[k-1]*(n-k+1)%mod*inv[k]%mod
 groups={}
 for b,c in enumerate(counts):
  if c:groups[c]=(groups.get(c,0)+(1<<b))%mod
 ans=[0]*(n+1);half=(mod+1)//2
 for c,weight in groups.items():
  d=n-2*c;prev=1;cur=d%mod;weight=weight*half%mod
  for k in range(1,n+1):
   ans[k]=(ans[k]+weight*(comb[k]-cur))%mod
   prev,cur=cur,(d*cur-(n-k+1)*prev)*inv[k+1]%mod if k<n else 0
 for k in range(1,n+1):ans[k]=(ans[k]+ans[k-1])%mod
 q=next(it);print('\n'.join(str(ans[next(it)]) for _ in range(q)))

if __name__ == '__main__':
 main()
