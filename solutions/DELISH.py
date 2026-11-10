#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()));out=[]
for _ in range(next(it)):
 n=next(it);a=[next(it) for _ in range(n)];lo=[0]*n;hi=[0]*n;l=h=a[0];lo[0]=hi[0]=a[0]
 for i in range(1,n):
  l=min(a[i],l+a[i]);h=max(a[i],h+a[i]);lo[i]=min(lo[i-1],l);hi[i]=max(hi[i-1],h)
 l=h=a[-1];mn=mx=a[-1];ans=0
 for i in range(n-2,-1,-1):
  ans=max(ans,abs(hi[i]-mn),abs(lo[i]-mx));l=min(a[i],l+a[i]);h=max(a[i],h+a[i]);mn=min(mn,l);mx=max(mx,h)
 out.append(str(ans))
print('\n'.join(out))
