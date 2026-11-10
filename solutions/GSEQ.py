#!/usr/bin/env python3
"""GSEQ: standalone Python 3 solution."""
import sys
def solve(it):
 n=next(it);a=[next(it) for _ in range(n)];dp={0:(1,0)};prev=[-1]*(n+1);s=0;best=(1,0)
 for i,x in enumerate(a,1):
  s+=2*x-1;v,j=dp.get(s-1,(0,-1));cur=(v+1,i);prev[i]=j
  if cur[0]>dp.get(s,(0,0))[0]:dp[s]=cur
  if cur[0]>best[0]:best=cur
 ans=[];j=best[1]
 while j>=0:ans.append(j+1);j=prev[j]
 return str(best[0])+'\n'+' '.join(map(str,reversed(ans)))

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
