#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()));out=[];p=1000000007
for _ in range(next(it)):
 n,m=next(it),next(it);cmd=[(next(it),next(it)-1,next(it)-1) for _ in range(m)];delta=[0]*(m+1);a=[0]*(n+1);extra=0
 for i in range(m-1,-1,-1):
  extra=(extra+delta[i])%p;count=extra+1;t,l,r=cmd[i]
  if t==2:delta[r]=(delta[r]+count)%p;delta[l-1 if l else m]=(delta[l-1 if l else m]-count)%p
  else:a[l]+=count;a[r+1]-=count
 total=0;ans=[]
 for x in a[:n]:total=(total+x)%p;ans.append(str(total))
 out.append(' '.join(ans))
print('\n'.join(out))
