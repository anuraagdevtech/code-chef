#!/usr/bin/env python3
"""GCD_QUERIES: standalone Python 3 solution."""
import sys
spf=list(range(1000001))
for i in range(2,1001):
 if spf[i]==i:
  for j in range(i*i,1000001,i):
   if spf[j]==j:spf[j]=i
import heapq

def solve(it):
 n=next(it);a=sorted(next(it) for _ in range(n));heaps={}
 def factors(x):
  while x>1:
   p=spf[x];yield p
   while x%p==0:x//=p
 for i,x in enumerate(a):
  for p in factors(x):heaps.setdefault(p,[]).append(i)
 alive=bytearray(b'\1')*n;lo=0;out=[];q=next(it)
 for _ in range(q):
  x=next(it);best=n
  for p in factors(x):
   h=heaps.get(p)
   if h:
    while h and not alive[h[0]]:heapq.heappop(h)
    if h:best=min(best,h[0])
  if best==n:
   while not alive[lo]:lo+=1
   best=lo
  alive[best]=0;out.append(str(a[best]))
 return ' '.join(out)

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
