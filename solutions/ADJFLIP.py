#!/usr/bin/env python3
"""ADJFLIP: standalone Python 3 solution."""
import sys
def solve(it):
 n=int(next(it));s=next(it);v=sum((1 if i%2==0 else -1) for i,c in enumerate(s) if c==49)
 return 'Yes' if v==0 or (n%2 and v==1) else 'No'

if __name__ == '__main__':
 it=iter(sys.stdin.buffer.read().split())
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
