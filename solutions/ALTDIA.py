#!/usr/bin/env python3
"""ALTDIA: standalone Python 3 solution."""
import sys
def solve(it):
 b,w=next(it),next(it);n=b+w
 if n==1:return 'B' if b else 'W'
 if not b or not w:return '-1'
 if w>=2:s='B'*(b)+'W'*w
 else:s='W'+'B'*b
 return s+'\n'+'\n'.join('1 '+str(i) for i in range(2,n+1))

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
