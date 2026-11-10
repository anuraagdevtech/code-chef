"""Deterministic differential tests against small exhaustive models.

Run from any directory: python3 tools/test_remaining.py
"""
from collections import Counter, deque
from itertools import combinations, permutations, product
from math import gcd
from pathlib import Path
from random import Random
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
RNG = Random(20261110)
TOTAL = 0


def check(code, cases):
    global TOTAL
    data = str(len(cases))+'\n'+'\n'.join(case[0] for case in cases)+'\n'
    result = subprocess.run([sys.executable,'-I',str(ROOT/'solutions'/f'{code}.py')],
                            input=data,text=True,capture_output=True,timeout=30)
    assert result.returncode == 0,(code,result.stderr)
    actual = result.stdout.splitlines()
    expected = [str(case[1]) for case in cases]
    assert actual == expected,(code,next(((cases[i][0],e,a) for i,(e,a) in enumerate(zip(expected,actual)) if e != a), (len(actual),len(expected))))
    TOTAL += len(cases)
    print(f'{code}: {len(cases)} cases passed')


def binary_cases():
    xor_cases,flip_cases,klxor_cases,prez_cases = [],[],[],[]
    for n in range(1,9):
        for bits in product('01',repeat=n):
            s = ''.join(bits)
            answer = 0
            for l in range(n):
                for r in range(l+1,n+1):
                    answer ^= int(s[l:r],2)
            xor_cases.append((f'{n}\n{s}',answer))
            distances = {s:0}
            queue = deque([s])
            while queue:
                cur = queue.popleft()
                for end in range(1,n+1):
                    nxt = ''.join('1' if c == '0' else '0' for c in cur[:end])+cur[end:]
                    if nxt not in distances:
                        distances[nxt] = distances[cur]+1
                        queue.append(nxt)
            for k in range(1,n+1):
                answer = min(d for text,d in distances.items() if '1'*k in text)
                flip_cases.append((f'{n} {k}\n{s}',answer))
                val = 0
                for i in range(n-k+1):
                    val ^= int(s[i:i+k],2)
                klxor_cases.append((f'{n} {k}\n{s}',val.bit_count()))
    check('SUB_XOR',xor_cases)
    check('PREFIXFLIP',flip_cases)
    check('KLXOR',klxor_cases)
    for n in range(1,4):
        # BFS from each candidate initial state, independent of the cost formula.
        for _ in range(30):
            s = ''.join(str(RNG.randrange(10)) for _ in range(n))
            distances = {s:0}
            queue = deque([s])
            while queue:
                cur = queue.popleft()
                for end in range(1,n+1):
                    nxt = ''.join(str((int(c)+1)%10) for c in cur[:end])+cur[end:]
                    if nxt not in distances:
                        distances[nxt] = distances[cur]+1
                        queue.append(nxt)
            for budget in (0,1,5,9,15,25):
                answer = max(n-len(text.lstrip('0')) for text,d in distances.items() if d <= budget)
                prez_cases.append((f'{n} {budget}\n{s}',answer))
    check('PREZ',prez_cases)


def array_cases():
    cases = {c:[] for c in ['MINNOTES','MONKS','DISTELE','KCON','LUNCHTIM','SUMQ','SET302','CHEFELEC']}
    for _ in range(200):
        n = RNG.randrange(1,8)
        a = [RNG.randrange(1,10) for _ in range(n)]
        line = ' '.join(map(str,a))
        answer = 10**9
        for idx in range(n):
            for value in range(1,max(a)+1):
                b = a[:]
                b[idx] = value
                common = 0
                for x in b:
                    common = gcd(common,x)
                answer = min(answer,sum(b)//common)
        cases['MINNOTES'].append((f'{n}\n{line}',answer))
        answer = n-1
        total = sum(a)
        for mask in range(1,1<<n):
            keep = [a[i] for i in range(n) if mask >> i & 1]
            if max(keep)*len(keep) <= total:
                answer = min(answer,n-len(keep))
        cases['MONKS'].append((f'{n}\n{line}',answer))
        answer = 0
        for mask in range(1,1<<n):
            b = [a[i] for i in range(n) if mask >> i & 1]
            answer += len(b) == len(set(b))
        cases['DISTELE'].append((f'{n}\n{line}',answer))
        h = RNG.randrange(n,n*10+1)
        rate = next(k for k in range(1,max(a)+1) if sum((x+k-1)//k for x in a) <= h)
        cases['SET302'].append((f'{n} {h}\n{line}',rate))
        visibility = [sum(i != j and a[i] == a[j] and all(a[k] <= a[i] for k in range(min(i,j)+1,max(i,j))) for j in range(n)) for i in range(n)]
        cases['LUNCHTIM'].append((f'{n}\n{line}',' '.join(map(str,visibility))))
        b = [x-5 for x in a]
        k = RNG.randrange(1,6)
        big = b*k
        best = max(sum(big[l:r]) for l in range(len(big)) for r in range(l+1,len(big)+1))
        cases['KCON'].append((f'{n} {k}\n'+ ' '.join(map(str,b)),best))
        b,c = [RNG.randrange(1,10) for _ in range(3)],[RNG.randrange(1,10) for _ in range(4)]
        answer = sum((x+y)*(y+z) for x in a for y in b for z in c if x <= y and z <= y)
        cases['SUMQ'].append((f'{n} 3 4\n{line}\n'+ ' '.join(map(str,b))+'\n'+' '.join(map(str,c)),answer))
        flags = [RNG.randrange(2) for _ in range(n)]
        flags[RNG.randrange(n)] = 1
        x = sorted(RNG.sample(range(30),n))
        best = 10**9
        for mask in range(1<<max(0,n-1)):
            valid = True
            start = 0
            for end in range(n):
                if end == n-1 or not (mask >> end & 1):
                    if not any(flags[start:end+1]):
                        valid = False
                    start = end+1
            if valid:
                best = min(best,sum(x[i+1]-x[i] for i in range(n-1) if mask >> i & 1))
        cases['CHEFELEC'].append((f'{n}\n'+''.join(map(str,flags))+'\n'+' '.join(map(str,x)),best))
    for code,items in cases.items():
        check(code,items)


def tree_cases():
    cases = {c:[] for c in ['SUBREM','ABDTOLL','TREEVERS','DIAMTREE','TR1']}
    for _ in range(150):
        n = RNG.randrange(1,8)
        parent = [0]+[RNG.randrange(i) for i in range(1,n)]
        children = [[] for _ in range(n)]
        edges = []
        for i in range(1,n):
            children[parent[i]].append(i)
            edges.append(f'{parent[i]+1} {i+1}')
        edge_text = '\n'.join(edges)
        ancestors = []
        for i in range(n):
            path = [i]
            while path[-1]:
                path.append(parent[path[-1]])
            ancestors.append(path)
        a = [RNG.randrange(-5,6) for _ in range(n)]
        x = RNG.randrange(1,6)
        best = -10**9
        for mask in range(1<<n):
            kept = [v for v in range(n) if not any(mask >> p & 1 for p in ancestors[v])]
            removals = sum(bool(mask >> v & 1) and not any(mask >> p & 1 for p in ancestors[v][1:]) for v in range(n))
            best = max(best,sum(a[v] for v in kept)-x*removals)
        cases['SUBREM'].append((f'{n} {x}\n'+' '.join(map(str,a))+'\n'+edge_text,best))
        toll = [RNG.randrange(1,4) for _ in range(n)]
        budget = RNG.randrange(1,7)
        best = 10**9
        for kept in product(*(range(x+1) for x in toll)):
            if all(sum(kept[p] for p in path) <= budget for path in ancestors):
                best = min(best,2*(sum(toll)-sum(kept)))
        cases['ABDTOLL'].append((f'{n} 1 {budget}\n'+' '.join(map(str,toll))+'\n'+edge_text,best))
        weights = [RNG.randrange(2) for _ in range(n)]
        def traversals(v):
            for order in permutations(children[v]):
                choices = [list(traversals(u)) for u in order]
                for seq in product(*choices):
                    yield [weights[v]]+[x for s in seq for x in s]
        best = min(sum(s[i] > s[j] for i in range(n) for j in range(i+1,n)) for s in traversals(0))
        cases['TREEVERS'].append((f'{n}\n'+' '.join(map(str,weights))+'\n'+edge_text,best))
        distances = []
        lcas = 0
        for u in range(n):
            for v in range(n):
                common = next(p for p in ancestors[u] if p in ancestors[v])
                lcas += common+1
                distances.append(ancestors[u].index(common)+ancestors[v].index(common))
        cases['DIAMTREE'].append((f'{n}\n'+edge_text,max(distances)))
        cases['TR1'].append((f'{n}\n'+edge_text,lcas))
    for code,items in cases.items():
        check(code,items)


if __name__ == '__main__':
    binary_cases()
    array_cases()
    tree_cases()
    print(f'Total: {TOTAL} differential cases passed')
