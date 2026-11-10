#!/usr/bin/env python3
import sys
it=iter(sys.stdin.buffer.read().split());out=[]
for _ in range(int(next(it))):
 n,m=int(next(it)),int(next(it));a=[next(it) for _ in range(n)]
 def near(x,y):return {(u,v) for u,v in ((x,y),(x-1,y),(x+1,y),(x,y-1),(x,y+1)) if 0<=u<n and 0<=v<m}
 dp=[[[10**9]*2 for _ in range(m)] for _ in range(n)];initial=sum(a[x][y]==49 for x,y in near(0,0));dp[0][0]=[initial,initial]
 for x in range(n):
  for y in range(m):
   for last in range(2):
    if dp[x][y][last]>=10**9:continue
    seen=near(x,y)
    if x+y:seen|=near(x-(last==0),y-(last==1))
    for d,(u,v) in enumerate(((x+1,y),(x,y+1))):
     if u<n and v<m:dp[u][v][d]=min(dp[u][v][d],dp[x][y][last]+sum(a[r][s]==49 for r,s in near(u,v)-seen))
 out.append(str(min(dp[-1][-1])))
print('\n'.join(out))
