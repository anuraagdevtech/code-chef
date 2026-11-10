#!/usr/bin/env python3
"""TSHIRTS: standalone Python 3 solution."""
import sys
def main():
 lines=iter(sys.stdin.buffer.read().splitlines());t=int(next(lines));out=[];mod=1000000007
 for _ in range(t):
  n=int(next(lines));owners=[[] for _ in range(101)]
  for i in range(n):
   for x in map(int,next(lines).split()):owners[x].append(1<<i)
  dp=[0]*(1<<n);dp[0]=1
  for people in owners:
   for mask in range((1<<n)-1,-1,-1):
    if dp[mask]:
     for bit in people:
      if not mask&bit:dp[mask|bit]=(dp[mask|bit]+dp[mask])%mod
  out.append(str(dp[-1]))
 print('\n'.join(out))

if __name__ == '__main__':
 main()
