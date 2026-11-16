#!/usr/bin/env python3
"""Deterministic small-instance oracles for the added roadmap solutions.

These checks enumerate valid operations, subarrays, subsets, or traversal orders,
rather than duplicating the optimised algorithms. Run after tools/verify.py.
"""
from collections import deque
from functools import lru_cache
from itertools import combinations, permutations, product
from math import gcd
from pathlib import Path
import random
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
RNG = random.Random(54721)
CHECKED = 0


def run(code, text):
    process = subprocess.run([sys.executable, '-I', str(ROOT/'solutions'/f'{code}.py')],
                             input=text, text=True, capture_output=True, timeout=30)
    assert process.returncode == 0, (code, process.stderr)
    return process.stdout.split()


def batch(code, cases):
    global CHECKED
    got = run(code, str(len(cases))+'\n'+'\n'.join(case for case,_ in cases)+'\n')
    want = [str(value) for _,expected in cases for value in
            (expected if isinstance(expected,list) else [expected])]
    assert got == want, (code, next(((i,a,b) for i,(a,b) in enumerate(zip(got,want)) if a != b),
                                  ('lengths',len(got),len(want))))
    CHECKED += len(cases)
    print(f'{code}: {len(cases)} oracle cases',flush=True)


def tree(n):
    return [(i,RNG.randrange(i)) for i in range(1,n)]


def adjacency(n, edges):
    graph = [[] for _ in range(n)]
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph


def edge_text(edges, base=1):
    return '\n'.join(f'{u+base} {v+base}' for u,v in edges)


def xor_and_prefix():
    cases = []
    for n in range(1,8):
        for bits in product('01',repeat=n):
            s = ''.join(bits)
            value = 0
            for left in range(n):
                for right in range(left+1,n+1):
                    value ^= int(s[left:right],2)
            cases.append((f'{n}\n{s}',value))
    batch('SUB_XOR',cases)
    cases = []
    for n in range(1,8):
        for k in range(1,n+1):
            distance = [-1]*(1 << n)
            queue = deque()
            for state in range(1 << n):
                if '1'*k in f'{state:0{n}b}':
                    distance[state] = 0
                    queue.append(state)
            while queue:
                u = queue.popleft()
                for width in range(1,n+1):
                    # Reverse-prefix operations are self-inverse, giving an
                    # exhaustive shortest path to any acceptable final string.
                    mask = ((1 << width)-1) << (n-width)
                    v = u^mask
                    if distance[v] == -1:
                        distance[v] = distance[u]+1
                        queue.append(v)
            cases.extend((f'{n} {k}\n{state:0{n}b}',distance[state]) for state in range(1 << n))
    batch('PREFIXFLIP',cases)
    cases = []
    for _ in range(300):
        n = RNG.randint(1,8)
        k = RNG.randint(1,n)
        s = ''.join(RNG.choice('01') for _ in range(n))
        value = 0
        for left in range(n-k+1):
            value ^= int(s[left:left+k],2)
        cases.append((f'{n} {k}\n{s}',value.bit_count()))
    batch('KLXOR',cases)


def arrays():
    cases = []
    for _ in range(250):
        n = RNG.randint(1,6)
        a = [RNG.randint(1,16) for _ in range(n)]
        answer = 10**9
        for removed in range(n):
            for denomination in range(1,max(a)+1):
                others = a[:removed]+a[removed+1:]
                if all(v%denomination == 0 for v in others):
                    answer = min(answer,1+sum(v//denomination for v in others))
        cases.append((f'{n}\n'+ ' '.join(map(str,a)),answer))
    batch('MINNOTES',cases)
    cases = []
    for _ in range(250):
        n,k = RNG.randint(1,6),RNG.randint(1,4)
        a = [RNG.randint(-5,5) for _ in range(n)]
        expanded = a*k
        answer = max(sum(expanded[l:r]) for l in range(len(expanded)) for r in range(l+1,len(expanded)+1))
        cases.append((f'{n} {k}\n'+' '.join(map(str,a)),answer))
    batch('KCON',cases)
    cases = []
    for _ in range(150):
        n = RNG.randint(1,8)
        a = [RNG.randint(0,12) for _ in range(n)]
        total = sum(a)
        answer = n-1
        for mask in range(1,1 << n):
            kept = [a[i] for i in range(n) if mask>>i&1]
            if len(kept)*max(kept) <= total:
                answer = min(answer,n-len(kept))
        cases.append((f'{n}\n'+' '.join(map(str,a)),answer))
    batch('MONKS',cases)
    cases = []
    for _ in range(150):
        n = RNG.randint(1,15)
        a = [RNG.randint(1,5) for _ in range(n)]
        answer = [sum(i != j and a[i] == a[j] and
                      all(v <= a[i] for v in a[min(i,j)+1:max(i,j)])
                      for j in range(n)) for i in range(n)]
        cases.append((f'{n}\n'+' '.join(map(str,a)),answer))
    batch('LUNCHTIM',cases)
    cases = []
    for _ in range(100):
        n = RNG.randint(1,8)
        a = [RNG.randint(1,3) for _ in range(n)]
        answer = sum(len(set(sub)) == len(sub) for mask in range(1,1 << n)
                     for sub in [[a[i] for i in range(n) if mask>>i&1]])
        cases.append((f'{n}\n'+' '.join(map(str,a)),answer))
    batch('DISTELE',cases)


def zero_prefix():
    cases = []
    for _ in range(35):
        n = RNG.randint(1,3)
        s = tuple(RNG.randrange(10) for _ in range(n))
        budget = RNG.randrange(22)
        distance = {s:0}
        queue = deque([s])
        answer = 0
        while queue:
            u = queue.popleft()
            length = 0
            for v in u:
                if v != 0:
                    break
                length += 1
            answer = max(answer,length)
            if distance[u] == budget:
                continue
            for width in range(1,n+1):
                v = tuple((c+1)%10 if i < width else c for i,c in enumerate(u))
                if v not in distance:
                    distance[v] = distance[u]+1
                    queue.append(v)
        cases.append((f'{n} {budget}\n'+''.join(map(str,s)),answer))
    batch('PREZ',cases)


def tree_choices():
    inversion_cases, removal_cases, coupon_cases = [],[],[]
    for _ in range(90):
        n = RNG.randint(1,7)
        edges = tree(n)
        children = [[] for _ in range(n)]
        for v,p in edges:
            children[p].append(v)
        weight = [RNG.randrange(2) for _ in range(n)]
        def traversals(u):
            for ordered in permutations(children[u]):
                lists = [list(traversals(v)) for v in ordered]
                for tails in product(*lists):
                    yield [weight[u]]+[x for tail in tails for x in tail]
        answer = min(sum(a[i] > a[j] for i in range(n) for j in range(i+1,n)) for a in traversals(0))
        inversion_cases.append((f'{n}\n'+' '.join(map(str,weight))+'\n'+edge_text(edges),answer))
        a = [RNG.randint(-5,5) for _ in range(n)]
        penalty = RNG.randint(1,6)
        best = -10**9
        for kept in range(1 << n):
            if any(kept>>v&1 and not kept>>p&1 for v,p in edges):
                continue
            removed_roots = int(not kept&1)+sum(not kept>>v&1 and kept>>p&1 for v,p in edges)
            profit = sum(a[i] for i in range(n) if kept>>i&1)-penalty*removed_roots
            best = max(best,profit)
        removal_cases.append((f'{n} {penalty}\n'+' '.join(map(str,a))+'\n'+edge_text(edges),best))
        if n <= 6:
            toll = [RNG.randint(1,3) for _ in range(n)]
            budget = RNG.randint(1,7)
            paths = [[0] for _ in range(n)]
            for v,p in edges:
                paths[v] = paths[p]+[v]
            best = sum(toll)
            for retained in product(*(range(v+1) for v in toll)):
                if all(sum(retained[i] for i in path) <= budget for path in paths):
                    best = min(best,sum(toll)-sum(retained))
            coupon_cases.append((f'{n} 1 {budget}\n'+' '.join(map(str,toll))+'\n'+edge_text(edges),2*best))
    batch('TREEVERS',inversion_cases)
    batch('SUBREM',removal_cases)
    batch('ABDTOLL',coupon_cases)


def wealth_pairs():
    global CHECKED
    for _ in range(35):
        n = RNG.randint(2,9)
        edges = tree(n)
        parent = [-1]*n
        for v,p in edges:
            parent[v] = p
        w = [RNG.randint(-10,10) for _ in range(n)]
        signed,absolute = -10**9,0
        for v in range(1,n):
            u = parent[v]
            while u != -1:
                signed = max(signed,w[u]-w[v])
                absolute = max(absolute,abs(w[u]-w[v]))
                u = parent[u]
        source = f'{n}\n'+' '.join(map(str,w))+'\n'+' '.join(str(p+1) if p >= 0 else '-1' for p in parent)+'\n'
        assert run('INOI1601',source) == [str(signed)]
        assert run('FAMTREE',source) == [str(absolute)]
        CHECKED += 2
    print('INOI1601/FAMTREE: 70 strict-ancestor oracle cases',flush=True)


def electricity():
    cases = []
    for _ in range(100):
        n = RNG.randint(1,8)
        positions = sorted(RNG.sample(range(30),n))
        sources = [RNG.randrange(2) for _ in range(n)]
        sources[RNG.randrange(n)] = 1
        best = 10**9
        for mask in range(1 << (n-1)):
            valid = True
            cost = 0
            component = sources[0]
            for i in range(n-1):
                if mask>>i&1:
                    component |= sources[i+1]
                    cost += positions[i+1]-positions[i]
                else:
                    valid &= bool(component)
                    component = sources[i+1]
            valid &= bool(component)
            if valid:
                best = min(best,cost)
        cases.append((f'{n}\n'+''.join(map(str,sources))+'\n'+' '.join(map(str,positions)),best))
    batch('CHEFELEC',cases)


def fire():
    cases = []
    for _ in range(100):
        n = RNG.randint(1,8)
        edges = []
        child_count = [0]*n
        for v in range(1,n):
            p = RNG.choice([u for u in range(v) if child_count[u] < 2])
            child_count[p] += 1
            edges.append((p,v))
        graph = adjacency(n,edges)
        marked = {i for i in range(n) if RNG.randrange(3) == 0}
        if not marked:
            marked.add(RNG.randrange(n))
        target = sum(1 << i for i in marked)
        neighbours = [sum(1 << v for v in adj) for adj in graph]
        @lru_cache(None)
        def possible(burning,burned):
            if burning&target:
                return False
            if not burning:
                return True
            spread = 0
            for u in range(n):
                if burning>>u&1:
                    spread |= neighbours[u]
            spread &= ~(burning|burned)
            choices = [0]+[1 << u for u in range(n) if not (burning|burned)>>u&1]
            return any(possible(spread&~shield,burned|burning) for shield in choices)
        expected = 'yes' if possible(1,0) else 'no'
        source = f'{n} 1 {len(marked)}\n'+'\n'.join(str(len(adj))+' '+ ' '.join(str(v+1) for v in adj) for adj in graph)+'\n'+' '.join(str(v+1) for v in marked)
        cases.append((source,expected))
    batch('FIRE',cases)


def wall():
    cases = []
    for width in range(1,7):
        cells = 2*width
        tiles = []
        for col in range(width-1):
            block = [2*col,2*col+1,2*col+2,2*col+3]
            for absent in block:
                tiles.append(sum(1 << v for v in block if v != absent))
        full = (1 << cells)-1
        @lru_cache(None)
        def exact_cover(occupied):
            if occupied == full:
                return 1
            first = next(i for i in range(cells) if not occupied>>i&1)
            answer = exact_cover(occupied | (1 << first))
            for tile in tiles:
                if tile>>first&1 and not tile&occupied:
                    answer += exact_cover(occupied|tile)
            return answer
        cases.append((str(width),exact_cover(0)))
    batch('BWALL',cases)


def main():
    xor_and_prefix()
    arrays()
    zero_prefix()
    tree_choices()
    wealth_pairs()
    electricity()
    fire()
    wall()
    additional_oracles()
    dp_oracles()
    print(f'PASS: {CHECKED} deterministic oracle cases')


def additional_oracles():
    cases = []
    for _ in range(35):
        n = RNG.randint(3,6)
        original = [[RNG.randrange(2) for _ in range(8)] for _ in range(8)]
        expanded = original
        for _ in range(n-3):
            expanded = [row+row[::-1] for row in expanded]
            expanded += expanded[::-1]
        width = len(expanded)
        seen = set()
        components = 0
        for r in range(width):
            for c in range(width):
                if not expanded[r][c] or (r,c) in seen:
                    continue
                components += 1
                stack = [(r,c)]
                seen.add((r,c))
                while stack:
                    x,y = stack.pop()
                    for a,b in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                        if 0 <= a < width and 0 <= b < width and expanded[a][b] and (a,b) not in seen:
                            seen.add((a,b))
                            stack.append((a,b))
        cases.append((str(n)+'\n'+'\n'.join(''.join(map(str,row)) for row in original),components))
    batch('F3',cases)
    cases = []
    for _ in range(100):
        n = RNG.randint(1,9)
        intervals = []
        for _ in range(n):
            left = RNG.randrange(n+1)
            right = RNG.randint(left,n)
            intervals.append((left,right))
        valid = []
        for bits in product('01',repeat=n):
            knights = bits.count('1')
            if all((bit == '1') == (left <= knights <= right) for bit,(left,right) in zip(bits,intervals)):
                valid.append(''.join(bits))
        if valid:
            cases.append((str(n)+'\n'+'\n'.join(f'{l} {r}' for l,r in intervals),[len(valid),min(valid)]))
    batch('BYTEISLE',cases)
    cases = []
    for n in range(2,31):
        count = sum(a%b == c and b%c == 0 for a in range(1,n+1)
                    for b in range(1,n+1) for c in range(1,n+1))
        cases.append((str(n),count))
    batch('SPCTRIPS',cases)
    cases = []
    for _ in range(80):
        n = RNG.randint(1,5)
        a = [RNG.randint(1,6) for _ in range(n)]
        bound = max(a)+1
        best = 10**9
        for b in product(range(1,bound+1),repeat=n):
            if any(x > y for x,y in zip(a,b)) or any(b[i] > b[i+1] for i in range(n-1)):
                continue
            common = 0
            for v in b:
                common = gcd(common,v)
            if common > 1:
                best = min(best,sum(b)-sum(a))
        cases.append((str(n)+'\n'+' '.join(map(str,a)),best))
    batch('CBALLS',cases)
    cases = []
    for n in range(1,65):
        numerator = sum(gcd(a,b) == b for a in range(1,n+1) for b in range(1,n+1))
        denominator = n*n
        divisor = gcd(numerator,denominator)
        cases.append((str(n),f'{numerator//divisor}/{denominator//divisor}'))
    batch('COOLGUYS',cases)
    def is_prime(n):
        return n >= 2 and all(n%d for d in range(2,int(n**0.5)+1))
    batch('PTUPLES',[(str(n),sum(is_prime(a) and is_prime(b) and is_prime(a+b)
                                for a in range(2,n+1) for b in range(a+1,n+1) if a+b <= n))
                    for n in range(1,81)])
    batch('LEVY',[(str(n),sum(is_prime(p) and is_prime(q) and p+2*q == n
                             for p in range(2,n+1) for q in range(2,n+1)))
                 for n in range(1,81)])
    cases = []
    for _ in range(60):
        n = RNG.randint(2,4)
        grid = [[b'.'[0] for _ in range(n)] for _ in range(n)]
        for r in range(n):
            for c in range(n):
                if (r,c) not in ((0,0),(n-1,n-1)):
                    grid[r][c] = RNG.choice(b'...#*')
        treasures = [(r,c) for r in range(n) for c in range(n) if grid[r][c] == 42]
        treasure_bit = {p:1 << i for i,p in enumerate(treasures)}
        full = (1 << len(treasures))-1
        queue = deque([(0,0,0,0)])
        seen = {(0,0,0)}
        expected = -1
        while queue:
            r,c,mask,steps = queue.popleft()
            if (r,c) == (n-1,n-1) and mask == full:
                expected = steps
                break
            for x,y in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                if 0 <= x < n and 0 <= y < n and grid[x][y] != 35:
                    updated = mask|treasure_bit.get((x,y),0)
                    state = (x,y,updated)
                    if state not in seen:
                        seen.add(state)
                        queue.append((x,y,updated,steps+1))
        cases.append((str(n)+'\n'+'\n'.join(bytes(row).decode() for row in grid),expected))
    batch('N1',cases)


def dp_oracles():
    global CHECKED
    cases = []
    for n in range(1,7):
        for p in permutations(range(1,n+1)):
            edges = [(i,j) for i in range(n) for j in range(i+1,n) if p[i] > p[j]]
            possible = False
            for mask in range(1 << n):
                first = sum(mask>>i&1 and mask>>j&1 for i,j in edges)
                second = sum(not mask>>i&1 and not mask>>j&1 for i,j in edges)
                if first == second:
                    possible = True
                    break
            cases.append((str(n)+'\n'+' '.join(map(str,p)),'YES' if possible else 'NO'))
    batch('PERMSPL',cases)
    pp_cases,mchef_cases,marcha_cases = [],[],[]
    for _ in range(100):
        n = RNG.randint(1,8)
        budget = RNG.randint(1,15)
        items = [(RNG.randint(1,4),RNG.randint(1,4),RNG.randint(1,8)) for _ in range(n)]
        best = max(sum(c*p for i,(c,p,t) in enumerate(items) if mask>>i&1)
                   for mask in range(1 << n) if sum(t for i,(c,p,t) in enumerate(items) if mask>>i&1) <= budget)
        pp_cases.append((f'{n} {budget}\n'+'\n'.join(f'{c} {p} {t}' for c,p,t in items),best))
        notes = [RNG.randint(1,12) for _ in range(n)]
        possible = any(sum(v for i,v in enumerate(notes) if mask>>i&1) == budget for mask in range(1 << n))
        marcha_cases.append((f'{n} {budget}\n'+' '.join(map(str,notes)),'Yes' if possible else 'No'))
        a = [RNG.randint(-8,8) for _ in range(n)]
        intervals = []
        for _ in range(RNG.randint(1,8)):
            l = RNG.randrange(n)
            r = RNG.randint(l,n-1)
            intervals.append((l,r,RNG.randint(1,8)))
        costs = [min([c for l,r,c in intervals if l <= i <= r]+[10**9]) for i in range(n)]
        best = max(sum(v for i,v in enumerate(a) if not mask>>i&1)
                   for mask in range(1 << n) if sum(c for i,c in enumerate(costs) if mask>>i&1) <= budget)
        mchef_cases.append((f'{n} {budget} {len(intervals)}\n'+' '.join(map(str,a))+'\n'+
                            '\n'.join(f'{l+1} {r+1} {c}' for l,r,c in intervals),best))
    batch('PPTEST',pp_cases)
    batch('MARCHA1',marcha_cases)
    batch('MCHEF',mchef_cases)
    merge_cases,partition_cases = [],[]
    for _ in range(80):
        a = ''.join(RNG.choice('abc') for _ in range(RNG.randint(1,4)))
        b = ''.join(RNG.choice('abc') for _ in range(RNG.randint(1,4)))
        @lru_cache(None)
        def merges(i,j,last):
            if i == len(a) and j == len(b):
                return 0
            answers = []
            if i < len(a):
                answers.append((a[i] != last)+merges(i+1,j,a[i]))
            if j < len(b):
                answers.append((b[j] != last)+merges(i,j+1,b[j]))
            return min(answers)
        merge_cases.append((f'{len(a)} {len(b)}\n{a}\n{b}',merges(0,0,'')))
        s = ''.join(RNG.choice('ABC') for _ in range(RNG.randint(1,9)))
        @lru_cache(None)
        def partitions(start):
            if start == len(s):
                return (1,0)
            ways = 0
            minimum = len(s)
            for end in range(start+1,len(s)+1):
                part = s[start:end]
                if part == part[::-1]:
                    tail_ways,tail_minimum = partitions(end)
                    ways += tail_ways
                    minimum = min(minimum,tail_minimum+1)
            return ways,minimum
        ways,minimum = partitions(0)
        assert run('COUNTPAL',s+'\n') == [str(ways)]
        CHECKED += 1
        partition_cases.append((f'{len(s)}\n{s}',minimum))
    batch('STRMRG',merge_cases)
    batch('CHGLSTGT',partition_cases)
    print('COUNTPAL: 80 exhaustive partition oracles',flush=True)
    for _ in range(50):
        n = RNG.randint(2,12)
        position = [0]
        for _ in range(n-1):
            position.append(position[-1]+RNG.randint(1,3))
        capacity = RNG.randint(3,8)
        dist = [10**9]*n
        ways = [0]*n
        dist[0],ways[0] = 0,1
        for j in range(1,n):
            for i in range(j):
                if position[j]-position[i] <= capacity:
                    candidate = dist[i]+1
                    if candidate < dist[j]:
                        dist[j],ways[j] = candidate,ways[i]
                    elif candidate == dist[j]:
                        ways[j] += ways[i]
        got = run('TRIP',f'{n} {capacity}\n'+'\n'.join(map(str,position))+'\n')
        assert got == [str(dist[-1]-1),str(ways[-1]%1000000007)],(position,capacity,got)
        CHECKED += 1
    print('TRIP: 50 full-DAG oracles',flush=True)
    cases = []
    for n in range(1,51):
        answer = 0
        for i in range(1,n+1):
            for j in range(1,n+1):
                digits = list(map(int,str(i+j)))
                answer += abs(sum(d if d%2 == 0 else -d for d in digits))
        cases.append((str(n),answer))
    batch('VK18',cases)
    cases = []
    for n in range(2,7):
        for m in range(2,7):
            row_order = [(r,c) for r in range(n) for c in range(m)]
            col_order = [(r,c) for c in range(m) for r in range(n)]
            expected = [len(set(row_order[::k+1])|set(col_order[::k+1])) for k in range(n*m)]
            cases.append((f'{n} {m}',expected))
    batch('DESTCELL',cases)


if __name__ == '__main__':
    main()
