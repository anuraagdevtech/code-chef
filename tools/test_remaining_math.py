"""Independent small-model checks for the final mathematical solutions."""
from collections import Counter
from functools import lru_cache
from importlib.util import module_from_spec,spec_from_file_location
from itertools import combinations,permutations,product
from pathlib import Path
from random import Random
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
RNG=Random(73249)
checks=0


def load(code):
    spec=spec_from_file_location(code,ROOT/'solutions'/f'{code}.py')
    module=module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run(code,text):
    result=subprocess.run([sys.executable,'-I',str(ROOT/'solutions'/f'{code}.py')],input=text,text=True,capture_output=True,timeout=30)
    assert result.returncode==0,(code,result.stderr)
    return result.stdout.strip()


def batch(code,cases):
    global checks
    text=str(len(cases))+'\n'+'\n'.join(inp for inp,want in cases)+'\n'
    got=run(code,text).splitlines()
    expected='\n'.join(str(want) for inp,want in cases).splitlines()
    assert got==expected,(code,next(((cases[i],g) for i,g in enumerate(got) if g!=expected[i]),'length mismatch'))
    checks+=len(cases)


def test_expectations():
    global checks
    m=load('INFDIV');p=m.MOD
    got=m.expectations(700)
    want=[0]*701
    for x in range(1,len(want)):
        want[x]=(1+sum(want[x%r] for r in range(1,x+1)))*pow(x,p-2,p)%p
    assert got==want
    checks+=len(want)
    for _ in range(40):
        n=RNG.randrange(1,60);start=RNG.randrange(1,200)
        dp=[0]*(start+1)
        for value in range(1,start+1):
            changing=min(n,value)
            dp[value]=(n+sum(dp[value%r] for r in range(1,changing+1)))*pow(changing,p-2,p)%p
        assert int(run('INFDIV',f'{n} {start}\n'))==dp[start]
        checks+=1


def test_degrees():
    global checks
    m=load('TREDEG');p=m.MOD
    inverse=[0]+[pow(i,p-2,p) for i in range(1,100)]
    cases=[]
    for n in range(2,8):
        for k in [1,2,3,9,123456789]:
            total=0
            for seq in product(range(n),repeat=n-2):
                counts=Counter(seq);value=1
                for v in range(n):value=value*(1+counts[v])%p
                total=(total+pow(value,k,p))%p
            want=total*pow(pow(n,n-2,p),p-2,p)%p
            assert m.general(n,k,inverse)==want,(n,k)
            cases.append((f'{n} {k}',want))
            checks+=1
    batch('TREDEG',cases)
    for _ in range(50):
        a=[RNG.randrange(p) for _ in range(RNG.randrange(25,80))]
        b=[RNG.randrange(p) for _ in range(RNG.randrange(25,80))]
        want=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):want[i+j]=(want[i+j]+x*y)%p
        assert m.multiply(a,b)==want
        checks+=1


def test_mobiles():
    @lru_cache(None)
    def count(weights):
        if len(weights)==1:return 1
        total=sum(weights)
        if total%2:return 0
        lefts=set()
        for mask in range(1,(1<<len(weights))-1):
            left=tuple(weights[i] for i in range(len(weights)) if mask>>i&1)
            if sum(left)==total//2:lefts.add(left)
        answer=0
        for left in lefts:
            remaining=list(weights)
            for value in left:remaining.remove(value)
            answer+=count(left)*count(tuple(remaining))
        return answer
    cases=[]
    for n in range(1,8):
        for _ in range(60):
            weights=tuple(sorted(RNG.choices([1,2,3,4,6,8],k=n)))
            cases.append((f'{n}\n'+' '.join(map(str,weights)),count(weights)))
    batch('MOBCNT',cases)


def test_matrix_orbits():
    global checks
    for n,m in [(1,1),(1,4),(2,2),(2,3),(3,3)]:
        representatives=set()
        for flat in product(range(2),repeat=n*m):
            canonical=min(tuple(flat[r*m+c] for r in rows for c in cols) for rows in permutations(range(n)) for cols in permutations(range(m)))
            representatives.add(canonical)
        assert int(run('ADIMAT',f'{n} {m}\n'))==len(representatives),(n,m)
        checks+=1
    assert run('ADIMAT','10 10\n')=='508361223'
    checks+=1


def test_leagues():
    global checks
    module=load('M3')
    for _ in range(160):
        n=RNG.randrange(1,7)
        wins=[0]*n;matches=[]
        for u,v in combinations(range(n),2):
            status=RNG.randrange(3)
            if status==2 and len(matches)<8:matches.append((u,v))
            else:wins[u if status%2 else v]+=1
        possible=[False]*n
        for bits in product(range(2),repeat=len(matches)):
            final=wins[:]
            for (u,v),bit in zip(matches,bits):final[v if bit else u]+=1
            for i in range(n):possible[i]|=final[i]==max(final)
        for i in range(n):
            limit=wins[i]+sum(i in edge for edge in matches)
            assert module.feasible(n,matches,wins,i,limit)==possible[i]
            checks+=1


def test_knights():
    cases=[]
    for n in range(1,9):
        for _ in range(30):
            intervals=[]
            for i in range(n):
                a,b=sorted([RNG.randrange(n+1),RNG.randrange(n+1)])
                intervals.append((a,b))
            valid=[]
            for bits in product(range(2),repeat=n):
                total=sum(bits)
                if all(bool(b)==(left<=total<=right) for b,(left,right) in zip(bits,intervals)):
                    valid.append(''.join(map(str,bits)))
            if valid:cases.append((str(n)+'\n'+'\n'.join(f'{a} {b}' for a,b in intervals),f'{len(valid)}\n{min(valid)}'))
    # Flatten the two-line answers for the common batch helper.
    batch('BYTEISLE',[(inp,want) for inp,want in cases])


def test_reflections():
    cases=[]
    for exponent in range(3,7):
        for _ in range(12):
            grid=[[RNG.randrange(2) for _ in range(8)] for _ in range(8)]
            initial='\n'.join(''.join(map(str,row)) for row in grid)
            for _ in range(exponent-3):
                grid=[row+row[::-1] for row in grid]
                grid=grid+grid[::-1]
            seen=set();components=0;size=len(grid)
            for r in range(size):
                for c in range(size):
                    if not grid[r][c] or (r,c) in seen:continue
                    components+=1;stack=[(r,c)];seen.add((r,c))
                    while stack:
                        x,y=stack.pop()
                        for u,v in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                            if 0<=u<size and 0<=v<size and grid[u][v] and (u,v) not in seen:
                                seen.add((u,v));stack.append((u,v))
            cases.append((str(exponent)+'\n'+initial,components))
    batch('F3',cases)


if __name__=='__main__':
    test_expectations();test_degrees();test_mobiles();test_matrix_orbits();test_leagues();test_reflections();test_knights()
    print(f'{checks} independent mathematical and state-model checks passed')
