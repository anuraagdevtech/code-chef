[&larr; 567. Trip](567-TRIP.md) &middot; [Index](README.md) &middot; [569. Winter &rarr;](569-ELWINTER.md)

# 568. Maximum Factors Problem

> [`MXFACS`](https://www.codechef.com/problems/MXFACS) &middot; difficulty **2006** &middot; time limit **0.5s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Remove one copy of the prime with the largest exponent |
| **CodeChef tags** | `Mathematics`, `Number Theory`, `Integer Factorisation`, `Divisors`, `Algorithms`, `Prime Divisors`, `Greedy` |
| **Complexity class** | Square root $O(\sqrt{n})$ |
| **Time** | $O(\sqrt{N})$ per test case |
| **Space** | $O(1)$ |

## Question

You are given an integer $N$. Let $K$ be a divisor of $N$ **of your choice** such that $K > 1$, and let $M = \frac{N}{K}$. You need to find the **smallest** $K$ such that $M$ has as many divisors as possible.

**Note**: $U$ is a divisor of $V$ if $V$ is divisible by $U$.

**Input**

- The first line of the input contains an integer $T$ - the number of test cases. The test cases then follow.
- The only line of each test case contains an integer $N$.

**Output**

For each test case, output in a single line minimum value of $K$ such that $M$ has as many divisors as possible.

## Constraints

- $1 \leq T \leq 3000$
- $2 \leq N \leq 10^9$

## Sample

**Sample input**

```
3
3
4
6
```

**Sample output**

```
3
2
2
```

<details><summary>Explanation</summary>

- **Test case $1$**: The only possible value for $K$ is $3$, and that is the answer.
- **Test case $2$**: There are two cases:
    - $K = 2$. Then $M = \frac{4}{2} = 2$, which has $2$ divisors ($1$ and $2$).
    - $K = 4$. Then $M = \frac{4}{4} = 1$, which has $1$ divisor ($1$).

Therefore the answer is $2$.
- **Test case $3$**: There are three cases:
    - $K = 2$. Then $M = \frac{6}{2} = 3$, which has $2$ divisors ($1$ and $3$).
    - $K = 3$. Then $M = \frac{6}{3} = 2$, which has $2$ divisors ($1$ and $2$).
    - $K = 6$. Then $M = \frac{6}{6} = 1$, which has $1$ divisor ($1$).

Therefore the answer is $2$.

</details>

## Approach

Write $N = \prod p_i^{e_i}$; it has $\prod (e_i + 1)$ divisors. Dividing by $K$ lowers some exponents, and every lowered exponent shrinks the divisor count, so an optimal $K$ removes as little as possible: a single prime.

Removing one copy of a prime with exponent $e$ multiplies the divisor count by $e / (e + 1)$, which is largest for the largest $e$. So the answer is the prime with the maximum exponent, and among several such primes the smallest one - the smallest $K$ is asked for.

Trial division up to $\sqrt{N}$ visits the primes in increasing order, so keeping the first prime that strictly improves the best exponent gives the smallest one automatically. A leftover factor greater than 1 is a prime with exponent 1; it is the answer only when $N$ itself is prime.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        best = 0
        answer = n
        prime = 2
        while prime * prime <= n:
            exponent = 0
            while n % prime == 0:
                n //= prime
                exponent += 1
            if exponent > best:
                best = exponent
                answer = prime
            prime = 3 if prime == 2 else prime + 2
        if best == 0:
            answer = n
        out.append(str(answer))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- $N$ prime: the only possible $K$ is $N$.
- Ties in the exponent are broken towards the smaller prime by the strict comparison.
- A large prime factor above $\sqrt{N}$ has exponent 1 and never beats an earlier prime.
- $K = 1$ is not allowed, so something always has to be removed.

## Dry run

`N = 12 = 2^2 * 3`. Trial division finds exponent 2 for the prime 2 (best so far) and exponent 1 for 3 (no improvement).

Answer $K = 2$: $M = 6$ has 4 divisors, whereas $K = 3$ would leave $M = 4$ with only 3.

---

Same problem grouped by topic: [../docs/number-theory/MXFACS.md](../docs/number-theory/MXFACS.md)
