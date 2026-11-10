#!/usr/bin/env python3
import sys
import heapq
it=iter(map(int,sys.stdin.buffer.read().split()));out=[]
for _ in range(next(it)):
 n,k,m=next(it),next(it),next(it);a=[next(it) for _ in range(n)];judges=sorted((next(it)-1,next(it)-1,next(it)) for _ in range(m));heap=[];p=0;groups={}
 for i,x in enumerate(a):
  while p<m and judges[p][0]<=i:
   l,r,c=judges[p];heapq.heappush(heap,(c,r));p+=1
  while heap and heap[0][1]<i:heapq.heappop(heap)
  if x<0 and heap and heap[0][0]<=k:groups.setdefault(heap[0][0],[]).append(-x)
 dp=[0]*(k+1)
 for cost,gains in groups.items():
  for gain in sorted(gains,reverse=True)[:k//cost]:
   for budget in range(k,cost-1,-1):dp[budget]=max(dp[budget],dp[budget-cost]+gain)
 out.append(str(sum(a)+dp[k]))
print('\n'.join(out))
