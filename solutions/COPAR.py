#!/usr/bin/env python3
"""COPAR: standalone Python 3 solution."""
import sys
spf=list(range(100001))
for i in range(2,317):
 if spf[i]==i:
  for j in range(i*i,100001,i):
   if spf[j]==j:spf[j]=i
def solve(it):
 n=next(it); a=[next(it) for _ in range(n)]; last={}; fs=[]
 for i,x in enumerate(a):
  f=[]
  while x>1:
   p=spf[x];f.append(p)
   while x%p==0:x//=p
  fs.append(f)
  for p in f:last[p]=i
 end=0
 for i,f in enumerate(fs):
  for p in f:end=max(end,last[p])
  if i==end:return str(i+1)

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
