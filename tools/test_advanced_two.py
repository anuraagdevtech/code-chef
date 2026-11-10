#!/usr/bin/env python3
"""Deterministic differential and constructive tests for the 56-code final batch."""
import importlib.util,itertools as I,json,random,subprocess,sys
from collections import Counter,deque
from functools import lru_cache
from math import gcd,isqrt
from pathlib import Path
from checkers_advanced_two import CHECKERS
R=Path(__file__).resolve().parents[1];rng=random.Random(749102);mods={};checks=0

def load(code):
 if code not in mods:
  spec=importlib.util.spec_from_file_location(code,R/'solutions'/f'{code}.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);mods[code]=m
 return mods[code]

def run(code,inp):
 p=subprocess.run([sys.executable,'-I',str(R/'solutions'/f'{code}.py')],input=inp,text=True,capture_output=True,timeout=45)
 assert p.returncode==0,(code,p.stderr)
 return p.stdout.strip()

def eq(code,tokens,want,text=False):
 global checks
 got=load(code).solve(iter(str(x).encode() if text else x for x in tokens));assert got.lower()==str(want).lower(),(code,tokens,want,got);checks+=1

def valid(code,inp):
 global checks
 out=run(code,inp);ok,why=CHECKERS[code](inp,out);assert ok,(code,inp,out,why);checks+=1

# Legacy HTML examples without structured sampleTestCases.
legacy=[
 ('ANUMLA','2\n1\n0 10\n2\n0 1 1 2\n','10\n1 1'),
 ('DIANE','4\n2\n5\n200\n13\n',None),
 ('TSHIRTS','2\n2\n3 5\n8 100\n3\n5 100 1\n2\n5 100\n','4\n4'),
 ('KSUM','3 4\n1 3 4\n','8 7 4 4'),
 ('KSUM','3 3\n10 2 7\n','19 12 10'),
 ('ABCSTR','ABACABA\n','2'),
 ('ABROADS','3 3 6\n1 2 3\n1 2\n2 3\n3 1\nP 1 3\nD 1\nP 2 3\nD 2\nP 3 10\nD 3\n','8\n8\n9\n6\n13\n10'),
 ('CHEFQUE','5 1 1 1\n','3'),
 ('TDISTS','4\n2 2\n29 20\n3 12\n6 3\n',None),
]
for code,inp,want in legacy:
 out=run(code,inp)
 if code in CHECKERS:ok,why=CHECKERS[code](inp,out);assert ok,(code,why)
 else:assert out.split()==want.split(),(code,out,want)
 checks+=1

# Sample cases, including all semantic checkers in this batch.
for code in (R/'data'/'remaining.txt').read_text().split()[193:]:
 raw=json.loads((R/'data'/'raw'/f'{code}.json').read_text())
 for sample in raw['problemComponents'].get('sampleTestCases',[]):
  out=run(code,sample['input'])
  if code in CHECKERS:ok,why=CHECKERS[code](sample['input'],out);assert ok,(code,why)
  else:assert out.split()==sample['output'].strip().split() or out.lower().split()==sample['output'].lower().split(),(code,out,sample['output'])
  checks+=1

for n in range(1,8):
 for t in I.product('01',repeat=n):
  s=''.join(t);v=[int(x) for x in s]
  weight=lambda a:sum(x*(i+1)*(n-i) for i,x in enumerate(a))
  want=max(weight(v[:l]+[1-x for x in v[l:r]]+v[r:]) for l in range(n+1) for r in range(l,n+1))
  eq('MAX1S',[s],want,True)
  seen={s};q=deque([s])
  while q:
   a=q.popleft()
   for i in range(n-1):
    if a[i]==a[i+1]:
     b=a[:i]+str(1-int(a[i]))*2+a[i+2:]
     if b not in seen:seen.add(b);q.append(b)
  eq('ADJFLIP',[n,s],'Yes' if '0'*n in seen or '1'*n in seen else 'No',True)
  eq('MAXCYCSHIFT',[n]+v,max(len(set(I.accumulate(v[j:]+v[:j],lambda x,y:x^y))) for j in range(n)))

# Independently enumerate reversal equivalence classes for small binary strings.
classes={}
for n in range(1,8):
 unseen={''.join(t) for t in I.product('01',repeat=n)}
 while unseen:
  s=min(unseen);unseen.remove(s);q=deque([s]);classes[s]=s
  while q:
   a=q.popleft()
   for l in range(n):
    for r in range(l+1,n+1):
     if a[l:r].count('1')%2==0:
      b=a[:l]+a[l:r][::-1]+a[r:]
      if b in unseen:unseen.remove(b);classes[b]=s;q.append(b)
for n in range(1,8):
 for t in I.product('01',repeat=n):
  s=''.join(t);want=len({classes[s[l:r]] for l in range(n) for r in range(l+1,n+1)});eq('STROPERS',[s],want,True)

@lru_cache(None)
def game(a):
 if not any(a):return False
 for i,x in enumerate(a):
  if x:
   b=list(a);b[i]-=1
   if not game(tuple(sorted(b))):return True
 return min(a)>0 and not game(tuple(x-1 for x in a))
for n in range(1,7):
 for a in I.combinations_with_replacement(range(1,5),n):eq('ONEORALL',[n]+list(a),'CHEF' if game(a) else 'CHEFINA')

for _ in range(180):
 n=rng.randint(2,8);a=[rng.randint(1,9) for _ in range(n)]
 diffs={sorted(a[l:r])[-1]-sorted(a[l:r])[-2] for l in range(n) for r in range(l+2,n+1)};eq('DIST_VALS',[n]+a,len(diffs))
 eq('SUMOFCUBE',[n]+a,sum(sum(a[l:r])**3 for l in range(n) for r in range(l+1,n+1))%998244353)
 weird=0
 for l in range(n):
  for r in range(l+1,n+1):c=Counter(a[l:r]);weird+=sum(x for x,v in c.items() if x==v)
 eq('WRDVLS',[n]+a,weird)
 k=rng.randint(1,8);want=0
 for mask in range(1<<n):
  b=[a[i] for i in range(n) if mask>>i&1]
  want+=all((x+y)%k for i,x in enumerate(b) for y in b[i+1:])
 eq('SIMPLEARRAY',[n,k]+a,want)
 vals=[]
 for l in range(n):
  for r in range(l+1,n+1):
   x=y=0
   for z in a[l:r]:x|=z
   for z in a[:l]+a[r:]:y|=z
   if x==y:vals.append(r-l)
 eq('LONGESTARRAY',[n]+a,max(vals,default=-1))
 for c in ('GSEQ','CONSTANARRAY'):
  v=[rng.randrange(2) for _ in range(n)] if c=='GSEQ' else [rng.randint(1,n) for _ in range(n)]
  inp='1\n'+str(n)+(' '+str(n) if c=='CONSTANARRAY' else '')+'\n'+' '.join(map(str,v))+'\n';out=load(c).solve(iter([n]+([n] if c=='CONSTANARRAY' else [])+v));ok,why=CHECKERS[c](inp,out);assert ok,(c,inp,out,why);checks+=1
 b=[rng.randint(-5,5) for _ in range(n)];k=rng.randint(1,min(3,n))
 def brute_sub(start,j):
  if j>k:return 0
  return max((sum(b[l:r])*j+brute_sub(r,j+1) for l in range(start,n) for r in range(l+1,n+1) if n-r>=k-j),default=-10**15)
 eq('CHESUB',[n,k]+b,brute_sub(0,1))
 # Exhaustive assignments and two nonempty piles.
 pairs=[(rng.randint(1,12),rng.randint(1,12)) for _ in range(min(n,5))];want=10**9
 for chosen in I.product(*pairs):
  for mask in range(1,(1<<len(chosen))-1):
   want=min(want,abs(max(x for i,x in enumerate(chosen) if mask>>i&1)-max(x for i,x in enumerate(chosen) if not mask>>i&1)))
 eq('SPLITMIN',[len(pairs)]+[x for p in pairs for x in p],want)
 # Enumerate partitions for MEXSUB.
 v=[rng.randrange(5) for _ in range(n)];want=0
 for mask in range(1<<(n-1)):
  parts=[];start=0
  for i in range(n):
   if i==n-1 or mask>>i&1:parts.append(set(v[start:i+1]));start=i+1
  mex=[]
  for p in parts:
   x=0
   while x in p:x+=1
   mex.append(x)
  want+=len(set(mex))==1
 eq('MEXSUB',[n]+v,want)
 # Two-counter unrestricted brute force states.
 times=sorted(rng.sample(range(1,n+1),rng.randint(1,n)));types=[rng.randint(1,2) for _ in times];events=dict(zip(times,types));dp={0:0}
 for minute in range(1,n+1):
  nd={}
  for d,score in dp.items():
   for x in (d-1,d+1):
    s=score
    if minute in events:
     if (x>0 and events[minute]==1) or (x<0 and events[minute]==2):s+=1
     else:x=0
    nd[x]=max(nd.get(x,-1),s)
  dp=nd
 eq('TWOCOUNTERS',[n,len(times)]+times+types,max(dp.values()))

for _ in range(200):
 a,b,c=[rng.randrange(32) for _ in range(3)];want=any((a^x)+(b^x)==(c^x) for x in range(128));eq('EXISTENCEOFX',[a,b,c],'YES' if want else 'NO')
 l=rng.randint(1,300);r=rng.randint(l,500)
 def f(x):return x.bit_length()-x.bit_count()
 def g(x):return 3*(1<<(x.bit_length()-1))-1-x
 eq('CHEFFFUNC',[l,r],max(f(x)+g(x) for x in range(l,r+1)))
 n,m,k=rng.randint(1,5),rng.randint(1,5),rng.randint(1,6);a=[rng.randint(1,k) for _ in range(n)];b=[rng.randint(1,k) for _ in range(m)];sa,sb=sum(a),sum(b);want=-1
 if k>1:
  for z in range(100):
   if any((sa+k*x)*(m+z-x)>(sb+z-x)*(n+x) for x in range(z+1)):want=z;break
 eq('TWOAVG',[n,m,k]+a+b,want)

for _ in range(50):
 n=rng.randint(1,8);a=[rng.randrange(32) for _ in range(n)];want=[]
 for k in range(1,n+1):
  total=0
  for mask in range(1,1<<n):
   if mask.bit_count()<=k:
    x=0
    for j,z in enumerate(a):
     if mask>>j&1:x^=z
    total+=x
  want.append(total%998244353)
 inp=str(n)+'\n'+' '.join(map(str,a))+'\n'+str(n)+'\n'+'\n'.join(map(str,range(1,n+1)))+'\n';assert list(map(int,run('SUMXOR2',inp).split()))==want;checks+=1

# Exhaustive valid grids confirm the SMALLESTDIFF optimum formula for the 2x3 case.
best=10**9
for p in I.permutations(range(1,7)):
 i=j=0;path=[p[0]]
 while i<1 or j<2:
  if i==1:j+=1
  elif j==2:i+=1
  elif ((i+j)%2==0 and p[(i+1)*3+j]>p[i*3+j+1]) or ((i+j)%2 and p[(i+1)*3+j]<p[i*3+j+1]):i+=1
  else:j+=1
  path.append(p[i*3+j])
 best=min(best,max(path)-min(path))
assert best==3
for n in range(2,8):
 for m in range(2,8):
  a=rng.sample(range(1,10000),n*m);inp='1\n'+f'{n} {m}\n'+' '.join(map(str,a))+'\n';out=load('SMALLESTDIFF').solve(iter([n,m]+a));ok,why=CHECKERS['SMALLESTDIFF'](inp,out);assert ok,(inp,out,why);checks+=1

for code,values in [('DIANE',[0,1,2,5,99997,99998,99999,10**9]),('INTREP',[1,2,3,8,135,6508915847719005,10**16])]:
 valid(code,str(len(values))+'\n'+'\n'.join(map(str,values))+'\n')
valid('ALTDIA','9\n1 0\n0 1\n0 2\n2 0\n1 1\n1 2\n2 1\n3 3\n100 90\n')

# Reconstruction from shuffled subset sums.
for _ in range(100):
 n=rng.randint(1,9);a=[rng.randint(1,25) for _ in range(n)];sums=[0]
 for x in a:sums += [s+x for s in sums]
 rng.shuffle(sums);eq('ANUMLA',[n]+sums,' '.join(map(str,sorted(a))))

for _ in range(120):
 n=rng.randint(2,8);a=[rng.randint(2,50) for _ in range(n)];validcuts=[]
 from math import prod
 for j in range(1,n):
  if gcd(prod(a[:j]),prod(a[j:]))==1:validcuts.append(j)
 if validcuts:eq('COPAR',[n]+a,min(validcuts))
 # Sequential permutation assignment versus enumerating zero replacements.
 n=rng.randint(1,5);m=rng.randint(1,3);p=list(range(n));rng.shuffle(p);a=[rng.randint(0,m) for _ in range(n)];zero=[i for i,x in enumerate(a) if not x];want=0
 for fill in I.product(range(1,m+1),repeat=len(zero)):
  b=a.copy()
  for i,x in zip(zero,fill):b[i]=x
  for i in range(n):b[i]=b[p[i]]
  want+=len(set(b))==1
 eq('ALIKE_THEM',[n,m]+[x+1 for x in p]+a,want)
 # Gifts versus forward simulation of every candidate initial group.
 b=rng.randint(1,4);c=rng.randint(0,3);positions=rng.sample(range(1,20),b+c);dishes=[(positions[i],rng.randint(1,5)) for i in range(b)];clans=[(positions[b+i],rng.randint(1,7),rng.randint(1,5)) for i in range(c)];ev=sorted([(p,0,x,0) for p,x in dishes]+[(p,1,q,r) for p,q,r in clans]);want=None
 for initial in range(1,30):
  size=initial
  for _,kind,x,y in ev:
   if kind==0:size-=x
   elif size>=x:size+=y
   if size<1:break
  if size>=1:want=initial;break
 eq('ASHIGIFT',[20,b]+[x for p in sorted(dishes) for x in p]+[c]+[x for p in sorted(clans) for x in p],want)
 # Enumerate wildcard replacements and triples for 404.
 n=rng.randint(1,8);s=''.join(rng.choice('40*') for _ in range(n));zero=[i for i,x in enumerate(s) if x=='*'];want=0
 for fill in I.product('40',repeat=len(zero)):
  a=list(s)
  for i,x in zip(zero,fill):a[i]=x
  want+=sum(''.join(a[i] for i in inds)=='404' for inds in I.combinations(range(n),3))
 eq('CS2023_404',[n,s],want,True)
 # Merge all interleavings.
 n=rng.randint(1,5);a=''.join(rng.choice('01') for _ in range(n));b=''.join(rng.choice('01') for _ in range(n));want=10**9
 for inds in I.combinations(range(2*n),n):
  inds=set(inds);ai=bi=0;s=[]
  for i in range(2*n):
   if i in inds:s.append(a[ai]);ai+=1
   else:s.append(b[bi]);bi+=1
  want=min(want,sum(s[i]=='1' and s[j]=='0' for i in range(2*n) for j in range(i+1,2*n)))
 eq('MERGEBS',[n,a,b],want,True)

# Interval +/-1 moves on mirrored differences, solved by exhaustive BFS.
for m in range(1,4):
 start=(0,)*m;dist={start:0};q=deque([start])
 while q:
  a=q.popleft()
  for l in range(m):
   for r in range(l+1,m+1):
    for x in (-1,1):
     b=a[:l]+tuple(v+x for v in a[l:r])+a[r:]
     if max(map(abs,b))<=2 and b not in dist:dist[b]=dist[a]+1;q.append(b)
 for d,want in dist.items():
  a=[5+x for x in d]+[5]*m;eq('MAKEPAL3',[2*m]+a,want)

# Tiny MST reference for compressed bit-clique Kruskal.
for _ in range(80):
 n=rng.randint(1,7);a=[rng.randrange(16) for _ in range(n)];p=list(range(n))
 def root(x):
  while p[x]!=x:x=p[x]
  return x
 edges=[]
 for i in range(n):
  for j in range(i):
   shared=a[i]&a[j]
   if shared:edges.append((shared&-shared,i,j))
 ans=0;cnt=0
 for w,u,v in sorted(edges):
  u,v=root(u),root(v)
  if u!=v:p[u]=v;ans+=w;cnt+=1
 eq('CNCTCT',[n]+a,ans if cnt==n-1 else -1)
 # Indexed gcd-removal brute force.
 a=[rng.randint(1,50) for _ in range(n)];xs=[rng.randint(1,50) for _ in range(n)];b=a.copy();want=[]
 for x in xs:
  v=min((v for v in b if gcd(x,v)>1),default=min(b));want.append(v);b.remove(v)
 eq('GCD_QUERIES',[n]+a+[n]+xs,' '.join(map(str,want)))
 # Candy prices versus direct integer divisions.
 m=rng.randint(1,10);a=[rng.randint(1,m) for _ in range(n)];c=[rng.randint(1,20) for _ in range(m)];eq('CANDIES3',[n,m]+a+c,max(c[p-1]*sum(x//p for x in a) for p in range(1,m+1)))
 # A source at each special node, scores computed with independent BFS.
 n=rng.randint(1,12);edges=[(i,rng.randrange(i)) for i in range(1,n)];g=[[] for _ in range(n)]
 for u,v in edges:g[u].append(v);g[v].append(u)
 def distances(root):
  d=[-1]*n;d[root]=0;q=deque([root])
  while q:
   u=q.popleft()
   for v in g[u]:
    if d[v]<0:d[v]=d[u]+1;q.append(v)
  return d
 k=rng.randint(1,n);special=rng.sample(range(n),k);root=rng.randrange(n);d=distances(root);want=[max(d[u]-distances(u)[b] for u in special) for b in range(n)];tokens=[n,k,root+1]+[u+1 for u in special]+[x+1 for e in edges for x in e];got=load('SPTREE').solve(iter(tokens)).splitlines();assert list(map(int,got[0].split()))==want
 for b,u in enumerate(map(int,got[1].split())):assert u-1 in special and d[u-1]-distances(u-1)[b]==want[b]
 checks+=1

# True event-driven ant motion with exact rational coordinates.
from fractions import Fraction
for _ in range(100):
 lines=[sorted(rng.sample([x for x in range(-5,6) if x],rng.randint(1,4))) for _ in range(rng.randint(1,3))];ants=[[line,Fraction(x),1 if x<0 else -1] for line,a in enumerate(lines) for x in a];want=0
 for step in range(200):
  times=[]
  for i,(line,x,v) in enumerate(ants):
   for line2,y,w in ants[i+1:]:
    if line==line2 and v!=w:
     dt=(y-x)/(v-w)
     if dt>0:times.append(dt)
  central=Counter(-x/v for _,x,v in ants if -x/v>0)
  times += [dt for dt,count in central.items() if count>=2]
  if not times:break
  dt=min(times)
  for ant in ants:ant[1]+=dt*ant[2]
  groups={}
  for i,(line,x,v) in enumerate(ants):groups.setdefault(('origin',0) if x==0 else (line,x),[]).append(i)
  for group in groups.values():
   if len(group)>=2:
    want+=1
    for i in group:ants[i][2]*=-1
 else:raise AssertionError('ant simulation did not terminate')
 eq('ANTSCHEF',[len(lines)]+[x for a in lines for x in [len(a)]+a],want)

# Exhaustive square-product subsequences, batched to avoid repeated large sieve startup.
cases=[];wants=[]
for _ in range(100):
 n=rng.randint(1,8);a=[rng.randint(1,100) for _ in range(n)];want=0
 for mask in range(1,1<<n):
  b=[a[i] for i in range(n) if mask>>i&1]
  if all((isqrt(x)*isqrt(x)==x)==(sub.bit_count()%2==0) for sub in range(1,1<<len(b)) for x in [prod(b[i] for i in range(len(b)) if sub>>i&1)]):want=max(want,len(b))
 cases.append(str(n)+'\n'+' '.join(map(str,a)));wants.append(want)
assert list(map(int,run('SQUAR',str(len(cases))+'\n'+'\n'.join(cases)).split()))==wants;checks+=len(cases)

# The generated-query bitmap versus a normal set.
for _ in range(5):
 q=rng.randint(1,1000);s,a,b=[rng.randint(1,100) for _ in range(3)];x=s;v=set()
 for i in range(q):
  if x&1:v.add(x>>1)
  else:v.discard(x>>1)
  x=(a*x+b)&((1<<32)-1)
 assert int(run('CHEFQUE',f'{q} {s} {a} {b}\n'))==sum(v);checks+=1


# Legacy statement samples are not always present in sampleTestCases: cover their algorithms directly.
for _ in range(35):
 n=rng.randint(1,8);a=[rng.randint(1,12) for _ in range(n)];sums=sorted((sum(a[l:r]) for l in range(n) for r in range(l+1,n+1)),reverse=True);k=rng.randint(1,len(sums));inp=f'{n} {k}\n'+' '.join(map(str,a))+'\n';assert list(map(int,run('KSUM',inp).split()))==sums[:k];checks+=1
 s=''.join(rng.choice('ABC') for _ in range(n));want=sum(len(set(Counter(s[l:r]).get(c,0) for c in 'ABC'))==1 for l in range(n) for r in range(l+1,n+1));assert int(run('ABCSTR',s+'\n'))==want;checks+=1

cases=[];wants=[]
for _ in range(50):
 n=rng.randint(1,5);shirts=[sorted(rng.sample(range(1,8),rng.randint(1,5))) for _ in range(n)];wants.append(sum(len(set(v))==n for v in I.product(*shirts)));cases.append(str(n)+'\n'+'\n'.join(' '.join(map(str,a)) for a in shirts))
assert list(map(int,run('TSHIRTS',str(len(cases))+'\n'+'\n'.join(cases)+'\n').split()))==wants;checks+=len(cases)

for _ in range(100):
 n=rng.randint(1,3);a=[rng.randint(1,4) for _ in range(n)];b=[rng.randint(1,4) for _ in range(n)];ca=[rng.randint(0,2) for _ in range(n)];cb=[rng.randint(0,2) for _ in range(n)];seen={(tuple(a),tuple(b))};q=deque(seen);want=False
 while q:
  x,y=q.popleft()
  if list(x)==sorted(x):want=True;break
  for i in range(n):
   for j in range(n):
    if ca[i]==cb[j]:
     xx,yy=list(x),list(y);xx[i],yy[j]=yy[j],xx[i];v=tuple(xx),tuple(yy)
     if v not in seen:seen.add(v);q.append(v)
 eq('ASH57',[n]+a+ca+b+cb,'Yes' if want else 'No')
 n=rng.randint(1,6);w=[rng.randint(1,3) for _ in range(n)];a=[x+rng.randint(1,4) for x in w];want=[]
 for source in range(n):
  for add in range(50):
   total=w[source]+add
   if total<a[source]:continue
   possible=False
   for left in range(total+1):
    weight=left;ok=True
    for j in range(source-1,-1,-1):
     weight+=w[j]
     if weight<a[j]:ok=False;break
    weight=total-left
    for j in range(source+1,n):
     weight+=w[j]
     if weight<a[j]:ok=False;break
    if ok:possible=True;break
   if possible:want.append(add);break
 eq('CHANDWEIGHT',[n]+w+a,' '.join(map(str,want)))
 n=rng.randint(1,7);m=rng.randint(n+1,30);a=rng.sample(range(1,m),n);posts=[0,m];want=[]
 for x in a:posts.append(x);posts.sort();want.append(max(y-x for x,y in zip(posts,posts[1:])))
 eq('KEEPOUT',[n,m]+a,' '.join(map(str,want)))
 n=2*rng.randint(1,8);k=rng.randint(1,20);v=list(range(1,n+1))
 for _ in range(k):v=v[::2]+v[1::2]
 eq('RIFFLES',[n,k],' '.join(map(str,v)))

for _ in range(40):
 n=rng.randint(1,7);edges=[(i,j) for i in range(n) for j in range(i) if rng.randrange(3)==0];a=[rng.randint(1,3) for _ in range(n)];reach=[[False]*n for _ in range(n)]
 for i in range(n):reach[i][i]=True
 for u,v in edges:reach[u][v]=reach[v][u]=True
 for k in range(n):
  for i in range(n):
   for j in range(n):reach[i][j]|=reach[i][k] and reach[k][j]
 want=0
 for p in I.permutations(range(n)):
  want+=all(not reach[u][v] or a[u]<=a[v] for i,u in enumerate(p) for v in p[i+1:])
 eq('SPOOKYSEQ',[n,len(edges)]+[x+1 for e in edges for x in e]+a,want)

# Dynamic connectivity against rebuilding components after each change.
for _ in range(30):
 n=rng.randint(2,8);edges=[(i,j) for i in range(n) for j in range(i) if rng.randrange(2)];m=len(edges);a=[rng.randint(1,20) for _ in range(n)];cur=a.copy();live=set(range(m));queries=[];want=[]
 for step in range(12):
  if live and rng.randrange(2):
   e=rng.choice(sorted(live));queries.append(f'D {e+1}');live.remove(e)
  else:
   u=rng.randrange(n);x=rng.randint(1,20);queries.append(f'P {u+1} {x}');cur[u]=x
  g=[[] for _ in range(n)]
  for e in live:u,v=edges[e];g[u].append(v);g[v].append(u)
  seen=set();best=0
  for i in range(n):
   if i in seen:continue
   seen.add(i);q=[i];total=0
   for u in q:
    total+=cur[u]
    for v in g[u]:
     if v not in seen:seen.add(v);q.append(v)
   best=max(best,total)
  want.append(best)
 inp=f'{n} {m} {len(queries)}\n'+' '.join(map(str,a))+'\n'+'\n'.join(f'{u+1} {v+1}' for u,v in edges)+'\n'+'\n'.join(queries)+'\n';assert list(map(int,run('ABROADS',inp).split()))==want;checks+=1

for n in range(1,4):
 for m in range(1,4):
  total=0
  def paths(i,j,seq):
   seq=seq+[i*m+j]
   if i==n-1 and j==m-1:return [seq]
   return (paths(i+1,j,seq) if i+1<n else [])+(paths(i,j+1,seq) if j+1<m else [])
  ps=paths(0,0,[])
  for mask in range(1<<(n*m)):total+=sum(sum((mask>>x&1)*2-1 for x in p)==0 for p in ps)
  eq('REDGREEN',[n,m],total)
# Reject malformed or nonoptimal constructions, rather than accepting arbitrary output.
for code,inp,out in [
 ('DIANE','1\n1\n','1\n1\n'),
 ('INTREP','1\n1\n','2 1\n'),
 ('ALTDIA','1\n2 2\n','BBWW\n1 2\n2 3\n3 4\n'),
 ('CONSTANARRAY','1\n2 2\n1 1\n','2 1\n'),
 ('TDISTS','1\n2 2\n','NO\n'),
 ('GSEQ','1\n2\n1 1\n','1\n1\n'),
 ('SPTREE','1\n2 1 1\n2\n1 2\n','0 1\n1 1\n'),
 ('SMALLESTDIFF','1\n2 2\n1 2 3 4\n','1 2\n3 4\n'),
]:
 ok,_=CHECKERS[code](inp,out);assert not ok,(code,'accepted invalid construction');checks+=1
for x in range(1,21):
 for y in range(1,21):
  inp=f'1\n{x} {y}\n';out=load('TDISTS').solve(iter([x,y]));ok,why=CHECKERS['TDISTS'](inp,out);assert ok,(inp,out,why);checks+=1
for a in range(1,9):
 for b in range(1,9):
  x,y=a*a+b*b,2*a*b;inp=f'1\n{x} {y}\n';out=load('TDISTS').solve(iter([x,y]));ok,why=CHECKERS['TDISTS'](inp,out);assert ok,(inp,out,why);checks+=1
print(f'{checks} deterministic checks passed')
