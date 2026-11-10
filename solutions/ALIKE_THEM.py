#!/usr/bin/env python3
"""ALIKE_THEM: standalone Python 3 solution."""
import sys
def solve(it):
 n,m=next(it),next(it); p=[next(it)-1 for _ in range(n)]; a=[next(it) for _ in range(n)]; src=list(range(n))
 for i in range(n):src[i]=src[p[i]]
 used=set(src); fixed={a[i] for i in used if a[i]}; free=sum(a[i]==0 for i in range(n) if i not in used)
 return str(0 if len(fixed)>1 else pow(m,free+(not fixed),1000000007))

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
