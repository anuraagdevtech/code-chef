"""Pruefer degree generating function, using exact bigint convolution.

For K=1, the generating function is exp(N*x)*(1+x)^N and gives a
linear recurrence for the summands. Other K use formal power series.
"""
import sys
from array import array

MOD = 998244353


def multiply(a,b,limit=None):
    if not a or not b:
        return []
    size = len(a)+len(b)-1
    if limit is not None:
        size = min(size,limit)
        a,b = a[:size],b[:size]
    if min(len(a),len(b)) <= 24:
        result = [0]*size
        for i,x in enumerate(a):
            for j in range(min(len(b),size-i)):
                result[i+j] += x*b[j]
        return [x % MOD for x in result]
    # Each integer digit has enough bits for a complete convolution sum,
    # so there can be no carry from one coefficient into the next.
    width = ((min(len(a),len(b))*(MOD-1)**2).bit_length()+7)//8
    first = int.from_bytes(b''.join(x.to_bytes(width,'little') for x in a),'little')
    second = int.from_bytes(b''.join(x.to_bytes(width,'little') for x in b),'little')
    product = first*second
    packed = product.to_bytes((product.bit_length()+7)//8,'little')
    packed = packed[:size*width].ljust(size*width,b'\0')
    return [int.from_bytes(packed[i:i+width],'little') % MOD for i in range(0,size*width,width)]


def reciprocal(a,size):
    result = [pow(a[0],MOD-2,MOD)]
    while len(result) < size:
        length = min(size,2*len(result))
        residual = multiply(a[:length],result,length)
        residual = [(-x) % MOD for x in residual]
        residual[0] = (residual[0]+2) % MOD
        result = multiply(result,residual,length)
    return result


def general(n,k,inverse):
    size = n-1
    invfact = 1
    f = []
    factorial = 1
    for d in range(size):
        if d:
            invfact = invfact*inverse[d] % MOD
            factorial = factorial*d % MOD
        f.append(pow(d+1,k,MOD)*invfact % MOD)
    if size == 1:
        return 1
    derivative = [d*f[d] % MOD for d in range(1,size)]
    h = multiply(derivative,reciprocal(f,size-1),size-1)
    h = [x*n % MOD for x in h]
    coefficients = [0]*size
    coefficients[0] = 1
    pending = [0]*size

    def solve(left,right):
        if right-left == 1:
            if left:
                coefficients[left] = pending[left]*inverse[left] % MOD
            return
        middle = (left+right)//2
        solve(left,middle)
        contribution = multiply(coefficients[left:middle],h[:right-left-1],right-left-1)
        for pos in range(middle,right):
            pending[pos] = (pending[pos]+contribution[pos-left-1]) % MOD
        solve(middle,right)

    solve(0,size)
    return coefficients[-1]*factorial % MOD*pow(pow(n,n-2,MOD),MOD-2,MOD) % MOD


def solve():
    it = iter(map(int,sys.stdin.buffer.read().split()))
    cases = [(next(it),next(it)) for _ in range(next(it))]
    limit = max(n for n,k in cases)
    inverse = array('I',[0])*(limit+1)
    inverse[1] = 1
    for i in range(2,limit+1):
        inverse[i] = MOD-(MOD//i)*inverse[MOD % i] % MOD
    out = []
    for n,k in cases:
        if k == 1:
            term = answer = 1
            invn = inverse[n]
            for j in range(n-2):
                term = term*(n-j)*(n-2-j) % MOD*inverse[j+1] % MOD*invn % MOD
                answer = (answer+term) % MOD
        else:
            answer = general(n,k,inverse)
        out.append(str(answer))
    sys.stdout.write('\n'.join(out))


if __name__ == '__main__':
    solve()
