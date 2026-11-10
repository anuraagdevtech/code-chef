#!/usr/bin/env python3
"""ABCSTR: standalone Python 3 solution."""
import sys
def main():
 s=sys.stdin.buffer.read().strip();x=y=ans=0;c={(0,0):1}
 for a in s:
  if a==65:x+=1;y+=1
  elif a==66:x-=1
  else:y-=1
  key=(x,y);ans+=c.get(key,0);c[key]=c.get(key,0)+1
 print(ans)

if __name__ == '__main__':
 main()
