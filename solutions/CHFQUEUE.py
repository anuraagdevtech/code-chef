#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()));n=next(it);next(it);a=[next(it) for _ in range(n)];stack=[];ans=1
for i in range(n-1,-1,-1):
 while stack and a[stack[-1]]>=a[i]:stack.pop()
 if stack:ans=ans*(stack[-1]-i+1)%1000000007
 stack.append(i)
print(ans)
