#!/usr/bin/env python3
"""CHANDWEIGHT: standalone Python 3 solution."""
import sys
def solve(it):
 n=next(it);w=[next(it) for _ in range(n)];a=[next(it) for _ in range(n)];pref=[0]*(n+1);suf=[0]*(n+1)
 for i in range(n):pref[i+1]=max(a[i],pref[i])-w[i]
 for i in range(n-1,-1,-1):suf[i]=max(a[i],suf[i+1])-w[i]
 return ' '.join(str(max(a[i],pref[i]+suf[i+1])-w[i]) for i in range(n))

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
