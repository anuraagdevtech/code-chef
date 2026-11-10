#!/usr/bin/env python3
import sys
it=iter(sys.stdin.buffer.read().split());out=[]
for _ in range(int(next(it))):
 n=int(next(it));s=next(it).decode();ones=s.count('1');zeros=n-ones
 if min(ones,zeros)==0:out.append(f'{n} 0');continue
 diff=abs(ones-zeros);minor='0' if ones>zeros else '1';ops=[]
 for _ in range(diff):
  i=next(i for i in range(len(s)-1) if s[i]!=s[i+1]);ops.append(f'{i+1} {i+2} {minor}');s=s[:i]+minor+s[i+2:]
 ops.append(f'1 {len(s)} 0');out.append(f'1 {len(ops)}');out.extend(ops)
print('\n'.join(out))
