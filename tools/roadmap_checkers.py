"""Semantic sample checkers for new roadmap solutions with non-unique output."""
from collections import Counter
from math import isfinite


def cab(inp, got):
    data = iter(inp.split())
    result = iter(got.split())
    for _ in range(int(next(data))):
        n, k = int(next(data)), int(next(data))
        word = next(result, '')
        minimum = k // (1 << 25) + (k % (1 << 25)).bit_count()
        feasible = minimum <= n <= k
        if word == '-1':
            if feasible:
                return False, 'reported impossible for a feasible score and length'
        elif (not feasible or len(word) != n or
              any(c < 'a' or c > 'z' for c in word) or
              sum(1 << (ord(c)-97) for c in word) != k):
            return False, 'wrong alphabet, length or total score'
    return (next(result, None) is None), 'valid score construction'


def brknlife(inp, got):
    data = iter(inp.split())
    result = iter(got.split())
    for _ in range(int(next(data))):
        n, m = int(next(data)), int(next(data))
        source, target = next(data), next(data)
        word = next(result, '')
        # Question marks can always avoid matching the next target letter.
        matched = 0
        for c in source:
            if matched < m and c == target[matched]:
                matched += 1
        if word == '-1':
            if matched < m:
                return False, 'a replacement avoiding the target exists'
            continue
        if len(word) != n or any(c not in 'abcde' for c in word):
            return False, 'invalid replacement alphabet or length'
        if any(a != '?' and a != b for a,b in zip(source,word)):
            return False, 'a fixed character changed'
        matched = 0
        for c in word:
            if matched < m and c == target[matched]:
                matched += 1
        if matched == m:
            return False, 'target is still a subsequence'
    return (next(result,None) is None), 'target avoided'


def chefham(inp, got):
    data = iter(map(int,inp.split()))
    result = iter(map(int,got.split()))
    for _ in range(next(data)):
        n = next(data)
        a = [next(data) for _ in range(n)]
        distance = next(result,-1)
        b = [next(result,None) for _ in range(n)]
        if Counter(a) != Counter(b):
            return False, 'output does not preserve the input multiset'
        optimum = min(n,2*(n-max(Counter(a).values())))
        if distance != optimum or sum(x != y for x,y in zip(a,b)) != distance:
            return False, 'Hamming distance is not the optimum'
    return (next(result,None) is None), 'optimal rearrangement'


def taaplusb(inp, got):
    data = list(map(int,inp.split()))
    answers = got.split()
    if len(answers) != data[0]:
        return False, 'wrong number of answers'
    for n, text in zip(data[1:],answers):
        value = float(text)
        expected = n/2-(1-10.0**(-n))/18
        if not isfinite(value) or abs(value-expected) >= 1e-6:
            return False, 'expected carry count outside the absolute tolerance'
    return True, 'within absolute error tolerance'


def zeroone(inp, got):
    data = iter(map(int,inp.split()))
    result = iter(map(int,got.split()))
    for _ in range(next(data)):
        n = next(data)
        a = [next(data) for _ in range(n)]
        b = [next(result,None) for _ in range(n)]
        reported = next(result,-1)
        if Counter(a[::2]) != Counter(b[::2]) or Counter(a[1::2]) != Counter(b[1::2]):
            return False, 'blocks moved between different character classes'
        optimal = [0]*n
        optimal[::2] = sorted(a[::2],reverse=True)
        optimal[1::2] = sorted(a[1::2])
        def score(c):
            zeros = total = 0
            for i,v in enumerate(c):
                if i%2:
                    total += zeros*v
                else:
                    zeros += v
            return total
        if reported != score(b) or reported != score(optimal):
            return False, '01 subsequence count is not optimal or is misreported'
    return (next(result,None) is None), 'optimal compression'


CHECKERS = {'CAB':cab, 'BRKNLIFE':brknlife, 'CHEFHAM':chefham,
            'TAAPLUSB':taaplusb, 'ZEROONE':zeroone}


def evedg(inp, got):
    data = iter(map(int,inp.split()))
    result = iter(map(int,got.split()))
    for _ in range(next(data)):
        n,m = next(data),next(data)
        edges = [(next(data)-1,next(data)-1) for _ in range(m)]
        degree = [0]*n
        for u,v in edges:
            degree[u] += 1
            degree[v] += 1
        optimum = 1 if m%2 == 0 else (2 if any(d%2 for d in degree) else 3)
        k = next(result,-1)
        labels = [next(result,-1) for _ in range(n)]
        if k != optimum or any(not 1 <= c <= k for c in labels):
            return False,'nonminimal part count or invalid label'
        counts = [0]*k
        for u,v in edges:
            if labels[u] == labels[v]:
                counts[labels[u]-1] += 1
        if any(c%2 for c in counts):
            return False,'an induced subgraph has an odd number of edges'
    return (next(result,None) is None),'optimal even-edge partition'


def tourists(inp, got):
    data = iter(map(int,inp.split()))
    n,m = next(data),next(data)
    edges = [(next(data)-1,next(data)-1) for _ in range(m)]
    graph = [[] for _ in range(n)]
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    def reachable(adj):
        seen = {0}
        stack = [0]
        while stack:
            for v in adj[stack.pop()]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        return len(seen) == n
    feasible = all(len(a)%2 == 0 for a in graph) and reachable(graph)
    result = iter(got.split())
    verdict = next(result,'').upper()
    if verdict == 'NO':
        return (not feasible and next(result,None) is None),'Euler orientation infeasible'
    if verdict != 'YES' or not feasible:
        return False,'incorrect feasibility verdict'
    directed = [[] for _ in range(n)]
    reverse = [[] for _ in range(n)]
    balance = [0]*n
    for a,b in edges:
        try:
            u,v = int(next(result))-1,int(next(result))-1
        except (ValueError,StopIteration):
            return False,'missing or invalid edge orientation'
        if (u,v) not in ((a,b),(b,a)):
            return False,'road order or endpoints changed'
        directed[u].append(v)
        reverse[v].append(u)
        balance[u] += 1
        balance[v] -= 1
    if any(balance) or not reachable(directed) or not reachable(reverse):
        return False,'orientation is not strongly connected and balanced'
    return (next(result,None) is None),'directed Euler circuit exists'


def arrgraph(inp, got):
    from math import gcd
    data = iter(map(int,inp.split()))
    result = iter(map(int,got.split()))
    def connected(a):
        seen = {0}
        stack = [0]
        while stack:
            u = stack.pop()
            for v in range(len(a)):
                if v not in seen and gcd(a[u],a[v]) == 1:
                    seen.add(v)
                    stack.append(v)
        return len(seen) == len(a)
    for _ in range(next(data)):
        n = next(data)
        a = [next(data) for _ in range(n)]
        changes = next(result,-1)
        b = [next(result,-1) for _ in range(n)]
        if any(not 2 <= v <= 50 for v in b) or not connected(b):
            return False,'output values or connectivity invalid'
        if changes != sum(x != y for x,y in zip(a,b)) or changes != int(not connected(a)):
            return False,'changes misreported or nonminimal'
    return (next(result,None) is None),'optimal coprime graph construction'


def percapta(inp, got):
    data = iter(map(int,inp.split()))
    result = iter(map(int,got.split()))
    for _ in range(next(data)):
        n,m = next(data),next(data)
        a = [next(data) for _ in range(n)]
        b = [next(data) for _ in range(n)]
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u,v = next(data)-1,next(data)-1
            graph[u].append(v)
            graph[v].append(u)
        best = 0
        for i in range(n):
            if a[i]*b[best] > a[best]*b[i]:
                best = i
        eligible = {i for i in range(n) if a[i]*b[best] == a[best]*b[i]}
        optimum = 0
        unseen = set(eligible)
        while unseen:
            start = unseen.pop()
            component = [start]
            for u in component:
                for v in graph[u]:
                    if v in unseen:
                        unseen.remove(v)
                        component.append(v)
            optimum = max(optimum,len(component))
        k = next(result,-1)
        chosen = {next(result,-1)-1 for _ in range(max(0,k))}
        if k != optimum or len(chosen) != k or not chosen <= eligible:
            return False,'chosen component size, ratio or vertices invalid'
        seen = {next(iter(chosen))}
        stack = list(seen)
        while stack:
            for v in graph[stack.pop()]:
                if v in chosen and v not in seen:
                    seen.add(v)
                    stack.append(v)
        if seen != chosen:
            return False,'chosen provinces are disconnected'
    return (next(result,None) is None),'largest maximum-ratio component'


CHECKERS.update({'EVEDG':evedg,'TOURISTS':tourists,'ARRGRAPH':arrgraph,'PERCAPTA':percapta})


def pathsums(inp, got):
    data = iter(map(int,inp.split()))
    result = iter(map(int,got.split()))
    for _ in range(next(data)):
        n = next(data)
        graph = [[] for _ in range(n)]
        for _ in range(n-1):
            u,v = next(data)-1,next(data)-1
            graph[u].append(v)
            graph[v].append(u)
        a = [next(result,-1) for _ in range(n)]
        if any(not 1 <= v <= 100000 for v in a):
            return False,'value outside the output bounds'
        for start in range(n):
            stack = [(start,-1,a[start],1)]
            while stack:
                u,p,total,length = stack.pop()
                if length > 1 and total%length == 0:
                    return False,'a path has an integer average'
                for v in graph[u]:
                    if v != p:
                        stack.append((v,u,total+a[v],length+1))
    return (next(result,None) is None),'all nontrivial tree paths checked'


CHECKERS['PATHSUMS'] = pathsums


def eartseq(inp, got):
    from math import gcd
    data = iter(map(int,inp.split()))
    result = iter(map(int,got.split()))
    for _ in range(next(data)):
        n = next(data)
        a = [next(result,-1) for _ in range(n)]
        if len(set(a)) != n or any(not 1 <= v <= 10**9 for v in a):
            return False,'values must be distinct positive integers at most 10^9'
        for i in range(n):
            b,c = a[(i+1)%n],a[(i+2)%n]
            if gcd(a[i],b) == 1 or gcd(a[i],b,c) != 1:
                return False,'a cyclic pair or triple GCD condition failed'
    return (next(result,None) is None),'all cyclic GCD conditions satisfied'


CHECKERS['EARTSEQ'] = eartseq


def peppera(inp, got):
    data = iter(inp.split())
    result = iter(got.split())
    for _ in range(int(next(data))):
        n = int(next(data))
        rows = [next(data) for _ in range(n)]
        output = [next(result,'') for _ in range(n)]
        if any(new not in (old,old[::-1]) for old,new in zip(rows,output)):
            return False,'a row is neither the original nor its reversal'
        difference = [r[:n//2].count('1')-r[n//2:].count('1') for r in rows]
        possible = {0}
        for d in difference:
            possible = {v+d for v in possible}|{v-d for v in possible}
        optimum = min(map(abs,possible))
        actual = abs(sum(r[:n//2].count('1')-r[n//2:].count('1') for r in output))
        if actual != optimum:
            return False,'the pepperoni imbalance is not minimal'
    return (next(result,None) is None),'optimal row reversals'


CHECKERS['PEPPERA'] = peppera


# Checkers for the later roadmap batches live in their own modules; a code that
# already has a checker above keeps it.
from seed_checkers_dp_course import CHECKERS as _DP_COURSE
from seed_checkers_advanced_one import CHECKERS as _ADVANCED_ONE
from seed_checkers_advanced_two import CHECKERS as _ADVANCED_TWO
for _extra in (_DP_COURSE, _ADVANCED_ONE, _ADVANCED_TWO):
    for _code, _checker in _extra.items():
        CHECKERS.setdefault(_code, _checker)
