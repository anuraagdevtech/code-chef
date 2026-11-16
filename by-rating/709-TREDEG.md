[&larr; 708. Mean Mean Medians](708-MEANMEDI.md) &middot; [Index](README.md) &middot; [710. Coin Partition &rarr;](710-COINPART.md)

# 709. Trees and Degrees

> [`TREDEG`](https://www.codechef.com/problems/TREDEG) &middot; difficulty **2783** &middot; time limit **3s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Pruefer codes and the coefficient of a power of an exponential generating function |
| **Complexity class** | Linear times polylog $O(n \log^2 n)$ |
| **Time** | $O(N)$ for $K = 1$; otherwise $O(N \log K)$ plus $O(\log N)$ levels of big-integer convolutions |
| **Space** | $O(N)$ coefficients plus the big-integer workspace |

## Question

Vivek is quite fond of expected values. One day, he stumbled upon the following problem. He cannot solve it, so he is asking you for help.

Consider all trees with $N$ vertices (numbered $1$ through $N$); two trees are different if there is a pair of vertices $u$ and $v$ such that there is an edge between vertices $u$ and $v$ in exactly one of these trees.

For a uniformly randomly chosen tree $T$, let's denote the degrees of vertices $1$ through $N$ in this tree by $d_1, d_2, \ldots, d_N$. Then, let's denote $A = (d_1 \cdot d_2 \cdot \ldots \cdot d_N)^K$. Find the expected value of $A$.

It can be proved that the expected value of $A$ can be expressed as a fraction $P/Q$, where $P$ and $Q$ are coprime positive integers and $Q$ is coprime to $998,244,353$. You should compute the value of $P \cdot Q^{-1}$ modulo $998,244,353$, where $Q^{-1}$ denotes the multiplicative inverse of $Q$ modulo $998,244,353$.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $N$ and $K$.

**Output**
For each test case, print a single line containing one integer ― $P \cdot Q^{-1} \pmod{998244353}$.

**Constraints**
- $1 \le T \le 100$
- $2 \le N \le 2,000,000$
- $1 \le K \le 10^9$
- the sum of $N$ over all test cases does not exceed $2,000,000$

**Subtasks**
**Subtask #1 (20 points):**
- $T = 10$
- $2 \le N \le 7$

**Subtask #2 (30 points):** the sum of $N$ over all test cases does not exceed $100,000$

**Subtask #3 (50 points):** $K = 1$

## Constraints

- $1 \le T \le 100$
- $2 \le N \le 2,000,000$
- $1 \le K \le 10^9$
- the sum of $N$ over all test cases does not exceed $2,000,000$

## Sample

**Sample input**

```
2
3 1
4 2
```

**Sample output**

```
2
748683279
```

<details><summary>Explanation</summary>

**Example case 1:** There are $3$ labelled trees with size $3$: the paths $[1-2-3]$, $[1-3-2]$ and $[3-1-2]$.

The expected value is $\left((1 \cdot 2 \cdot 1)^1 + (1 \cdot 1 \cdot 2)^1 + (2 \cdot 1 \cdot 1)^1\right) / 3 = 2$, so $P = 2$, $Q = 1$, $Q^{-1} = 1$ and the answer is $2$.

</details>

## Approach

In a Pruefer code a vertex of degree $d$ appears exactly $d - 1$ times, and every sequence of length $N - 2$ is the code of exactly one tree. Summing $\prod d_i^K$ over all trees is therefore a sum over sequences, which by the multinomial theorem equals

$$(N-2)! \cdot [x^{N-2}] \; F(x)^N, \qquad F(x) = \sum_{c \ge 0} (c+1)^K \frac{x^c}{c!},$$

and the expectation divides this by the number of trees, $N^{N-2}$.

For $K = 1$, $F(x) = (1 + x) e^x$, so $F^N = (1+x)^N e^{Nx}$ and the coefficient is a single sum whose consecutive terms have a simple ratio: $\sum_j \binom{N}{j} \frac{(N-2)!}{(N-2-j)!} N^{-j}$, evaluated in $O(N)$.

For general $K$, let $G = F^N$. Differentiating gives $G' = N \frac{F'}{F} G$, i.e. $k \, g_k = \sum_{j} h_j \, g_{k-1-j}$ with $h = N F'/F$. The series $1/F$ comes from Newton iteration, and the recurrence - each coefficient depends on all earlier ones - is solved by divide and conquer, convolving the finished left half into the right half. Polynomial products are done exactly by packing coefficients into one big Python integer with enough bits per slot (Kronecker substitution).

## Solution

```python
import sys
from array import array


MOD = 998244353


def multiply(a, b, limit=None):
    if not a or not b:
        return []
    size = len(a) + len(b) - 1
    if limit is not None:
        size = min(size, limit)
        a, b = (a[:size], b[:size])
    if min(len(a), len(b)) <= 24:
        result = [0] * size
        for i, x in enumerate(a):
            for j in range(min(len(b), size - i)):
                result[i + j] += x * b[j]
        return [x % MOD for x in result]
    width = ((min(len(a), len(b)) * (MOD - 1) ** 2).bit_length() + 7) // 8
    first = int.from_bytes(b''.join((x.to_bytes(width, 'little') for x in a)), 'little')
    second = int.from_bytes(b''.join((x.to_bytes(width, 'little') for x in b)), 'little')
    product = first * second
    packed = product.to_bytes((product.bit_length() + 7) // 8, 'little')
    packed = packed[:size * width].ljust(size * width, b'\x00')
    return [int.from_bytes(packed[i:i + width], 'little') % MOD for i in range(0, size * width, width)]


def reciprocal(a, size):
    result = [pow(a[0], MOD - 2, MOD)]
    while len(result) < size:
        length = min(size, 2 * len(result))
        residual = multiply(a[:length], result, length)
        residual = [-x % MOD for x in residual]
        residual[0] = (residual[0] + 2) % MOD
        result = multiply(result, residual, length)
    return result


def general(n, k, inverse):
    size = n - 1
    invfact = 1
    f = []
    factorial = 1
    for d in range(size):
        if d:
            invfact = invfact * inverse[d] % MOD
            factorial = factorial * d % MOD
        f.append(pow(d + 1, k, MOD) * invfact % MOD)
    if size == 1:
        return 1
    derivative = [d * f[d] % MOD for d in range(1, size)]
    h = multiply(derivative, reciprocal(f, size - 1), size - 1)
    h = [x * n % MOD for x in h]
    coefficients = [0] * size
    coefficients[0] = 1
    pending = [0] * size

    def solve(left, right):
        if right - left == 1:
            if left:
                coefficients[left] = pending[left] * inverse[left] % MOD
            return
        middle = (left + right) // 2
        solve(left, middle)
        contribution = multiply(coefficients[left:middle], h[:right - left - 1], right - left - 1)
        for pos in range(middle, right):
            pending[pos] = (pending[pos] + contribution[pos - left - 1]) % MOD
        solve(middle, right)
    solve(0, size)
    return coefficients[-1] * factorial % MOD * pow(pow(n, n - 2, MOD), MOD - 2, MOD) % MOD


def solve():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    cases = [(next(tokens), next(tokens)) for _ in range(next(tokens))]
    limit = max((n for n, k in cases))
    inverse = array('I', [0]) * (limit + 1)
    inverse[1] = 1
    for i in range(2, limit + 1):
        inverse[i] = MOD - MOD // i * inverse[MOD % i] % MOD
    out = []
    for n, k in cases:
        if k == 1:
            term = answer = 1
            invn = inverse[n]
            for j in range(n - 2):
                term = term * (n - j) * (n - 2 - j) % MOD * inverse[j + 1] % MOD * invn % MOD
                answer = (answer + term) % MOD
        else:
            answer = general(n, k, inverse)
        out.append(str(answer))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
```

## Edge cases

- $N = 2$: the only tree has both degrees 1 and the answer is 1.
- The modulus is 998244353, and $N^{N-2}$ is inverted with Fermat's little theorem.
- $K = 1$ has to take the linear path - it is where the largest $N$ occurs.
- The packing width must hold a full convolution sum, otherwise coefficients would carry into each other.

## Dry run

`N = 3, K = 1`. The sum over $j = 0, 1$:

- $j = 0$: 1
- $j = 1$: $\binom{3}{1} \cdot \frac{1!}{0!} \cdot \frac{1}{3} = 1$

Answer 2. Check: the three labelled trees on 3 vertices are paths with degree product $1 \cdot 2 \cdot 1 = 2$ each.

---

Same problem grouped by topic: [../docs/combinatorics/TREDEG.md](../docs/combinatorics/TREDEG.md)
