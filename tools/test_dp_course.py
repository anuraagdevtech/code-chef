#!/usr/bin/env python3
"""Deterministic small exhaustive/differential checks, independent of samples."""
from pathlib import Path
import itertools as I, random, subprocess, sys, math, collections
ROOT=Path(__file__).resolve().parents[1];rng=random.Random(731925);checks=0

def run(code,text):
 p=subprocess.run([sys.executable,'-I',str(ROOT/'solutions'/f'{code}.py')],input=text,text=True,capture_output=True,timeout=30)
 assert p.returncode==0,(code,p.stderr);return p.stdout.split()
def batch(code,cases,want):
 global checks
 got=run(code,str(len(cases))+'\n'+'\n'.join(cases)+'\n');assert got==list(map(str,want)),(code,got,want);checks+=len(cases)
def subsets(a):
 for mask in range(1<<len(a)):yield [x for i,x in enumerate(a) if mask>>i&1]

cases=[];want=[]
for _ in range(120):
 n=rng.randrange(1,9);a=list(range(1,n+1));rng.shuffle(a);cases.append(f'{n}\n'+ ' '.join(map(str,a)))
 def inv(a):return sum(x>y for i,x in enumerate(a) for y in a[i+1:])
 ok=any(inv([a[i] for i in range(n) if mask>>i&1])==inv([a[i] for i in range(n) if not mask>>i&1]) for mask in range(1<<n));want.append('YES' if ok else 'NO')
batch('PERMSPL',cases,want)

cases=[];want=[]
for _ in range(100):
 n=rng.randrange(1,8);a=[rng.randrange(1,11) for _ in range(n)];x=rng.randrange(1,19);y=x+rng.randrange(8);cases.append(f'{n} {x} {y}\n'+' '.join(map(str,a)));best=99
 for mask in range(1<<n):
  if x<=sum(a[i] for i in range(n) if mask>>i&1)<=y:
   k=mask.bit_count();best=min(best,sum(bool(mask>>i&1) for i in range(k,n)))
 want.append(best if best<99 else -1)
batch('BLKJK',cases,want)

cases=[];want=[]
for _ in range(80):
 n=rng.randrange(1,9);k=rng.randrange(1,n+1);a=[rng.randrange(1,20) for _ in range(n)];cases.append(f'{n} {k}\n'+' '.join(map(str,a)));want.append('%.3f'%min(abs(sum(b)/k-sorted(b)[(k-1)//2]) for b in I.combinations(a,k)))
batch('MEANMEDI',cases,want)

cases=[];want=[]
for n in range(1,9):
 for mask in range(1,1<<n):
  a=[1+bool(mask>>i&1) for i in range(n)];cases.append(f'{n}\n'+' '.join(map(str,a)));full=(1<<n)-1;queue=collections.deque([(mask,0)]);seen={mask}
  while queue:
   state,d=queue.popleft()
   if state==full:want.append(d);break
   for l in range(n):
    for r in range(l,n):
     interval=((1<<(r-l+1))-1)<<l
     if (state&interval).bit_count()*2>=r-l+1:
      ns=state|interval
      if ns not in seen:seen.add(ns);queue.append((ns,d+1))
batch('MEDIAN',cases,want)

cases=[];want=[]
for _ in range(80):
 n=rng.randrange(2,6);m=rng.randrange(2,6);a=[''.join(rng.choice('01') for _ in range(m)) for _ in range(n)];cases.append(f'{n} {m}\n'+'\n'.join(a));ans=n*m
 # Avoid evaluating invalid paths via conditional expressions.
 def brute(x,y,seen):
  seen=seen|{(u,v) for u,v in ((x,y),(x+1,y),(x-1,y),(x,y-1),(x,y+1)) if 0<=u<n and 0<=v<m}
  if (x,y)==(n-1,m-1):return sum(a[u][v]=='1' for u,v in seen)
  result=[]
  if x+1<n:result.append(brute(x+1,y,seen))
  if y+1<m:result.append(brute(x,y+1,seen))
  return min(result)
 want.append(brute(0,0,set()))
batch('LEMOUSE',cases,want)

for code in ['HMAPPY1','CHEFSUBA']:
 for _ in range(30):
  n=rng.randrange(1,15);k=rng.randrange(1,n+1);a=[rng.randrange(2) for _ in range(n)];commands=''.join(rng.choice('!?') for _ in range(70));text=f'{n} {70 if code=="HMAPPY1" else k} {k if code=="HMAPPY1" else 70}\n'+' '.join(map(str,a))+'\n'+commands;want=[]
  for ch in commands:
   if ch=='!':a=a[-1:]+a[:-1]
   elif code=='CHEFSUBA':want.append(max(sum(a[i:i+k]) for i in range(n-k+1)))
   else:
    longest=cur=0
    for x in a:cur=(cur+1)*x;longest=max(longest,cur)
    want.append(min(k,longest))
  assert run(code,text)==list(map(str,want)),(code,text,want,run(code,text));checks+=len(want)

for _ in range(15):
 n=15;low,high=3,7;a=[0]*n;commands=[];want=[]
 for _ in range(100):
  if rng.randrange(2):x=rng.randrange(n);v=rng.randrange(12);a[x]=v;commands.append(f'1 {x+1} {v}')
  else:
   l=rng.randrange(n);r=rng.randrange(l,n);commands.append(f'2 {l+1} {r+1}');want.append(sum(low<=max(a[i:j+1])<=high for i in range(l,r+1) for j in range(i,r+1)))
 assert run('CSUBQ',f'{n} {len(commands)} {low} {high}\n'+'\n'.join(commands))==list(map(str,want));checks+=len(want)

cases=[];want=[]
for _ in range(60):
 n=rng.randrange(1,9);l=rng.randrange(1,8);a=rng.randrange(l+1);b=rng.randrange(l+1);s=''.join(rng.choice('+-') for _ in range(n));cases.append(f'{n} {l} {a} {b}\n{s}');ok=set()
 for seq in subsets(s):
  pos=a
  for ch in seq:
   pos+=1 if ch=='+' else -1
   if not 0<=pos<=l:break
  else:
   if pos==b:ok.add(''.join(seq))
 want.append(len(ok))
batch('F2',cases,want)

cases=[];want=[]
for _ in range(60):
 n=rng.randrange(1,9);a=[rng.randrange(1,1000) for _ in range(n)];cases.append(f'{n}\n'+' '.join(map(str,a)));answer=0
 for seq in subsets(a):
  if not seq:continue
  digits=[str(x).zfill(3) for x in seq];z=''.join(max(ds) for ds in zip(*digits)).lstrip('0')
  answer+=bool(z) and all(d in '47' for d in z)
 want.append(answer)
batch('LUCKY3',cases,want)

cases=[];want=[]
for _ in range(100):
 a=[rng.randrange(50) for _ in range(rng.randrange(1,8))];cases.append(str(len(a))+' '+' '.join(map(str,a)));poly=0
 for x in a:
  for j in range(x+1):
   if j&x==j:poly^=1<<j
 want.append(poly.bit_count())
batch('ODDBIN',cases,want)

cases=[];want=[]
for n in range(1,18):
 def walk(pos,back):
  if pos==n:return int(back)
  answer=sum(walk(pos+s,back) for s in (1,2) if pos+s<=n)
  if not back and pos!=0:answer+=sum(walk(pos-s,True) for s in (1,2))
  return answer
 cases.append(str(n));want.append(walk(0,False))
batch('CHEFWD',cases,want)

# Independently validate reconstructed outputs and objective against brute orders.
from checkers_dp_course import coinpart,peppera,n3
for code,check in [('COINPART',coinpart),('PEPPERA',peppera),('N3',n3)]:
 cases=[]
 for _ in range(30):
  if code=='COINPART':
   a=[rng.randrange(1,15) for _ in range(rng.randrange(1,8))];cases.append(str(len(a))+'\n'+' '.join(map(str,a)))
  elif code=='PEPPERA':
   n=rng.choice((2,4,6));cases.append(str(n)+'\n'+'\n'.join(''.join(rng.choice('01') for _ in range(n)) for _ in range(n)))
  else:
   n=rng.randrange(1,5);length=rng.randrange(1,5);k=rng.randrange(1,7);cases.append(f'{n} {length} {k}\n'+'\n'.join(''.join(rng.choice('ab') for _ in range(length)) for _ in range(n)))
 text=str(len(cases))+'\n'+'\n'.join(cases);output=' '.join(run(code,text));assert check(text,output)[0],(code,check(text,output));checks+=len(cases)



cases=[];want=[]
for length in range(9):
 groups=collections.Counter()
 def hashed(s):return s.count('A')+(max(hashed(s[:len(s)//2]),hashed(s[len(s)//2:])) if len(s)>1 else 0)
 for chars in I.product('AE',repeat=length):s=''.join(chars);groups[(s.count('A'),hashed(s))]+=1
 for a in range(length+1):
  for v in range(length*5+1):cases.append(f'{a} {length-a} {v}');want.append(groups[a,v])
batch('AEHASH',cases,want)

cases=[];want=[]
for _ in range(90):
 n=rng.randrange(1,8);budget=rng.randrange(1,10);a=[rng.randrange(-9,10) for _ in range(n)];judges=[]
 for _ in range(rng.randrange(1,7)):
  l=rng.randrange(n);r=rng.randrange(l,n);judges.append((l,r,rng.randrange(1,8)))
 costs=[min([c for l,r,c in judges if l<=i<=r] or [999]) for i in range(n)];answer=sum(a)
 for mask in range(1<<n):
  if sum(costs[i] for i in range(n) if mask>>i&1)<=budget:answer=max(answer,sum(a[i] for i in range(n) if not mask>>i&1))
 cases.append(f'{n} {budget} {len(judges)}\n'+' '.join(map(str,a))+'\n'+'\n'.join(f'{l+1} {r+1} {c}' for l,r,c in judges));want.append(answer)
batch('MCHEF',cases,want)

cases=[];want=[]
for _ in range(80):
 a=''.join(rng.choice('abc') for _ in range(rng.randrange(1,6)));b=''.join(rng.choice('abc') for _ in range(rng.randrange(1,6)));cases.append(f'{len(a)} {len(b)}\n{a}\n{b}')
 def merge(a,b,s):
  if not a or not b:
   seq=s+a+b;return 1+sum(seq[i]!=seq[i-1] for i in range(1,len(seq)))
  return min(merge(a[1:],b,s+a[0]),merge(a,b[1:],s+b[0]))
 want.append(merge(a,b,''))
batch('STRMRG',cases,want)

cases=[];want=[]
for _ in range(60):
 s=''.join(rng.choice('ABC') for _ in range(rng.randrange(1,10)));pieces=[]
 for mask in range(1<<(len(s)-1)):
  ends=[0]+[i+1 for i in range(len(s)-1) if mask>>i&1]+[len(s)];seq=[s[l:r] for l,r in zip(ends,ends[1:])]
  if all(t==t[::-1] for t in seq):pieces.append(len(seq))
 cases.append(f'{len(s)}\n{s}');want.append(min(pieces))
 assert run('COUNTPAL',s)==[str(len(pieces))];checks+=1
batch('CHGLSTGT',cases,want)

for _ in range(35):
 n,m=rng.randrange(1,6),rng.randrange(1,6);a=[''.join(rng.choice('01') for _ in range(m)) for _ in range(n)];answer=0
 for i in range(n):
  for j in range(m):
   for h in range(1,min(n-i,m-j)+1):answer+=all(a[i+x][j+y]=='1' for x in range(h) for y in range(x,h))
 assert run('MATRIX2',f'{n} {m}\n'+'\n'.join(a))==[str(answer)];checks+=1

for _ in range(15):
 n=rng.randrange(1,8);a=[rng.randrange(1,9) for _ in range(n)];queries=list(range(1,12));text=f'{n}\n'+' '.join(map(str,a))+f'\n{len(queries)}\n'+'\n'.join(map(str,queries));p=1000000007;want=[]
 for size in queries:
  counts=[(x+size-1)//size for x in a];total=sum(counts);ways=math.factorial(total)
  for x in counts:ways//=math.factorial(x)
  pal=0
  if sum(x%2 for x in counts)<=1:
   pal=math.factorial(total//2)
   for x in counts:pal//=math.factorial(x//2)
  want.append((ways+pal)//2%p)
 assert run('OLYMPIC',text)==list(map(str,want));checks+=len(want)

for _ in range(30):
 children=[[]];leaves=[0]
 for _ in range(rng.randrange(1,5)):
  new=[]
  for leaf in leaves:
   for _ in range(rng.randrange(1,4)):
    u=len(children);children.append([]);children[leaf].append(u);new.append(u)
  leaves=new
 n=len(children);edges=[(v,u) for v,row in enumerate(children) for u in row];qs=[];want=[];previous=0
 for _ in range(20):
  v=rng.randrange(n);y=rng.choice([1,2,3,1000000006]);depths=[];stack=[(v,0)]
  while stack:
   u,d=stack.pop();depths.append(d);stack.extend((ch,d+1) for ch in children[u])
  ans=sum(d*pow(y,i,1000000007) for i,d in enumerate(sorted(depths)))%1000000007;qs.append(f'{(v+1)^previous} {y^previous}');want.append(ans);previous=ans
 text='1\n'+f'{n} {len(qs)}\n'+'\n'.join(f'{u+1} {v+1}' for u,v in edges)+'\n'+'\n'.join(qs)
 assert run('PTREE',text)==list(map(str,want)),(text,run('PTREE',text),want);checks+=len(want)

for _ in range(25):
 n=rng.randrange(1,8);a=[rng.randrange(1,13) for _ in range(n)];text=f'1\n{n}\n'+' '.join(map(str,a));order=[int(x)-1 for x in run('COINPART',text)]
 def payout(order):
  s=t=0
  for i in order:
   if s<=t:s+=a[i]
   else:t+=a[i]
  return s
 assert payout(order)==max(map(payout,I.permutations(range(n))));checks+=1

cases=[];want=[]
for _ in range(50):
 a=''.join(rng.choice('12') for _ in range(rng.randrange(1,8)));b=''.join(rng.choice('12') for _ in a);cases.append(a+'\n'+b)
 def good(s):
  n=len(s)
  def dfs(i,mask):
   if mask==(1<<n)-1:return i==n-1
   return any(0<=j<n and not mask>>j&1 and dfs(j,mask|1<<j) for j in (i-int(s[i]),i+int(s[i])))
  return dfs(0,1)
 answer=0
 for mask in range(1<<len(a)):
  x=''.join(b[i] if mask>>i&1 else a[i] for i in range(len(a)));y=''.join(a[i] if mask>>i&1 else b[i] for i in range(len(a)));answer+=good(x) and good(y)
 want.append(answer)
batch('CHEFTWOS',cases,want)


cases=[];want=[]
for _ in range(70):
 a=[rng.randrange(1,20) for _ in range(rng.randrange(1,10))];target=rng.randrange(1,60);cases.append(f'{len(a)} {target}\n'+' '.join(map(str,a)));want.append('Yes' if any(sum(s)==target for s in subsets(a)) else 'No')
batch('MARCHA1',cases,want)

cases=[];want=[]
for n in range(2,7):
 for k in range(1,4):
  cases.append(f'{n} {k}');want.append(sum(all(s[i]!=s[i-1] for i in range(1,len(s))) and s[-1]==0 for mid in I.product(range(k+1),repeat=n) for s in [(0,)+mid]))
batch('FCBARCA',cases,want)

cases=[];want=[]
for n in range(1,35):
 def diamonds(x):return abs(sum(int(d)*(1 if int(d)%2==0 else -1) for d in str(x)))
 cases.append(str(n));want.append(sum(diamonds(i+j) for i in range(1,n+1) for j in range(1,n+1)))
batch('VK18',cases,want)

cases=[];want=[]
for _ in range(60):
 n=rng.randrange(2,9);a=[rng.randrange(-8,9) for _ in range(n)];cases.append(f'{n}\n'+' '.join(map(str,a)));want.append(max(abs(sum(a[i:j])-sum(a[k:l])) for i in range(n) for j in range(i+1,n+1) for k in range(j,n) for l in range(k+1,n+1)))
batch('DELISH',cases,want)

cases=[];want=[]
for _ in range(40):
 states=rng.choice((1,3,5));width=rng.choice((1,3,5));n=states*width;a=[rng.randrange(2) for _ in range(n)];cases.append(f'{states} {width}\n'+' '.join(map(str,a)));want.append(int(any(sum(sum(a[(start+j*width+k)%n] for k in range(width))>width//2 for j in range(states))>states//2 for start in range(n))))
batch('GERMANDE',cases,want)

cases=[];want=[]
for n in range(1,11):
 for k in range(1,n+1):
  answer=0
  for bits in I.product('01',repeat=n):answer+=all(len(s)%k==0 for s in ''.join(bits).split('0'))
  cases.append(f'{n} {k}');want.append(answer)
batch('SEARRAYS',cases,want)

cases=[];want=[]
for _ in range(80):
 a=[rng.randrange(10) for _ in range(rng.randrange(2,9))];valid=[]
 for i in range(len(a)):
  b=a[:i]+a[i+1:]
  if len(set(b[j]-b[j-1] for j in range(1,len(b))))<=1:valid.append(a[i])
 cases.append(f'{len(a)}\n'+' '.join(map(str,a)));want.append(min(valid,default=-1))
batch('TAASEQ',cases,want)

cases=[];want=[]
for _ in range(60):
 a=[rng.randrange(1,35) for _ in range(rng.randrange(1,10))];cases.append(f'{len(a)}\n'+' '.join(map(str,a)));want.append(max(len(s) for s in subsets(a) if all(math.gcd(x,y)>1 for x,y in zip(s,s[1:]))))
batch('KIRLAB',cases,want)

cases=[];want=[]
for b in range(1,7):
 counts=collections.Counter((sum(x for x in seq if x>0),seq.count(-1)) for seq in I.product((0,4,6,-1),repeat=b))
 for _ in range(8):
  r=rng.randrange(6*b+4);l=rng.randrange(4);cases.append(f'{r} {b} {l}');want.append(sum(counts[r,w] for w in range(l+1)))
batch('WORLDCUP',cases,want)

cases=[];want=[]
for _ in range(45):
 n=rng.randrange(1,10);h=rng.randrange(1,n+1);gaps=[]
 for _ in range(n):l=rng.randrange(n);r=rng.randrange(l,n);gaps.append((l,r))
 cases.append(f'{n} {h}\n'+'\n'.join(f'{l} {r}' for l,r in gaps));want.append(min(sum(not l<=y<=r for y in range(start,start+h) for l,r in gaps) for start in range(n-h+1)))
batch('WOUT',cases,want)

for _ in range(40):
 a=[rng.randrange(1,8) for _ in range(rng.randrange(1,20))];answer=1
 for i,x in enumerate(a):answer*=next((j-i+1 for j in range(i+1,len(a)) if a[j]<x),1)
 assert run('CHFQUEUE',f'{len(a)} 7\n'+' '.join(map(str,a)))==[str(answer%1000000007)];checks+=1

cases=[];want=[]
for n in range(1,7):
 for m in range(1,5):
  for k in range(1,5):cases.append(f'{n} {m} {k}');want.append(sum(len(set(s))<=k for s in I.product(range(m),repeat=n)))
batch('NEWREST',cases,want)

for _ in range(25):
 n=rng.randrange(1,8);a=[rng.randrange(1,20) for _ in range(n)];queries=[];want=[]
 for _ in range(7):
  k=rng.randrange(1,n+2);t=[rng.randrange(3) for _ in range(n)];values=[x*y for x,y in zip(a,t)];answer=0
  for cuts in I.combinations(range(1,n),k-1):
   points=(0,)+cuts+(n,);sweet=[sum(values[l:r]) for l,r in zip(points,points[1:])];v=sweet[0]
   for x in sweet[1:]:v&=x
   answer=max(answer,v)
  queries.append(str(k)+'\n'+' '.join(map(str,t)));want.append(answer)
 text=f'{n}\n'+' '.join(map(str,a))+f'\n{len(queries)}\n'+'\n'.join(queries);assert run('CHEFOFR',text)==list(map(str,want));checks+=len(want)

cases=[];want=[]
for n in range(2,9):
 for m in range(2,7):
  a=rng.randrange(1,n);b=rng.randrange(1,m);dp=[[0]*(m+1) for _ in range(n+1)];dp[0][0]=1
  for x in range(n+1):
   for y in range(m+1):
    if x>n-a and y<b:continue
    if x:dp[x][y]+=dp[x-1][y]
    if y:dp[x][y]+=dp[x][y-1]
  cases.append(f'{n} {m} {a} {b}');want.append(dp[n][m])
batch('CNTWAYS',cases,want)

for _ in range(25):
 n=rng.randrange(2,10);m=rng.randrange(3,15);a=sorted(rng.sample(range(30),n));paths=[]
 for middle in subsets(list(range(1,n-1))):
  path=[0]+middle+[n-1]
  if all(a[j]-a[i]<=m for i,j in zip(path,path[1:])):paths.append(len(path)-2)
 if not paths:continue
 best=min(paths);assert run('TRIP',f'{n} {m}\n'+'\n'.join(map(str,a)))==[str(best),str(paths.count(best))];checks+=1

for _ in range(15):
 n,m=rng.randrange(1,6),rng.randrange(1,6);a=[[rng.randrange(1,12) for _ in range(m)] for _ in range(n)];queries=[(h,w) for h in range(1,n+1) for w in range(1,m+1)];want=[]
 for h,w in queries:
  costs=[]
  for i in range(n-h+1):
   for j in range(m-w+1):
    values=[a[x][y] for x in range(i,i+h) for y in range(j,j+w)];costs.append(max(values)*h*w-sum(values))
  want.append(min(costs))
 text=f'{n} {m}\n'+'\n'.join(' '.join(map(str,row)) for row in a)+f'\n{len(queries)}\n'+'\n'.join(f'{h} {w}' for h,w in queries);assert run('CHSQARR',text)==list(map(str,want));checks+=len(want)

for _ in range(10):
 s=''.join(rng.choice('chef') for _ in range(30));queries=[];want=[]
 for _ in range(70):
  a,b=rng.sample('chef',2);l=rng.randrange(len(s));r=rng.randrange(l,len(s));queries.append(f'{a} {b} {l+1} {r+1}');want.append(sum(s[i]==a and s[j]==b for i in range(l,r+1) for j in range(i+1,r+1)))
 assert run('STRQ',s+'\n'+str(len(queries))+'\n'+'\n'.join(queries))==list(map(str,want));checks+=len(want)


print(f"{checks} deterministic brute-force comparisons passed")
