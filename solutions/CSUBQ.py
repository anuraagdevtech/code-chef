#!/usr/bin/env python3
import sys
from array import array
it=iter(map(int,sys.stdin.buffer.read().split()));n,q,low,high=(next(it) for _ in range(4));size=1
while size<n:size*=2
# Node stores length, prefix/suffix good lengths and good-subarray count
# for each of the thresholds high and low-1.
length=array('I',[0])*(2*size)
for i in range(size,size+n):length[i]=1
for i in range(size-1,0,-1):length[i]=length[i*2]+length[i*2+1]
pre=[array('I',length),array('I',length)];suf=[array('I',length),array('I',length)];count=[array('Q',[0])*(2*size),array('Q',[0])*(2*size)]
for z in range(2):
 for i in range(1,2*size):count[z][i]=length[i]*(length[i]+1)//2
out=[]
for _ in range(q):
 typ,x,y=next(it),next(it),next(it)
 if typ==1:
  leaf=size+x-1
  for z,bound in enumerate((high,low-1)):
   good=int(y<=bound);pre[z][leaf]=suf[z][leaf]=count[z][leaf]=good;i=leaf//2;p,s,c=pre[z],suf[z],count[z]
   while i:
    a,b=i*2,i*2+1;p[i]=p[a]+(p[b] if p[a]==length[a] else 0);s[i]=s[b]+(s[a] if s[b]==length[b] else 0);c[i]=c[a]+c[b]+s[a]*p[b];i//=2
 else:
  results=[]
  for z in range(2):
   l,r=size+x-1,size+y;ll=lp=ls=lc=0;rl=rp=rs=rc=0;p,s,c=pre[z],suf[z],count[z]
   while l<r:
    if l&1:
     lc+=c[l]+ls*p[l];lp+=p[l] if lp==ll else 0;ls=s[l]+(ls if s[l]==length[l] else 0);ll+=length[l];l+=1
    if r&1:
     r-=1;rc=c[r]+rc+s[r]*rp;rs+=s[r] if rs==rl else 0;rp=p[r]+(rp if p[r]==length[r] else 0);rl+=length[r]
    l//=2;r//=2
   results.append(lc+rc+ls*rp)
  out.append(str(results[0]-results[1]))
print('\n'.join(out))
