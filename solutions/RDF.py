#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()));cases=[(next(it),next(it)) for _ in range(next(it))];mx=max((n for n,k in cases),default=0);by={};ans=[0.0]*len(cases)
for i,(n,k) in enumerate(cases):
 if k<70:by.setdefault(k,[]).append((i,n))
dp=[float(i) for i in range(mx+1)]
for k in range(min(69,max(by,default=0))+1):
 for i,n in by.get(k,[]):ans[i]=dp[n]
 total=0.0;nd=[0.0]*(mx+1)
 for n in range(1,mx+1):total+=dp[n-1];nd[n]=total/n
 dp=nd
print('\n'.join('%.10f'%x for x in ans))
