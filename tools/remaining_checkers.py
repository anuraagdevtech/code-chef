"""Output validators for the remaining-roadmap solutions."""
from collections import Counter
from math import gcd, isfinite


def cab(inp, got):
    it, ans = iter(inp.split()), iter(got.split())
    for _ in range(int(next(it))):
        n,k = int(next(it)),int(next(it))
        s = next(ans)
        minimum = k//(1 << 25)+(k % (1 << 25)).bit_count()
        if s == '-1':
            assert not minimum <= n <= k
        else:
            assert len(s) == n and all('a' <= c <= 'z' for c in s)
            assert sum(1 << (ord(c)-97) for c in s) == k
    assert next(ans,None) is None
    return True,'valid cyberstring'


def brknlife(inp, got):
    it,ans = iter(inp.split()),iter(got.split())
    for _ in range(int(next(it))):
        n,m = int(next(it)),int(next(it))
        s,a = next(it),next(it)
        result = next(ans)
        def subsequence(text):
            j = 0
            for c in text:
                if j < m and c == a[j]:
                    j += 1
            return j == m
        if result == '-1':
            assert subsequence(s.replace('?',''))
        else:
            assert len(result) == n
            assert all(x == '?' or x == y for x,y in zip(s,result))
            assert all(c in 'abcde' for c in result)
            assert not subsequence(result)
    assert next(ans,None) is None
    return True,'valid completion'


def chefham(inp, got):
    it,ans = iter(map(int,inp.split())),iter(map(int,got.split()))
    for _ in range(next(it)):
        n = next(it)
        a = [next(it) for _ in range(n)]
        claimed = next(ans)
        b = [next(ans) for _ in range(n)]
        assert Counter(a) == Counter(b)
        distance = sum(x != y for x,y in zip(a,b))
        optimal = min(n,2*(n-max(Counter(a).values())))
        assert claimed == distance == optimal
    assert next(ans,None) is None
    return True,'optimal Hamming distance'


def zeroone(inp, got):
    it,ans = iter(map(int,inp.split())),iter(map(int,got.split()))
    for _ in range(next(it)):
        n = next(it)
        a = [next(it) for _ in range(n)]
        b = [next(ans) for _ in range(n)]
        claimed = next(ans)
        assert Counter(a[::2]) == Counter(b[::2])
        assert Counter(a[1::2]) == Counter(b[1::2])
        def score(c):
            total = zeros = 0
            for i,x in enumerate(c):
                if i % 2:
                    total += zeros*x
                else:
                    zeros += x
            return total
        a[::2] = sorted(a[::2],reverse=True)
        a[1::2] = sorted(a[1::2])
        assert claimed == score(b) == score(a)
    assert next(ans,None) is None
    return True,'optimal subsequence count'


def evedg(inp, got):
    it,ans = iter(map(int,inp.split())),iter(map(int,got.split()))
    for _ in range(next(it)):
        n,m = next(it),next(it)
        edges = [(next(it)-1,next(it)-1) for _ in range(m)]
        degree = [0]*n
        for u,v in edges:
            degree[u] += 1
            degree[v] += 1
        optimum = 1 if m % 2 == 0 else 2 if any(d % 2 for d in degree) else 3
        k = next(ans)
        labels = [next(ans) for _ in range(n)]
        assert k == optimum and set(labels) == set(range(1,k+1))
        counts = [0]*(k+1)
        for u,v in edges:
            if labels[u] == labels[v]:
                counts[labels[u]] += 1
        assert not any(x % 2 for x in counts)
    assert next(ans,None) is None
    return True,'minimum even-edge partition'


def tourists(inp, got):
    it,ans = iter(inp.split()),iter(got.split())
    n,m = int(next(it)),int(next(it))
    edges = [(int(next(it))-1,int(next(it))-1) for _ in range(m)]
    adj = [[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)
    seen = {0}
    stack = [0]
    while stack:
        for u in adj[stack.pop()]:
            if u not in seen:
                seen.add(u)
                stack.append(u)
    feasible = len(seen) == n and all(len(row) % 2 == 0 for row in adj)
    status = next(ans)
    assert status in ('YES','NO') and (status == 'YES') == feasible
    if feasible:
        balance = [0]*n
        for u,v in edges:
            a,b = int(next(ans))-1,int(next(ans))-1
            assert (a,b) in ((u,v),(v,u))
            balance[a] += 1
            balance[b] -= 1
        assert not any(balance)
    assert next(ans,None) is None
    return True,'Eulerian orientation'


def pathsums(inp, got):
    it,ans = iter(map(int,inp.split())),iter(map(int,got.split()))
    for _ in range(next(it)):
        n = next(it)
        adj = [[] for _ in range(n)]
        for _ in range(n-1):
            u,v = next(it)-1,next(it)-1
            adj[u].append(v)
            adj[v].append(u)
        a = [next(ans) for _ in range(n)]
        assert all(1 <= x <= 100000 for x in a)
        for root in range(n):
            stack = [(root,-1,a[root],1)]
            while stack:
                v,p,total,length = stack.pop()
                if length > 1:
                    assert total % length
                for u in adj[v]:
                    if u != p:
                        stack.append((u,v,total+a[u],length+1))
    assert next(ans,None) is None
    return True,'all paths valid'


def arrgraph(inp, got):
    it,ans = iter(map(int,inp.split())),iter(map(int,got.split()))
    def connected(a):
        seen = {0}
        stack = [0]
        while stack:
            v = stack.pop()
            for u in range(len(a)):
                if u not in seen and gcd(a[u],a[v]) == 1:
                    seen.add(u)
                    stack.append(u)
        return len(seen) == len(a)
    for _ in range(next(it)):
        n = next(it)
        a = [next(it) for _ in range(n)]
        claimed = next(ans)
        b = [next(ans) for _ in range(n)]
        assert all(2 <= x <= 50 for x in b)
        assert claimed == sum(x != y for x,y in zip(a,b)) == (0 if connected(a) else 1)
        assert connected(b)
    assert next(ans,None) is None
    return True,'minimum connected-array changes'


def checked(fn):
    def validate(inp,got):
        try:
            return fn(inp,got)
        except (AssertionError,ValueError,StopIteration,IndexError) as error:
            return False,f'invalid output ({type(error).__name__})'
    return validate


def eartseq(inp,got):
    it,ans = iter(map(int,inp.split())),iter(map(int,got.split()))
    for _ in range(next(it)):
        n = next(it)
        a = [next(ans) for _ in range(n)]
        assert len(set(a)) == n and all(1 <= x <= 10**9 for x in a)
        for i in range(n):
            assert gcd(a[i],a[(i+1)%n]) > 1
            assert gcd(gcd(a[i],a[(i+1)%n]),a[(i+2)%n]) == 1
    assert next(ans,None) is None
    return True,'cyclic gcd conditions valid'


CHECKERS = {code:checked(fn) for code,fn in {
    'CAB':cab, 'BRKNLIFE':brknlife, 'CHEFHAM':chefham,
    'ZEROONE':zeroone, 'EVEDG':evedg, 'TOURISTS':tourists,
    'PATHSUMS':pathsums, 'ARRGRAPH':arrgraph, 'EARTSEQ':eartseq,
}.items()}
