#!/usr/bin/env python3
import sys
p=1000000007;inv5=pow(5,p-2,p)
def fib(n):
 a,b=0,1
 for bit in bin(n)[2:]:
  c=a*((2*b-a)%p)%p;d=(a*a+b*b)%p
  if bit=='0':a,b=c,d
  else:a,b=d,(c+d)%p
 return a,b
out=[]
for n in list(map(int,sys.stdin.buffer.read().split()))[1:]:
 f,g=fib(n+1);h=(f+g)%p;j=(g+h)%p
 c1=((n+3)*(2*j-h)-h)*inv5%p
 c2=((n+4)*(2*(h+j)-j)-j)*inv5%p
 out.append(str((c1+c2-3*g-2*h-3*f)%p))
print('\n'.join(out))
