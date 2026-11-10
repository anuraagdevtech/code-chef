#!/usr/bin/env python3
"""Deterministic brute-force regressions for the 56 advanced_one solutions."""
import itertools as I, math, random, subprocess, sys, json
from collections import deque
from functools import lru_cache
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
import checkers_advanced_one as judges
ROOT=Path(__file__).resolve().parents[1]
rng=random.Random(927514);checks=0

def execute(code,inp):
 p=subprocess.run([sys.executable,'-I',str(ROOT/'solutions'/f'{code}.py')],input=inp,text=True,capture_output=True,timeout=30)
 assert p.returncode==0,(code,p.stderr);return p.stdout

def exact(code,cases,wants):
 global checks
 inp=str(len(cases))+'\n'+'\n'.join(cases)+'\n';got=execute(code,inp).split();expected=' '.join(map(str,wants)).split()
 assert [s.lower() for s in got]==[s.lower() for s in expected],(code, next(((i,a,b) for i,(a,b) in enumerate(zip(got,expected)) if a.lower()!=b.lower()),(got[:20],expected[:20])))
 checks+=len(cases)

def semantic(code,cases):
 global checks
 inp=str(len(cases))+'\n'+'\n'.join(cases)+'\n';out=execute(code,inp);ok,why=judges.CHECKERS[code](inp,out);assert ok,(code,why,out[:200]);checks+=len(cases)

# Every official sample, judged semantically when multiple answers are permitted.
def samples():
 global checks
 for code in (ROOT/'data/remaining.txt').read_text().split()[137:193]:
  raw=json.loads((ROOT/'data/raw'/f'{code}.json').read_text())
  for s in raw['problemComponents']['sampleTestCases']:
   inp=s.get('input','');want=s.get('output','');out=execute(code,inp)
   if code in judges.CHECKERS:
    fn=judges.CHECKERS[code]
    if hasattr(fn,'expected'):fn.expected=want.split()
    ok,why=fn(inp,out);assert ok,(code,why)
   else:assert out.lower().split()==want.lower().split(),(code,out,want)
   checks+=1

def core():
 cases=[];want=[]
 for n in range(2,1000):
  def tau(x):return sum(x%d==0 for d in range(1,x+1))
  ds=[k for k in range(2,n+1) if n%k==0];best=max(tau(n//k) for k in ds)
  cases.append(str(n));want.append(min(k for k in ds if tau(n//k)==best))
 exact('MXFACS',cases,want)
 cases=[];want=[]
 for n in range(2,8):
  for a in list(I.permutations(range(1,n+1)))[:300]:
   best=0
   for l in range(n):
    for r in range(l+1,n+1):
     b=a[:l]+a[r:]
     if b and sorted(b)==list(range(1,len(b)+1)):best=max(best,r-l)
   cases.append(str(n)+'\n'+' '.join(map(str,a)));want.append(best)
 exact('REMSUBARR',cases,want)
 cases=[];want=[]
 for n in range(1,9):
  for bits in I.product('01',repeat=n):
   s=''.join(bits)
   for k in (1,2,3,8,17):
    b=s
    for _ in range(k):b=''.join('1' if b[i]=='0' and ((i and b[i-1]=='1') or (i+1<n and b[i+1]=='1')) else '0' for i in range(n))
    cases.append(f'{n} {k}\n{s}');want.append(b)
 exact('ALTSUFF',cases,want)
 cases=[];want=[]
 beat={'R':'S','S':'P','P':'R'}
 for n in range(1,7):
  for a in I.product('RPS',repeat=n):
   ans=''
   for i in range(n):
    cur=a[i]
    for x in a[i+1:]:cur=cur if x==cur or beat[cur]==x else x
    ans+=cur
   cases.append(str(n)+'\n'+''.join(a));want.append(ans)
 exact('ROPASCI',cases,want)
 cases=[];want=[]
 for _ in range(150):
  a=[rng.randrange(128) for _ in range(rng.randrange(1,25))];ans=sum(str(a[i]^a[j])==str(a[i]^a[j])[::-1] for i in range(len(a)) for j in range(i,len(a)))
  cases.append(str(len(a))+'\n'+' '.join(map(str,a)));want.append(ans)
 # Exercise the Walsh-Hadamard branch against independent pair enumeration.
 a=list(range(3300));ans=sum(str(i^j)==str(i^j)[::-1] for i in a for j in range(i,3300));cases.append('3300\n'+' '.join(map(str,a)));want.append(ans)
 exact('PALIXOR',cases,want)
 semantic('DISTK',[f'{n} {k}' for n in range(1,30) for k in range(n,n*(n+1)//2+1)])
 cases=[];want=[]
 for a in range(1,65):
  for b in range(1,65):
   z=b;p=2;ok=True
   while p<=z:
    if z%p==0:
     if a%p:ok=False
     while z%p==0:z//=p
    p+=1
   cases.append(f'{a} {b}');want.append('YES' if ok else 'NO')
 exact('PRIMEFACDIV',cases,want)
 cases=[];want=[]
 for c in range(7):
  for a in range(1<<c):
   for b in rng.sample(range(1<<c),min(8,1<<c)):
    vals=[(b|x)-(a&x) for x in range(1<<c)];cases.append(f'{a} {b} {c}');want.append(vals.count(max(vals)))
 exact('MAXANDOR',cases,want)
 semantic('NOSEQ',[f'{n} {k} {s}' for n in range(1,6) for k in range(2,7) for s in range(1,80)])
 cases=[];want=[]
 for _ in range(150):
  n=rng.randrange(1,9);a=[rng.randrange(15) for _ in range(n)];b=[rng.randrange(15) for _ in range(n)];ans=min(max(c)-min(c) for c in I.product(*zip(a,b)))
  cases.append(f'{n}\n'+ ' '.join(map(str,a))+'\n'+' '.join(map(str,b)));want.append(ans)
 exact('SYMARRSWAP',cases,want)
 cases=[];want=[]
 def sequences(left,who=0):
  ans=0
  for v in range(1,5):
   if v>=left:ans+=who==0 and v==4
   else:ans+=sequences(left-v,who^(v==1))
  return ans
 for l in range(1,12):cases.append(str(l));want.append(sequences(l))
 exact('SPCP6',cases,want)
 cases=[];want=[]
 for n in range(1,8):
  for o in range(n+1):
   a=[2*i+1 for i in range(o)]+[2*i+2 for i in range(n-o)]
   for k in (0,1):
    ans=sum(all((p[i]+p[j])%2==k for i in range(n) for j in range(i+1,n) if (i+j)%2) for p in I.permutations(a))
    cases.append(f'{n} {k}\n'+' '.join(map(str,a)));want.append(ans)
 exact('PARPER',cases,want)
 # Distinct streak subsets enumerated independently.
 best={}
 for mask in range(1,1<<12):
  lens=[i+1 for i in range(12) if mask>>i&1];total=sum((1<<i)-1 for i in lens);minutes=sum(lens)+len(lens)-1
  best[total]=min(best.get(total,10**9),minutes)
 exact('BURGER',[f'1 {z}' for z in range(1,2000)],[best.get(z,-1) for z in range(1,2000)])
 semantic('SUMARRAY',[f'{n} {k}' for n in range(2,20,2) for k in range(1,130)]+['2 199999','2 200000','10 999995'])
 semantic('LCMMANIA',[str(n) for n in range(1,1000)])
 semantic('SUBARRAYXOR',[str(n) for n in (1,2,3,10,100,100000)])
 cases=[];want=[]
 for n in range(100):
  for k in range(1,40):
   cases.append(f'{n} {k}');want.append(max(range(n+1),key=lambda x:(x%k)*((n-x)%k)))
 inp=str(len(cases))+'\n'+'\n'.join(cases);got=list(map(int,execute('MAXIMALEXP',inp).split()))
 for case,x,y in zip(cases,got,want):n,k=map(int,case.split());assert (x%k)*((n-x)%k)==(y%k)*((n-y)%k)
 global checks;checks+=len(cases)
 cases=[]
 for n in range(1,9):
  for a in I.combinations_with_replacement(range(1,4),n):
   possible=any(all((p[i-1]<p[i]>p[i+1]) or (p[i-1]>p[i]<p[i+1]) for i in range(1,n-1)) for p in set(I.permutations(a)))
   case=f'{n}\n'+' '.join(map(str,a));out=execute('INTARR','1\n'+case).split();assert (out!=['-1'])==possible,('INTARR',a,out,possible)
   ok,why=judges.intarr('1\n'+case,' '.join(out));assert ok,('INTARR checker',a,why)
   checks+=1
 # Calendar exhaustive, one holiday flipped in each possible position.
 cases=[];want=[]
 for n in range(1,9):
  for bits in I.product('01',repeat=n):
   s=''.join(bits)
   for x in range(1,n+1):
    options=[s]+[s[:i]+'0'+s[i+1:] for i in range(n) if s[i]=='1'];ans=max(sum(len(r)//x for r in b.split('1')) for b in options)
    cases.append(f'{n} {x}\n{s}');want.append(ans)
 exact('MAXVAC',cases,want)
 cases=[];want=[]
 for x in range(1,1000):
  n=1
  # First hits occur at squares; enumerate with exact cube correction.
  j=x
  while True:
   n=j*j;c=round(n**(1/3))
   while (c+1)**3<=n:c+=1
   while c**3>n:c-=1
   if j-c>=x:break
   j+=1
  cases.append(str(x));want.append(n)
 exact('SQRTCBRT',cases,want)
 cases=[];want=[]
 for n in range(1,65):
  ans=sum(x+y+z==n and x|y|z==n for x in range(1,n) for y in range(1,n) for z in range(1,n))
  cases.append(str(n));want.append(ans)
 exact('AWESUM_OR',cases,want)
 cases=[];want=[]
 for _ in range(80):
  n=rng.randrange(1,8);a=[rng.randrange(1,8) for _ in range(n)];b=[rng.randrange(1,8) for _ in range(n)]
  ans=0
  for p in I.permutations(range(n)):
   pos=value=0
   for i in p:value+=pos*b[i];pos+=a[i]
   ans=max(ans,value)
  cases.append(f'{n}\n'+' '.join(map(str,a))+'\n'+' '.join(map(str,b)));want.append(ans)
 exact('MUSROD',cases,want)
 semantic('SUBSBIN',[f'{n}\n'+''.join(b) for n in range(1,9) for b in I.product('01',repeat=n)])
 # Full BFS of binary strings gives exact adjacent-swap distances to multiples of three.
 cases=[];want=[]
 for n in range(1,11):
  dist={};q=deque()
  for x in range(1<<n):
   if x%3==0:dist[x]=0;q.append(x)
  while q:
   x=q.popleft()
   for i in range(n-1):
    if (x>>i&1)!=(x>>(i+1)&1):
     y=x^(3<<i)
     if y not in dist:dist[y]=dist[x]+1;q.append(y)
  for x in range(1<<n):cases.append(f'{x:0{n}b}');want.append(dist.get(x,-1))
 exact('DIVBY3',cases,want)
 cases=[];want=[]
 for n in range(1,8):
  for _ in range(40):
   a=[rng.randrange(1,n+1) for _ in range(n)];ans=0
   for mask in range(1,1<<n):b=sorted(a[i] for i in range(n) if mask>>i&1);ans+=sum(v==i+1 for i,v in enumerate(b))
   cases.append(f'{n}\n'+' '.join(map(str,a)));want.append(ans)
 exact('SEQGOODNESS',cases,want)
 semantic('MINIMUMOP',[f'{n} {m}\n'+' '.join(map(str,[rng.randrange(2,m+1) for _ in range(n)])) for m in range(2,40) for n in range(1,15)])
 cases=[];want=[]
 for n in range(1,9):
  for _ in range(30):
   a=[rng.randrange(1,65) for _ in range(n)];sums=[sum(a[i] for i in range(n) if mask>>i&1) for mask in range(1<<n)];ans=0
   for s in sums:ans|=s
   cases.append(f'{n}\n'+' '.join(map(str,a)));want.append(ans)
 exact('SSO',cases,want)
 semantic('PARPERM',[f'{n} {k}' for n in range(2,80) for k in range(1,n)])

if __name__=='__main__':
 samples();core();import test_advanced_one_extra;test_advanced_one_extra.run(sys.modules[__name__]);print(f'PASS: {checks} deterministic sample, exhaustive, and differential cases')
