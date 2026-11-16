"""Semantic checkers for advanced-two constructive solutions."""
from collections import Counter, deque
from math import gcd, isqrt

def guarded(fn):
 def check(inp,out):
  try:
   fn(inp,out)
   return True,''
  except (ValueError,IndexError,StopIteration,AssertionError) as e:return False,str(e) or 'invalid construction'
 return check

def finish(it):
 assert next(it,None) is None,'extra output tokens'

@guarded
def diane(inp,out):
 a=iter(map(int,inp.split()));o=iter(map(int,out.split()))
 for _ in range(next(a)):
  d=next(a);n=next(o);assert 1<=n<=100000
  v=[next(o) for _ in range(n)];assert all(1<=x<=100000 for x in v)
  st=[];ending=mins=0;gs=[];gcdsum=0
  for x in v:
   count=1
   while st and st[-1][0]>=x:
    y,c=st.pop();ending-=y*c;count+=c
   st.append((x,count));ending+=x*count;mins+=ending
   new=[(x,1)]
   for y,c in gs:
    z=gcd(x,y)
    if new[-1][0]==z:new[-1]=(z,new[-1][1]+c)
    else:new.append((z,c))
   gs=new;gcdsum+=sum(y*c for y,c in gs)
  assert mins-gcdsum==d,'wrong min-minus-gcd sum'
 finish(o)

def prime(n):
 if n<2:return False
 for p in (2,3,5,7,11,13,17,19,23,29,31,37):
  if n%p==0:return n==p
 d=n-1;s=0
 while d%2==0:d//=2;s+=1
 for a in (2,325,9375,28178,450775,9780504,1795265022):
  if a%n==0:continue
  x=pow(a,d,n)
  if x in (1,n-1):continue
  for _ in range(s-1):
   x=x*x%n
   if x==n-1:break
  else:return False
 return True

def factors(n):
 if n==1:return set()
 if prime(n):return {n}
 if n%2==0:return {2}|factors(n//2)
 c=1
 while True:
  x=y=2;d=1
  while d==1:
   x=(x*x+c)%n;y=(y*y+c)%n;y=(y*y+c)%n;d=gcd(abs(x-y),n)
  if d!=n:return factors(d)|factors(n//d)
  c+=1

@guarded
def intrep(inp,out):
 a=iter(map(int,inp.split()));o=iter(map(int,out.split()))
 for _ in range(next(a)):
  n=next(a);x,y=next(o),next(o);assert 1<=x<=10**18 and 1<=y<=10**18 and x-y==n
  assert len(factors(x))==len(factors(y)),'prime-factor counts differ'
 finish(o)

@guarded
def altdia(inp,out):
 a=iter(map(int,inp.split()));o=iter(out.split())
 for _ in range(next(a)):
  b,w=next(a),next(a);n=b+w;s=next(o)
  if s=='-1':assert n>1 and (b==0 or w==0);continue
  assert Counter(s)==Counter({'B':b,'W':w}) and len(s)==n,'wrong colors'
  g=[[] for _ in range(n)]
  for _ in range(n-1):
   u,v=int(next(o))-1,int(next(o))-1;assert 0<=u<n and 0<=v<n and u!=v
   g[u].append(v);g[v].append(u)
  def bfs(root):
   d=[-1]*n;d[root]=0;q=deque([root])
   while q:
    u=q.popleft()
    for v in g[u]:
     if d[v]<0:d[v]=d[u]+1;q.append(v)
   return d
  d=bfs(0);assert min(d)>=0,'disconnected';u=max(range(n),key=d.__getitem__);diam=max(bfs(u));assert diam==min(2,n-1),'diameter not minimum'
  if n==2:assert s[0]!=s[1]
  if n>=3:assert any(sum(s[v]!=s[u] for v in g[u])>=2 for u in range(n)),'no alternating diameter'
 finish(o)

@guarded
def constanarray(inp,out):
 a=iter(map(int,inp.split()));o=iter(map(int,out.split()))
 for _ in range(next(a)):
  n,m=next(a),next(a);v=[next(a) for _ in range(n)];c=Counter();mx=0
  for x in v:
   y=next(o);assert 1<=y<=m;c[y]+=1;mx=max(mx,c[y]);assert c[x]==mx,'requested value is not a prefix mode'
 finish(o)

@guarded
def tdists(inp,out):
 a=iter(map(int,inp.split()));o=iter(out.split())
 for _ in range(next(a)):
  x,y=next(a),next(a);status=next(o).upper();n=isqrt(x+y);z=isqrt(max(0,x-y));possible=x>=y and n*n==x+y and z*z==x-y and (n-z)%2==0 and n>z
  assert status in ('YES','NO')
  if status=='NO':assert not possible;continue
  n=int(next(o));assert 1<=n<=31623;g=[[] for _ in range(n)]
  for _ in range(n-1):
   u,v=int(next(o))-1,int(next(o))-1;assert 0<=u<n and 0<=v<n and u!=v;g[u].append(v);g[v].append(u)
  col=[-1]*n;col[0]=0;q=deque([0])
  while q:
   u=q.popleft()
   for v in g[u]:
    if col[v]<0:col[v]=col[u]^1;q.append(v)
    else:assert col[v]!=col[u]
  assert min(col)>=0;p=col.count(0);r=n-p;assert p*p+r*r==x and 2*p*r==y
 finish(o)

@guarded
def gseq(inp,out):
 a=iter(map(int,inp.split()));o=iter(map(int,out.split()))
 for _ in range(next(a)):
  n=next(a);v=[next(a) for _ in range(n)];pref=[0]
  for x in v:pref.append(pref[-1]+2*x-1)
  k=next(o);seq=[next(o)-1 for _ in range(k)];assert 1<=k<=n+1 and all(0<=x<=n for x in seq)
  assert all(x<y and pref[y]-pref[x]==1 for x,y in zip(seq,seq[1:])),'not a good sequence'
  dp={};best=0
  for p in pref:dp[p]=max(dp.get(p,0),dp.get(p-1,0)+1);best=max(best,dp[p])
  assert k==best,'not longest'
 finish(o)

@guarded
def sptree(inp,out):
 a=iter(map(int,inp.split()));o=iter(map(int,out.split()))
 for _ in range(next(a)):
  n,k,root=next(a),next(a),next(a)-1;special={next(a)-1 for _ in range(k)};g=[[] for _ in range(n)]
  for _ in range(n-1):u,v=next(a)-1,next(a)-1;g[u].append(v);g[v].append(u)
  parent=[-1]*n;dep=[0]*n;parent[root]=root;order=[root]
  for u in order:
   for v in g[u]:
    if parent[v]<0:parent[v]=u;dep[v]=dep[u]+1;order.append(v)
  val=[next(o) for _ in range(n)];who=[next(o)-1 for _ in range(n)];best=[-10**9]*n
  for u in special:best[u]=dep[u]
  for u in reversed(order[1:]):best[parent[u]]=max(best[parent[u]],best[u]-1)
  for u in order[1:]:best[u]=max(best[u],best[parent[u]]-1)
  assert val==best,'incorrect optimal scores'
  # Binary lifting validates each claimed witness independently.
  up=[parent]
  for _ in range(n.bit_length()):up.append([up[-1][up[-1][i]] for i in range(n)])
  def lca(u,v):
   if dep[u]<dep[v]:u,v=v,u
   diff=dep[u]-dep[v]
   for j in range(diff.bit_length()):
    if diff>>j&1:u=up[j][u]
   if u==v:return u
   for row in reversed(up):
    if row[u]!=row[v]:u,v=row[u],row[v]
   return parent[u]
  for b,u in enumerate(who):assert u in special and dep[u]-(dep[b]+dep[u]-2*dep[lca(b,u)])==val[b],'invalid witness'
 finish(o)

@guarded
def smallestdiff(inp,out):
 a=iter(map(int,inp.split()));o=iter(map(int,out.split()))
 for _ in range(next(a)):
  n,m=next(a),next(a);v=sorted(next(a) for _ in range(n*m));g=[[next(o) for _ in range(m)] for _ in range(n)];assert sorted(x for row in g for x in row)==v,'not a permutation'
  i=j=0;path=[g[0][0]]
  while i<n-1 or j<m-1:
   if i==n-1:j+=1
   elif j==m-1:i+=1
   elif ((i+j)%2==0 and g[i+1][j]>g[i][j+1]) or ((i+j)%2 and g[i+1][j]<g[i][j+1]):i+=1
   else:j+=1
   path.append(g[i][j])
  length=n+m-1;t=min(n,m)-1;low=(t+1)//2;high=t//2
  optimum=min(v[s+length-1]-v[s] for s in range(low,n*m-length-high+1))
  assert max(path)-min(path)==optimum,'score not optimal'
 finish(o)

CHECKERS={'DIANE':diane,'INTREP':intrep,'ALTDIA':altdia,'CONSTANARRAY':constanarray,'TDISTS':tdists,'GSEQ':gseq,'SPTREE':sptree,'SMALLESTDIFF':smallestdiff}
