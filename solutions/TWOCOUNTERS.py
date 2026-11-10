#!/usr/bin/env python3
"""TWOCOUNTERS: standalone Python 3 solution."""
import sys
def solve(it):
 n,m=next(it),next(it);times=[next(it) for _ in range(m)];types=[next(it) for _ in range(m)];events=dict(zip(times,types));neg=-10**9;dp=[neg,neg,0,neg,neg]
 for t in range(1,n+1):
  dp=[dp[1],max(dp[0],dp[2]),max(dp[1],dp[3]),max(dp[2],dp[4]),dp[3]];kind=events.get(t)
  if kind==1:dp=[neg,neg,max(dp[:3]),dp[3]+1,dp[4]+1]
  elif kind==2:dp=[dp[0]+1,dp[1]+1,max(dp[2:]),neg,neg]
 return str(max(dp))

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
