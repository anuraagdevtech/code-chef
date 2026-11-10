#!/usr/bin/env python3
"""RIFFLES: standalone Python 3 solution."""
import sys
def solve(it):
 n,k=next(it),next(it);v=pow(2,k,n-1)
 return ' '.join(str((i*v)%(n-1)+1) for i in range(n-1))+' '+str(n)

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
