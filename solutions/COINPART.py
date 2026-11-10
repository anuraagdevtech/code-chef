#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()));out=[]
for _ in range(next(it)):
 n=next(it);a=[next(it) for _ in range(n)];big=max(range(n),key=a.__getitem__);ids=[i for i in range(n) if i!=big];history=[1]
 for i in ids:history.append(history[-1]|history[-1]<<a[i])
 target=sum(a[i] for i in ids)//2
 while not history[-1]>>target&1:target-=1
 low=[];high=[]
 for j in range(len(ids)-1,-1,-1):
  i=ids[j]
  if history[j]>>target&1:high.append(i)
  else:low.append(i);target-=a[i]
 low.insert(0,big);s=t=0;order=[]
 while low or high:
  if s<=t:i=low.pop();s+=a[i]
  else:i=high.pop();t+=a[i]
  order.append(str(i+1))
 out.append(' '.join(order))
print('\n'.join(out))
