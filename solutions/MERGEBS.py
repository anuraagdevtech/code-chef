#!/usr/bin/env python3
"""MERGEBS: standalone Python 3 solution."""
import sys
def solve(it):
 n=int(next(it));a=next(it);b=next(it);pb=[0]
 for c in b:pb.append(pb[-1]+(c==49))
 dp=[0]*(n+1)
 for j in range(1,n+1):dp[j]=dp[j-1]+(pb[j-1] if b[j-1]==48 else 0)
 ones=0
 for x in a:
  ones+=x==49
  dp[0]+=ones if x==48 else 0
  for j,y in enumerate(b,1):dp[j]=min(dp[j]+(ones+pb[j] if x==48 else 0),dp[j-1]+(ones+pb[j-1] if y==48 else 0))
 return str(dp[n])

if __name__ == '__main__':
 it=iter(sys.stdin.buffer.read().split())
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
