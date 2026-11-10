#!/usr/bin/env python3
import sys
from array import array
read=sys.stdin.buffer.readline
s=read().strip();q=int(read());by={}
for i in range(q):
 a,b,l,r=read().split();by.setdefault((a[0],b[0]),array('I')).extend((i,int(l)-1,int(r)))
chars=sorted(set(s));counts={c:array('I',[0]) for c in chars}
for ch in s:
 for c in chars:counts[c].append(counts[c][-1]+(c==ch))
ans=array('Q',[0])*q
for (a,b),group in by.items():
 if a not in counts or b not in counts:continue
 prefix=array('Q',[0]);ca=counts[a];cb=counts[b];total=0
 for i,ch in enumerate(s):
  if ch==b:total+=ca[i]
  prefix.append(total)
 for j in range(0,len(group),3):
  i,l,r=group[j:j+3];ans[i]=prefix[r]-prefix[l]-ca[l]*(cb[r]-cb[l])
# Bound temporary formatting memory even for a million queries.
for start in range(0,q,8192):sys.stdout.write('\n'.join(map(str,ans[start:start+8192]))+'\n')
