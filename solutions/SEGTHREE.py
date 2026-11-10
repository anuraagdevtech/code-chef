#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
for _ in range(next(it)):
 n=next(it);cost=[[0]*3 for _ in range(3)]
 for i in range(n):
  a=next(it)%3
  for v in range(3):cost[i%3][v]+=(v-a)%3
 ans=min(cost[0][a]+cost[1][b]+cost[2][(-a-b)%3] for a in range(3) for b in range(3))
 out.append(str(ans))
print('\n'.join(out))
