#!/usr/bin/env python3
"""SUMOFCUBE: standalone Python 3 solution."""
import sys
def solve(it):
 n=next(it);mod=998244353;p=s1=s2=s3=ans=0
 for i in range(1,n+1):
  p=(p+next(it))%mod;p2=p*p%mod;p3=p2*p%mod
  ans=(ans+i*p3-3*p2*s1+3*p*s2-s3)%mod
  s1=(s1+p)%mod;s2=(s2+p2)%mod;s3=(s3+p3)%mod
 return str(ans)

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
