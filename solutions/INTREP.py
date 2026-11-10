#!/usr/bin/env python3
"""INTREP: standalone Python 3 solution."""
import sys
def solve(it):
 n=next(it)
 if n%2==0:return str(2*n)+' '+str(n)
 for p in (3,5,7,11,13,17,19,23,29,31,37,41,43,47):
  if n%p:return str(p*n)+' '+str((p-1)*n)

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
