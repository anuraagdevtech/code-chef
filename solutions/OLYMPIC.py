#!/usr/bin/env python3
import sys
from collections import Counter
it=iter(map(int,sys.stdin.buffer.read().split()));n=next(it);a=[next(it) for _ in range(n)];queries=[next(it) for _ in range(next(it))];p=1000000007;mx=sum(a);f=[1]*(mx+1)
for i in range(1,mx+1):f[i]=f[i-1]*i%p
iv=[1]*(mx+1);iv[mx]=pow(f[mx],p-2,p)
for i in range(mx,0,-1):iv[i-1]=iv[i]*i%p
# ceil(value/S) changes only O(sqrt(value)) times. Sweep those changes.
events={};total=mx;den=halfden=1;odd=0
for value,multiplicity in Counter(a).items():
 den=den*pow(iv[value],multiplicity,p)%p;halfden=halfden*pow(iv[value//2],multiplicity,p)%p;odd+=(value%2)*multiplicity
 size=1;old=value
 while old>1:
  end=(value-1)//(old-1);size=end+1;new=(value+size-1)//size
  events.setdefault(size,[]).append((old,new,multiplicity));old=new
answers={};keys=iter(sorted(events));nextsize=next(keys,None)
for size in sorted(set(queries)):
 while nextsize is not None and nextsize<=size:
  for old,new,multiplicity in events[nextsize]:
   total+=(new-old)*multiplicity;odd+=((new%2)-(old%2))*multiplicity
   den=den*pow(f[old]*iv[new]%p,multiplicity,p)%p
   halfden=halfden*pow(f[old//2]*iv[new//2]%p,multiplicity,p)%p
  nextsize=next(keys,None)
 ways=f[total]*den%p;pal=f[total//2]*halfden%p if odd<=1 else 0;answers[size]=(ways+pal)*((p+1)//2)%p
print('\n'.join(str(answers[size]) for size in queries))
