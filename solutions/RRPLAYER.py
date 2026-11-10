#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()));ns=[next(it) for _ in range(next(it))];h=[0.0]*(max(ns,default=0)+1)
for i in range(1,len(h)):h[i]=h[i-1]+1/i
print('\n'.join('%.10f'%(n*h[n]) for n in ns))
