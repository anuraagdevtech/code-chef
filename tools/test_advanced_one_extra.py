"""Additional independent models used by test_advanced_one.py."""
import itertools as I, math
from collections import deque
from functools import lru_cache

def run(t):
 rng=t.rng;exact=t.exact;execute=t.execute;semantic=t.semantic
 def array(a):return ' '.join(map(str,a))
 # Arbitrary dynamic graph freezing is modeled one second at a time.
 for _ in range(35):
  n=rng.randrange(2,10);edges=[(i,j) for i in range(n) for j in range(i) if rng.random()<.3];g=[[] for _ in range(n)]
  for u,v in edges:g[u].append(v);g[v].append(u)
  frozen=set();ops=[];want=[]
  for _ in range(60):
   typ=rng.randrange(1,4);x=rng.randrange(1,n+1) if typ!=2 else rng.randrange(1,5);ops.append(f'{typ} {x}')
   if typ==1:frozen.add(x-1)
   elif typ==2:
    for _ in range(x):frozen|={v for u in frozen for v in g[u]}
   else:want.append('YES' if x-1 in frozen else 'NO')
  inp=f'{n} {len(edges)} {len(ops)}\n'+'\n'.join(f'{u+1} {v+1}' for u,v in edges)+'\n'+'\n'.join(ops)
  assert execute('ELWINTER',inp).split()==want;t.checks+=len(ops)
 for n in (1,2,12,36,60,97,720,10000,999983):
  ds=[d for d in range(1,n+1) if n%d==0];qs=[];want=[]
  for typ in (1,2,3):
   for k in range(1,70):qs.append(f'{typ} {k}');want.append(sum((k%d==0 if typ==1 else d%k==0 if typ==2 else d%k!=0) for d in ds))
  assert list(map(int,execute('QNUMBER',f'{n} {len(qs)}\n'+'\n'.join(qs)).split()))==want;t.checks+=len(qs)
 # Independent quotient-basis invariant for row/column window additions.
 cases=[];want=[]
 for _ in range(150):
  r=rng.randrange(2,7);c=rng.randrange(2,7);x=rng.randrange(2,min(r,c)+1);a=[[rng.randrange(-3,4) for _ in range(c)] for _ in range(r)];b=[[rng.randrange(-3,4) for _ in range(c)] for _ in range(r)]
  invariant=[[0]*(x-1) for _ in range(x-1)]
  for i in range(r):
   for j in range(c):
    for u in range(x-1):
     ri=-1 if i%x==x-1 else int(i%x==u)
     for v in range(x-1):invariant[u][v]+=(a[i][j]-b[i][j])*ri*(-1 if j%x==x-1 else int(j%x==v))
  cases.append(f'{r} {c} {x}\n'+'\n'.join(array(row) for row in a+b));want.append('YES' if not any(map(any,invariant)) else 'NO')
 exact('CONSADD',cases,want)
 cases=[];want=[]
 for n in range(1,8):
  for k in range(1,n+1):
   for _ in range(12):
    a=[rng.randrange(5) for _ in range(n)];possible=False
    for turns in range(80):
     low=high=0;ok=True
     for i in range(n//2):
      j=n-1-i;lo=max(a[i],a[j]);hi=min(a[i],a[j])+turns
      if lo>hi:ok=False;break
      low+=2*lo-a[i]-a[j];high+=2*hi-a[i]-a[j]
     if n%2:high+=turns
     if ok and low<=k*turns<=high and (n%2 or (k*turns-low)%2==0):possible=True;break
    cases.append(f'{n} {k}\n'+array(a));want.append('YES' if possible else 'NO')
 exact('KPAL',cases,want)
 # Direct cake simulation and direct arithmetic-progression updates.
 cases=[];want=[]
 for _ in range(100):
  n=rng.randrange(2,15);k=rng.randrange(1,n+1);ranges=[]
  for _ in range(n):l=rng.randrange(1,25);r=rng.randrange(l,26);ranges.append((l,r))
  best=0
  for skip in range(n):
   heights=[0]*26
   for j,(l,r) in enumerate(ranges):
    if j!=skip:
     for i in range(l,r+1):heights[i]+=1
   best=max(best,sum(x==k for x in heights))
  cases.append(f'{n} {k}\n'+'\n'.join(f'{l} {r}' for l,r in ranges));want.append(best)
 exact('MAXREMOV',cases,want)
 cases=[];want=[]
 for _ in range(100):
  n=rng.randrange(1,25);q=rng.randrange(1,25);a=[0]*n;qs=[]
  for _ in range(q):
   l=rng.randrange(n);r=rng.randrange(l,n);qs.append((l+1,r+1))
   for i in range(l,r+1):a[i]+=i-l+1
  cases.append(f'{n} {q}\n'+'\n'.join(f'{l} {r}' for l,r in qs));want.extend(a)
 exact('AGCY',cases,want)
 cases=[];want=[]
 for _ in range(150):
  n=rng.randrange(3,9);a=[rng.randrange(1,20) for _ in range(n)]
  ans=min(sum((b[i%3]-a[i])%3 for i in range(n)) for b in I.product(range(3),repeat=3) if sum(b)%3==0)
  cases.append(f'{n}\n'+array(a));want.append(ans)
 exact('SEGTHREE',cases,want)
 cases=[];want=[]
 for a in range(2,70):
  for b in range(2,70):
   va={a**i for i in range(1,20)};possible=any(b**i in va for i in range(1,20));cases.append(f'{a} {b}');want.append('YES' if possible else 'NO')
 exact('EQUIVALENT',cases,want)
 # Evaluate deleted-tree components directly for both tree problems.
 casesf=[];wantf=[];casesd=[];wantd=[]
 for _ in range(100):
  n=rng.randrange(2,14);edges=[(i,rng.randrange(i)) for i in range(1,n)];g=[[] for _ in range(n)];a=[rng.randrange(1,60) for _ in range(n)];parent=[0]*n
  for u,v in edges:g[u].append(v);g[v].append(u);parent[u]=v
  def score(removed):
   seen=set(removed);total=0
   for u in range(n):
    if u in seen:continue
    seen.add(u);stack=[u];gd=0
    while stack:
     v=stack.pop();gd=math.gcd(gd,a[v])
     for w in g[v]:
      if w not in seen:seen.add(w);stack.append(w)
    total+=gd
   return total
  fd=[];dd=[]
  for v in range(n):
   removed={v};u=v
   while u: u=parent[u];removed.add(u)
   fd.append(score(removed));dd.append(score({v}))
  estr='\n'.join(f'{u+1} {v+1}' for u,v in edges);casesf.append(f'{n}\n'+array(a)+'\n'+estr);wantf.append(max(fd));casesd.append(f'{n}\n'+estr+'\n'+array(a));wantd.append(max(dd))
 exact('FPE',casesf,wantf);exact('DLTNODE',casesd,wantd)
 cases=[];want=[]
 for n in range(2,8):
  for a in I.permutations(range(n)):
   if a[0]==0 or a[-1]==n-1:continue
   dp=[[False]*n for _ in range(n)];dp[0][0]=True
   for i in range(n):
    for j in range(n):
     if a[i]==j:dp[i][j]=False
     elif i or j:dp[i][j]=(i>0 and dp[i-1][j]) or (j>0 and dp[i][j-1])
   cases.append(f'{n}\n'+'\n'.join(f'{i+1} {v+1}' for i,v in enumerate(a)));want.append('YES' if dp[-1][-1] else 'NO')
 exact('RECHEND',cases,want)
 cases=[];want=[]
 for _ in range(100):
  n=rng.randrange(1,7);m=rng.randrange(1,7);k=rng.randrange(1,60);a=[[rng.randrange(5) for _ in range(m)] for _ in range(n)];best=-1
  for d in range(max(n,m)):
   if any(a[i][j] and sum(a[u][v] for u in range(n) for v in range(m) if max(abs(u-i),abs(v-j))<=d)>=k+1 for i in range(n) for j in range(m)):best=d;break
  cases.append(f'{n} {m} {k}\n'+'\n'.join(array(row) for row in a));want.append(best)
 exact('TRPTSTIC',cases,want)
 # Full operation search, including both subtraction orientations.
 @lru_cache(None)
 def majik(a,p,q):
  best=a[-1]-a[0]
  if len(a)<=2:return best
  for i in range(len(a)):
   for j in range(i+1,len(a)):
    rest=a[:i]+a[i+1:j]+a[j+1:]
    if p:best=max(best,majik(tuple(sorted(rest+(a[i]+a[j],))),p-1,q))
    if q:
     for z in (a[i]-a[j],a[j]-a[i]):best=max(best,majik(tuple(sorted(rest+(z,))),p,q-1))
  return best
 cases=[];want=[]
 for _ in range(50):
  n=rng.randrange(1,7);p=rng.randrange(n);q=rng.randrange(n);a=tuple(sorted(rng.randrange(-4,5) for _ in range(n)));cases.append(f'{n}\n{p} {q}\n'+array(a));want.append(majik(a,p,q))
 exact('MAJIK',cases,want)
 # Floyd-Warshall on the full graph of all purchasable edges.
 cases=[];want=[]
 for _ in range(100):
  n=rng.randrange(2,10);edges=[(i,j) for i in range(n) for j in range(i) if rng.random()<.15];d=[[(i-j)**2 for j in range(n)] for i in range(n)]
  for u,v in edges:d[u][v]=d[v][u]=0
  for k in range(n):
   for i in range(n):
    for j in range(n):d[i][j]=min(d[i][j],d[i][k]+d[k][j])
  cases.append(f'{n} {len(edges)}\n'+'\n'.join(f'{u+1} {v+1}' for u,v in edges));want.append(d[0][-1])
 exact('TRAVELLING',cases,want)
 # Lexicographically largest prefix-gcd arrays by scanning all possible next values.
 cases=[];want=[]
 for _ in range(120):
  n=rng.randrange(1,10);m=rng.randrange(1,50);b=[rng.randrange(1,m+1) for _ in range(n)];a=[];gd=0
  for x in b:gd=math.gcd(gd,x);a.append(gd)
  ans=[a[0]]
  for i in range(1,n):ans.append(max(x for x in range(1,m+1) if math.gcd(a[i-1],x)==a[i]))
  cases.append(f'{n} {m}\n'+array(a));want.extend(ans)
 exact('LEXILARGEST',cases,want)
 # Shop removal search tracks per-ingredient used operation types.
 cases=[];want=[]
 for _ in range(60):
  n=rng.randrange(1,7);l=[rng.randrange(1,12) for _ in range(n)];r=[rng.randrange(1,12) for _ in range(n)]
  @lru_cache(None)
  def shop(a,ls,rs):
   if len(a)==1:return 0
   best=10**9
   for i,x in enumerate(a):
    if i and not ls>>x&1:best=min(best,l[x]+shop(a[:i-1]+a[i:],ls|1<<x,rs))
    if i+1<len(a) and not rs>>x&1:best=min(best,r[x]+shop(a[:i+1]+a[i+2:],ls,rs|1<<x))
   return best
  cases.append(f'{n}\n'+array(l)+'\n'+array(r));want.append(shop(tuple(range(n)),0,0))
 exact('CHEFSHOPPING',cases,want)
 # Alternating difference queries verified by solving adjacent equations mod26.
 cases=[];want=[]
 for _ in range(50):
  n=rng.randrange(2,20);a=[rng.randrange(26) for _ in range(n)];b=[rng.randrange(26) for _ in range(n)];qs=[(l,r) for l in range(n) for r in range(l,n)]
  for l,r in qs:
   carry=0
   for i in range(l,r+1):carry=(b[i]-a[i]-carry)%26
   want.append('YES' if carry==0 else 'NO')
  cases.append(f'{n} {len(qs)}\n'+''.join(chr(97+x) for x in a)+'\n'+''.join(chr(97+x) for x in b)+'\n'+'\n'.join(f'{l+1} {r+1}' for l,r in qs))
 exact('CCD',cases,want)
 # Enumerate all random game outcomes over a small prime field.
 mod=998244353
 for p in (2,3,11):
  want=[]
  for n in range(1,9):
   ans=0
   for mask in range(1<<n):score=sum(pow(p,-i,mod) for i in range(n) if mask>>i&1)%mod;ans=(ans+score*score)%mod
   want.append(ans*pow(1<<n,-1,mod)%mod)
  assert list(map(int,execute('EXPVALUE',f'8 {p}').split()))==want;t.checks+=8
 # Rectangle flips, modeled literally.
 for _ in range(30):
  n=rng.randrange(1,10);m=rng.randrange(1,10);a=[[rng.randrange(2) for _ in range(m)] for _ in range(n)];orig=[''.join(map(str,row)) for row in a];qs=[]
  for _ in range(30):
   x=rng.randrange(n);u=rng.randrange(x,n);y=rng.randrange(m);v=rng.randrange(y,m);qs.append((x+1,y+1,u+1,v+1))
   for i in range(x,u+1):
    for j in range(y,v+1):a[i][j]^=1
  inp=f'{n} {m}\n'+'\n'.join(orig)+f'\n{len(qs)}\n'+'\n'.join(array(q) for q in qs);assert execute('CENS20A',inp).split()==[''.join(map(str,row)) for row in a];t.checks+=30
 # Exhaustive small mex constraints compared with existence among all actual arrays.
 for n in range(1,5):
  paths=[]
  for a in I.product(range(n+1),repeat=n):
   seen=set();mex=0;path=[]
   for x in a:
    seen.add(x)
    while mex in seen:mex+=1
    path.append(mex)
   paths.append(tuple(path))
  paths=set(paths);cases=[];possible=[]
  for b in I.product(range(-1,n+1),repeat=n):cases.append(f'{n}\n'+array(b));possible.append(any(all(x==-1 or x==y for x,y in zip(b,path)) for path in paths))
  out=execute('MEXYARR',str(len(cases))+'\n'+'\n'.join(cases)).splitlines()
  for case,answer,ok in zip(cases,out,possible):
   assert (answer!='-1')==ok,('MEXYARR',case,answer,ok)
   assert t.judges.mexyarr('1\n'+case,answer)[0]
  t.checks+=len(cases)
 cases=[];want=[]
 for n in range(1,9):
  for c in range(n):
   for _ in range(10):
    s=''.join(rng.choice('01') for _ in range(n));possible=False
    for rot in range(n):
     b=s[rot:]+s[:rot];pos=[i for i,x in enumerate(b) if x=='1']
     if all(pos[i]-pos[i-1]-1<=c for i in range(1,len(pos))):possible=True
    cases.append(f'{n} {c}\n{s}');want.append('YES' if possible else 'NO')
 exact('VSTRING',cases,want)
 cases=[];want=[]
 for s in range(1,60):
  for e in range(1,60):
   ways={s:1}
   for row in range(1,12):
    for x in range(row*(row-1)//2+1,row*(row+1)//2+1):
     if x in ways:ways[x+row]=ways.get(x+row,0)+ways[x];ways[x+row+1]=ways.get(x+row+1,0)+ways[x]
   cases.append(f'{s} {e}');want.append(ways.get(e,0))
 exact('PYRAMIDMOVES',cases,want)
 for _ in range(50):
  n=rng.randrange(1,25);k=rng.randrange(12);a=[rng.randrange(1,20) for _ in range(n)];ans=0
  for l in range(n):
   for r in range(l,n):ans+=not any(a[i]%a[j]==k for i in range(l,r+1) for j in range(i+1,r+1))
  assert int(execute('CHINSM',f'{n} {k}\n'+array(a)))==ans;t.checks+=1
 cases=[];want=[]
 @lru_cache(None)
 def merge(a):
  if len(a)==1:return 0
  ans=10**18
  for i in range(len(a)):
   b=a[i:]+a[:i];z=b[0]+b[1];ans=min(ans,z+merge((z,)+b[2:]))
  return ans
 for _ in range(100):
  n=rng.randrange(2,8);a=tuple(rng.randrange(1,10) for _ in range(n));cases.append(f'{n}\n'+array(a));want.append(merge(a))
 exact('CIRMERGE',cases,want)
 # Greedy actual decimal construction is independent of the closed-form digit sum.
 cases=[];want=[]
 for n in range(2,60):
  for k in range(1,n):
   s='1'
   for _ in range(1,n):
    for c in '0123456789':
     b=s+c
     if all(b[-length:]!=b[-length:][::-1] for length in range(k+1,len(b)+1)):s=b;break
   cases.append(f'{n} {k}');want.append(sum(map(int,s)))
 exact('NOPALINDROME',cases,want)
 # Every sum in many small matrices is constructed and semantically checked.
 for n in range(2,10):
  for m in range(2,7):
   qs=list(range(1,m*n*(n+1)//2+1));inp=f'{n} {m} {len(qs)}\n'+array(qs);out=execute('MOUNTAIN',inp);assert t.judges.mountain(inp,out)[0];t.checks+=len(qs)
