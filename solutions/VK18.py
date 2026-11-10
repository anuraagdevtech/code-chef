#!/usr/bin/env python3
import sys
a=list(map(int,sys.stdin.buffer.read().split()))[1:];m=max(a,default=0);v=[0]*(2*m+1);pre=[0]*(2*m+2)
for i in range(1,2*m+1):
 d=i%10;v[i]=v[i//10]+(d if d%2==0 else -d);pre[i+1]=pre[i]+abs(v[i])
 ans=[0]*(m+1)
for i in range(1,m+1):ans[i]=ans[i-1]+2*(pre[2*i]-pre[i+1])+abs(v[2*i])
print('\n'.join(str(ans[n]) for n in a))
