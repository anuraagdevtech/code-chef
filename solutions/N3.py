#!/usr/bin/env python3
import sys
from array import array
it=iter(sys.stdin.buffer.read().split());out=[]
for _ in range(int(next(it))):
 n,L,k=(int(next(it)) for _ in range(3));strings=[next(it).decode() for _ in range(n)];overlap=[[0]*n for _ in range(n)]
 for j in range(n):
  pattern=strings[j];pi=[0]*L
  for p in range(1,L):
   v=pi[p-1]
   while v and pattern[p]!=pattern[v]:v=pi[v-1]
   pi[p]=v+(pattern[p]==pattern[v])
  for i in range(n):
   matched=0
   for ch in strings[i][1:]:
    while matched and ch!=pattern[matched]:matched=pi[matched-1]
    if ch==pattern[matched]:matched+=1
   overlap[i][j]=matched
 dp=[L]*n;parents=[]
 for _ in range(k-1):
  nd=[10**9]*n;prev=array('h',[-1])*n
  for i in range(n):
   base=dp[i]+L
   for j in range(n):
    v=base-overlap[i][j]
    if v<nd[j]:nd[j]=v;prev[j]=i
  parents.append(prev);dp=nd
 last=min(range(n),key=dp.__getitem__);path=[last]
 for prev in reversed(parents):last=prev[last];path.append(last)
 path.reverse();h=strings[path[0]];positions=[0]
 for i,j in zip(path,path[1:]):positions.append(len(h)-overlap[i][j]);h+=strings[j][overlap[i][j]:]
 out.extend((str(len(h)),h));out.extend(f'{i} {p}' for i,p in zip(path,positions));out.append('')
print('\n'.join(out))
