#!/usr/bin/env python3
"""KSUM: standalone Python 3 solution."""
import sys
import heapq

def main():
 it=iter(map(int,sys.stdin.buffer.read().split()));n,k=next(it),next(it);a=[next(it) for _ in range(n)];p=[0]
 for x in a:p.append(p[-1]+x)
 h=[(-(p[n]-p[i]),i,n) for i in range(n)];heapq.heapify(h);out=[]
 for _ in range(k):
  v,l,r=heapq.heappop(h);out.append(str(-v))
  if r-1>l:heapq.heappush(h,(-(p[r-1]-p[l]),l,r-1))
 print(' '.join(out))

if __name__ == '__main__':
 main()
