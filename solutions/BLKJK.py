#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()));out=[]
for _ in range(next(it)):
 n,x,y=next(it),next(it),next(it);a=[next(it) for _ in range(n)];s=0;zero=False
 for v in a:s+=v;zero|=x<=s<=y
 if zero:out.append('0');continue
 cap=min(n,y);mask=(1<<(y+1))-1;dp=[1]+[0]*cap;pre=[[0]*(cap+1) for _ in range(n+1)];pre[0]=[1]*(cap+1)
 for i,v in enumerate(a,1):
  row=pre[i]
  for j in range(min(i,cap),0,-1):
   new=(dp[j-1]<<v)&mask;fresh=new&~dp[j];dp[j]|=new;cost=i-j
   if cost<=cap:row[cost]|=fresh
  for cost in range(cap+1):row[cost]|=pre[i-1][cost]|(row[cost-1] if cost else 0)
 dp=[1]+[0]*cap;answer=cap+1
 for i in range(n-1,-1,-1):
  v=a[i]
  for j in range(min(n-i,cap,answer-1),0,-1):
   new=(dp[j-1]<<v)&mask;fresh=new&~dp[j];dp[j]|=new
   while fresh:
    bit=fresh&-fresh;fresh-=bit;s=bit.bit_length()-1;low=max(0,x-s);high=y-s
    if high>=low and (pre[i][j]>>low)&((1<<(high-low+1))-1):answer=j;break
 out.append(str(answer if answer<=cap else -1))
print('\n'.join(out))
