[&larr; 724. GCD Queries](GCD_QUERIES.md) &middot; [Index](../../README.md)

# 731. Squarified

> CodeChef problem code [`SQUAR`](https://www.codechef.com/problems/SQUAR) &middot; difficulty **2470** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Group by square-free kernel and take the largest non-trivial group |
| **Time** | $O(V \log \log V + N \log V)$, $V$ the largest value in the input |
| **Space** | $O(V + N)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

You are given an array $A$ of length $N$.
An array $B$ is considered *squarified*, if:
- The product of the elements in any even-length [subsequence](https://en.wikipedia.org/wiki/Subsequence) of $B$ is a [perfect square](https://en.wikipedia.org/wiki/Perfect_square), and;
- The product of the elements in any odd-length subsequence of $B$ is **not** a perfect square.

Your task is to find the length of the **longest subsequence** of $A$ which is *squarified*.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$ — the number of elements in the array.
    - The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots ,A_N$ — the elements of the array.

**Output**

For each test case, output on a new line, the length of the **longest subsequence** of $A$ which is `squarified`.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^7$
- The sum of $N$ over all test cases won't exceed $5\cdot 10^5$.

## Sample

**Sample input**

```
3
4
7 18 8 10
5
27 8 12 16 12
2
9 1
```

**Sample output**

```
2
3
0
```

<details><summary>Explanation</summary>

**Test Case $1$:** $[18,8]$ is the longest squarified subsequence of the array.
- Even length subsequence is $[18, 8]$. Here, $18\cdot 8 = 144 = 12^2$.
- Odd length subsequence are $[18]$ and $[8]$. None of these are perfect squares.

**Test Case $2$:** $[27,12,12]$ is the longest squarified subsequence of the array.
- Even length subsequences are $[27,12]$ and $[12,12]$ with products $324$ and $144$ respectively. Both of these are perfect squares.
- Odd length subsequences are $[27],[12],$ and $[27,12,12]$ with products $27,12$ and $3888$. None of these are perfect squares.

**Test Case $3$:** There is no squarified subsequence present, hence answer is 0.

</details>

## Approach

The square-free kernel of a number is the product of the primes that occur in it with an odd exponent; a number is a perfect square exactly when its kernel is 1, and a product of two numbers is a perfect square exactly when their kernels are equal.

Apply the conditions to subsequences of length 1 and 2: no element may be a perfect square, and every two elements must have the same kernel. Conversely, if all elements share a kernel $k \ne 1$, then a product of $m$ of them is $k^m$ times a perfect square - a square for even $m$ and a non-square for odd $m$. So squarified subsequences are exactly the sets of elements with one common kernel different from 1.

Compute every kernel with a smallest-prime-factor sieve and print the largest multiplicity among the kernels other than 1 (0 if there is none). The sieve is sized by the largest number in the whole input, which is read up front.

## Solution (Python)

```python
import sys
from array import array
from collections import Counter


raw = list(map(int, sys.stdin.buffer.read().split()))
V = max(raw)
spf = array('I', [0]) * (V + 1)
for i in range(2, int(V ** 0.5) + 1):
    if not spf[i]:
        for j in range(i * i, V + 1, i):
            if not spf[j]:
                spf[j] = i


def solve(tokens):
    n = next(tokens)
    count = Counter()
    for _ in range(n):
        value = next(tokens)
        kernel = 1
        while value > 1:
            prime = spf[value] or value
            odd = 0
            while value % prime == 0:
                value //= prime
                odd ^= 1
            if odd:
                kernel *= prime
        if kernel != 1:
            count[kernel] += 1
    return str(max(count.values(), default=0))


if __name__ == "__main__":
    tokens = iter(raw)
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Complexity

- **Time:** $O(V \log \log V + N \log V)$, $V$ the largest value in the input
- **Space:** $O(V + N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Perfect squares, including 1, can never be used.
- If every element is a perfect square the answer is 0.
- A single non-square element gives a valid subsequence of length 1.
- The sieve only stores a factor for composites; a zero entry means the number is prime.

## Dry run

`A = [27, 8, 12, 16, 12]`.

Kernels: $27 = 3^3 \to 3$, $8 = 2^3 \to 2$, $12 = 2^2 \cdot 3 \to 3$, $16 = 2^4 \to 1$, $12 \to 3$.

Kernel 3 occurs three times, kernel 2 once, and the kernel 1 is ignored. Answer 3 (`27, 12, 12`).

---

Same problem in rating order (#696 of 735): [../../by-rating/696-SQUAR.md](../../by-rating/696-SQUAR.md)
