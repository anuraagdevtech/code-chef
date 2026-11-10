#!/usr/bin/env python3
import sys
it=iter(sys.stdin.buffer.read().split());n=int(next(it));m=int(next(it));a=[next(it) for _ in range(n)];d=[bytearray(m+1) for _ in range(n+1)]
for _ in range(int(next(it))):
 x=int(next(it))-1;y=int(next(it))-1;u=int(next(it));v=int(next(it));d[x][y]^=1;d[x][v]^=1;d[u][y]^=1;d[u][v]^=1
out=[]
for i in range(n):
 cur=0;row=d[i];above=d[i-1] if i else bytearray(m+1);r=[]
 for j in range(m):cur^=row[j];row[j]=cur^above[j];r.append(str((a[i][j]-48)^row[j]))
 out.append(''.join(r))
print('\n'.join(out))
