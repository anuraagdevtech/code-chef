#!/usr/bin/env python3
"""MEXSUB: standalone Python 3 solution."""
import sys
import heapq

def solve(it):
 n=next(it);a=[next(it) for _ in range(n)];seen=set(a);mex=0
 while mex in seen:mex+=1
 mod=1000000007
 if mex==0:return str(pow(2,n-1,mod))
 last=[-1]*mex;h=[(-1,x) for x in range(mex)];heapq.heapify(h);pref=[1];dp=0
 for i,x in enumerate(a):
  if x<mex:last[x]=i;heapq.heappush(h,(i,x))
  while h[0][0]!=last[h[0][1]]:heapq.heappop(h)
  j=h[0][0];dp=pref[j] if j>=0 else 0;pref.append((pref[-1]+dp)%mod)
 return str(dp)

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
