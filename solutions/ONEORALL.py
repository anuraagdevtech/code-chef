#!/usr/bin/env python3
"""ONEORALL: standalone Python 3 solution."""
import sys
def solve(it):
 n=next(it);a=[next(it) for _ in range(n)];win=(sum(a)%2==1) if n%2 else (min(a)%2==1 or sum(a)%2==1)
 return 'CHEF' if win else 'CHEFINA'

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
