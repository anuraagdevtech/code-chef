"""Semantic and tolerance validators for the dynamic-programming/course batch."""
import math

def float_checker(tolerance):
    def check(inp, output):
        try:
            got=list(map(float,output.split()));want=list(map(float,check.expected))
            return (len(got)==len(want) and all(math.isfinite(a) and abs(a-b)<=tolerance*max(1,abs(b)) for a,b in zip(got,want)), 'floating point answer differs')
        except (ValueError,AttributeError):return False,'invalid floating point output'
    return check

def peppera(inp, output):
    data=iter(inp.split());out=iter(output.split())
    try:
        for _ in range(int(next(data))):
            n=int(next(data));rows=[next(data) for _ in range(n)];got=[next(out) for _ in range(n)];bits=1;total=0
            for s in rows:
                w=abs(s[:n//2].count('1')-s[n//2:].count('1'));total+=w;bits|=bits<<w
            target=total//2
            while not bits>>target&1:target-=1
            if any(t not in (s,s[::-1]) for s,t in zip(rows,got)):return False,'a row is not an allowed reversal'
            difference=abs(sum(t[:n//2].count('1')-t[n//2:].count('1') for t in got))
            if difference!=total-2*target:return False,'pepperoni imbalance is not minimal'
        if next(out,None) is not None:return False,'extra output'
        return True,''
    except (ValueError,StopIteration):return False,'malformed grid'

def coinpart(inp, output):
    data=iter(map(int,inp.split()));out=iter(map(int,output.split()))
    try:
        for _ in range(next(data)):
            n=next(data);a=[next(data) for _ in range(n)];order=[next(out)-1 for _ in range(n)]
            if sorted(order)!=list(range(n)):return False,'indices are not a permutation'
            s=t=0
            for i in order:
                if s<=t:s+=a[i]
                else:t+=a[i]
            largest=max(a);remaining=a.copy();remaining.remove(largest);bits=1
            for x in remaining:bits|=bits<<x
            target=sum(remaining)//2
            while not bits>>target&1:target-=1
            if s!=largest+target:return False,'Chefu does not receive the optimum amount'
        if next(out,None) is not None:return False,'extra output'
        return True,''
    except (ValueError,StopIteration):return False,'invalid order'

def n3(inp, output):
    data=iter(inp.split());out=iter(output.split())
    try:
        for _ in range(int(next(data))):
            n,L,k=(int(next(data)) for _ in range(3));a=[next(data) for _ in range(n)];size=int(next(out));h=next(out)
            if len(h)!=size:return False,'reported string length is wrong'
            positions=[]
            for _ in range(k):
                i,p=int(next(out)),int(next(out))
                if not 0<=i<n or p<0 or h[p:p+L]!=a[i]:return False,'invalid occurrence witness'
                positions.append(p)
            if len(set(positions))!=k:return False,'occurrence positions must differ'
            cost=[[L-max((r for r in range(L) if a[i][L-r:]==a[j][:r]),default=0) for j in range(n)] for i in range(n)]
            dp=[L]*n
            for _ in range(k-1):dp=[min(dp[i]+cost[i][j] for i in range(n)) for j in range(n)]
            if size!=min(dp):return False,'string is not shortest'
        if next(out,None) is not None:return False,'extra output'
        return True,''
    except (ValueError,StopIteration):return False,'invalid shortest-string output'

CHECKERS={'PEPPERA':peppera,'COINPART':coinpart,'N3':n3,'RRPLAYER':float_checker(.1),'RDF':float_checker(1e-6),'PHCUL':float_checker(1e-6),'MEANMEDI':float_checker(.00051)}
