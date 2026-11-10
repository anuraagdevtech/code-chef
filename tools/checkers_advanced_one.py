"""Semantic judges for advanced_one constructions and numerical answers."""
import math
from collections import Counter
from functools import wraps

def guarded(fn):
 @wraps(fn)
 def check(inp,out):
  try:fn(list(map(int,inp.split())),list(map(int,out.split())));return True,''
  except (AssertionError,ValueError,IndexError,StopIteration) as e:return False,str(e) or 'invalid construction'
 return check

def integer_cases(fn):
 @guarded
 def check(inp,out):
  it=iter(inp);ot=iter(out)
  for _ in range(next(it)):fn(it,ot)
  assert next(ot,None) is None,'extra output'
 return check

@integer_cases
def distk(it,ot):
 n=next(it);k=next(it);a=[next(ot) for _ in range(n)];assert all(1<=v<=n for v in a)
 last={};left=ans=0
 for i,v in enumerate(a):left=max(left,last.get(v,-1)+1);last[v]=i;ans+=i-left+1
 assert ans==k,'wrong number of distinct subarrays'

@integer_cases
def sumarray(it,ot):
 n=next(it);k=next(it);first=next(ot)
 possible=3*(n//2)<=k<=199999*(n//2) and (k-3*(n//2))%2==0
 if first==-1:assert not possible;return
 a=[first]+[next(ot) for _ in range(n-1)]
 assert all(1<=x<=100000 for x in a) and sum(a)==k and sum(x%2 for x in a)==n//2

@integer_cases
def lcmmania(it,ot):
 n=next(it);a=next(ot)
 if a==-1:assert n&(n-1)==0;return
 b=next(ot);c=next(ot);assert min(a,b,c)>0 and math.lcm(a,b)+math.lcm(b,c)+math.lcm(c,a)==n

@integer_cases
def subarrayxor(it,ot):
 n=next(it);seen={0};prefix=0
 for _ in range(n):
  x=next(ot);assert 1<=x<=1000000;prefix^=x;assert prefix not in seen;seen.add(prefix)

@integer_cases
def maximalexp(it,ot):
 n=next(it);k=next(it);x=next(ot);assert 0<=x<=n
 r=n%k;totals=[r]+([r+k] if n>=k and r<=k-2 else [])
 best=max((s//2)*((s+1)//2) for s in totals)
 assert (x%k)*((n-x)%k)==best

@integer_cases
def noseq(it,ot):
 n=next(it);k=next(it);s=next(it);a=next(ot)
 if a==-2:
  for _ in range(n):
   r=s%k
   if r not in (0,1,k-1):return
   s=(s-(0 if r==0 else 1 if r==1 else -1))//k
  assert s!=0;return
 vals=[a]+[next(ot) for _ in range(n-1)]
 assert all(-1<=x<=1 for x in vals) and sum(x*k**i for i,x in enumerate(vals))==s

@integer_cases
def intarr(it,ot):
 n=next(it);a=[next(it) for _ in range(n)];v=next(ot)
 if v==-1:
  assert n>2
  # Necessary and sufficient: one of the two alternating orientations has enough strict low/high values.
  a.sort();h=n//2
  valley=all(a[i]<a[h+i] for i in range(h)) if n%2==0 else all(a[i]<a[h+1+i] for i in range(h)) and (h==0 or a[h]<a[h+1])
  peak=all(a[i]<a[(n+1)//2+i] for i in range(h)) if n%2==0 else all(a[i]<a[h+i] for i in range(h)) and (h==0 or a[h-1]<a[h])
  assert not valley and not peak;return
 b=[v]+[next(ot) for _ in range(n-1)]
 assert Counter(a)==Counter(b)
 assert all((b[i-1]<b[i]>b[i+1]) or (b[i-1]>b[i]<b[i+1]) for i in range(1,n-1))

def parperm(inp,out):
 try:
  it=iter(map(int,inp.split()));ot=iter(out.split())
  for _ in range(next(it)):
   n=next(it);k=next(it);answer=next(ot).lower();assert answer in ('yes','no')
   p=list(range(n+1))
   def root(x):
    while p[x]!=x:p[x]=p[p[x]];x=p[x]
    return x
   for d in range(2,n+1):
    for m in range(2*d,n+1,d):p[root(m)]=root(d)
   sizes=Counter(root(i) for i in range(1,n+1));possible=k<=sum(s==1 for s in sizes.values()) or n-k<=sum(s==1 for s in sizes.values())
   if answer=='no':assert not possible;continue
   a={int(next(ot)) for _ in range(k)};assert len(a)==k and all(1<=x<=n for x in a)
   flags={}
   for i in range(1,n+1):r=root(i);flag=i in a;assert r not in flags or flags[r]==flag;flags[r]=flag
  assert next(ot,None) is None;return True,''
 except (AssertionError,ValueError,StopIteration):return False,'invalid coprime partition'

@guarded
def mountain(inp,out):
 it=iter(inp);ot=iter(out);n=next(it);m=next(it);q=next(it)
 for _ in range(q):
  s=next(it);p=next(ot);assert p!=-1;k=next(ot);assert 1<=p and 1<=k and p+k-1<=n
  a=[next(ot) for _ in range(k)];assert all(1<=v<=m for v in a) and sum((p+i)*v for i,v in enumerate(a))==s
 assert next(ot,None) is None

def subsbin(inp,out):
 try:
  it=iter(inp.split());ot=iter(out.split())
  for _ in range(int(next(it))):
   n=int(next(it));s=next(it);m=int(next(ot));k=int(next(ot));z=s.count('0');o=n-z
   assert (m,k)==((n,0) if min(z,o)==0 else (1,abs(z-o)+1))
   for _ in range(k):
    l=int(next(ot))-1;r=int(next(ot));b=next(ot);assert b in ('0','1') and 0<=l<r-1<len(s)
    sub=s[l:r];assert sub.count('0')*2==len(sub);s=s[:l]+b+s[r:]
   assert len(s)==m
  assert next(ot,None) is None;return True,''
 except (AssertionError,ValueError,StopIteration):return False,'invalid balanced-substring reduction'

@integer_cases
def minimumop(it,ot):
 n=next(it);m=next(it);a=[next(it) for _ in range(n)];k=next(ot);xs=[next(ot) for _ in range(k)]
 assert 0<=k<=2 and all(2<=x<=m for x in xs)
 b=a[:]
 for x in xs:b=[math.gcd(v,x) for v in b]
 assert len(set(b))==1
 if len(set(a))==1:assert k==0;return
 g=math.gcd(*a)
 if g>1:assert k==1;return
 # If a one-operation answer exists, a prime factor of X also works.
 sieve=bytearray(b'\1')*(m+1);sieve[:2]=b'\0\0';bad=set()
 for d in range(2,m+1):
  if sieve[d]:
   if not any(x%d==0 for x in a):assert k==1;return
   sieve[d*d:m+1:d]=b'\0'*max(0,(m-d*d)//d+1)
 assert k==2

@integer_cases
def mexyarr(it,ot):
 n=next(it);b=[next(it) for _ in range(n)];a=next(ot)
 if a!=-1:
  vals=[a]+[next(ot) for _ in range(n-1)];seen=set();mex=0
  for v,w in zip(vals,b):
   assert 0<=v<=10**9;seen.add(v)
   while mex in seen:mex+=1
   assert w==-1 or w==mex
  return
 # Independent interval scheduling feasibility test for numbers required by known mexes.
 known=[(i+1,v) for i,v in enumerate(b) if v>=0]
 if any(v>i for i,v in known) or any(known[j][1]<known[j-1][1] for j in range(1,len(known))):return
 last={v:i for i,v in known};mx=max([0]+[v for i,v in known]);parent=list(range(n+2))
 def find(x):
  while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
  return x
 j=0
 for v in range(mx):
  while known[j][1]<=v:j+=1
  slot=find(last.get(v,0)+1)
  if slot>known[j][0]:return
  parent[slot]=find(slot+1)
 assert False,'reported impossible for a feasible mex sequence'

def floating(inp,out):
 try:
  got=list(map(float,out.split()));want=list(map(float,floating.expected));assert len(got)==len(want)
  assert all(math.isfinite(x) and abs(x-y)<=1e-6*max(1,abs(y)) for x,y in zip(got,want));return True,''
 except (AssertionError,ValueError):return False,'floating answer differs beyond tolerance'
floating.expected=[]
CHECKERS={'DISTK':distk,'SUMARRAY':sumarray,'LCMMANIA':lcmmania,'SUBARRAYXOR':subarrayxor,'MAXIMALEXP':maximalexp,'NOSEQ':noseq,'INTARR':intarr,'PARPERM':parperm,'MOUNTAIN':mountain,'SUBSBIN':subsbin,'MINIMUMOP':minimumop,'MEXYARR':mexyarr,'GOLMINE':floating,'ICM2003':floating}
