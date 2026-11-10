#!/usr/bin/env python3
"""SWAPGAME: standalone Python 3 solution."""
import sys
def solve(it):
 n=next(it);a=[next(it) for _ in range(n)];b=[next(it) for _ in range(n)]
 return str(sum(i*(y-x) for i,(x,y) in enumerate(zip(a,b))))

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
