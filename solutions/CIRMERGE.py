#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
for _ in range(next(it)):
 n=next(it);a=[next(it) for _ in range(n)]*2;m=2*n;p=[0]
 for v in a:p.append(p[-1]+v)
 dp=[[0]*m for _ in range(m)];opt=[[0]*m for _ in range(m)]
 for i in range(m):opt[i][i]=i
 for length in range(2,n+1):
  for i in range(m-length+1):
   j=i+length-1;lo=opt[i][j-1];hi=min(j-1,opt[i+1][j]);best=10**30;at=lo
   for k in range(lo,hi+1):
    v=dp[i][k]+dp[k+1][j]
    if v<best:best=v;at=k
   dp[i][j]=best+p[j+1]-p[i];opt[i][j]=at
 out.append(str(min(dp[i][i+n-1] for i in range(n))))
print('\n'.join(out))
