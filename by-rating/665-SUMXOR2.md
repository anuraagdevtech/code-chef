[&larr; 664. K-Subarrays](664-CHESUB.md) &middot; [Index](README.md) &middot; [666. Chefs Favourite Function &rarr;](666-CHEFFFUNC.md)

# 665. XOR Sums

> [`SUMXOR2`](https://www.codechef.com/problems/SUMXOR2) &middot; difficulty **2306** &middot; time limit **3s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Per-bit signed coefficients from a three-term recurrence, grouped by bit count |
| **CodeChef tags** | `Mathematics`, `Bit Manipulation`, `Transformations`, `Algorithms`, `Simple Algos`, `Bitwise Operation`, `FFT`, `NTT`, `Prefix Sum` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(30 \cdot N + Q)$ |
| **Space** | $O(N)$ |

## Question

You are given a sequence of positive integers $A_1, A_2, \ldots, A_N$. You should answer $Q$ queries. In each query:
- You are given a positive integer $M$.
- Consider all non-empty subsequences of $A$ with length $\le M$. Recall that a subsequence is any sequence that can be created by deleting zero or more elements without changing the order of the remaining elements.
- For each of these subsequences, compute the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) of its elements. Your task is to determine the sum of these values. Since this sum can be very large, compute it modulo $998,244,353$.

**Input**
- The first line of the input contains a single integer $N$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
- The third line contains a single integer $Q$.
- $Q$ lines follow. Each of these lines contains a single integer $M$ describing a query.

**Output**
For each query, print a single line containing one integer ― the sum of bitwise XORs for all subsequences of $A$ with length $\le M$, modulo $998,244,353$.

**Constraints**
- $1 \leq N, Q \leq 2 \cdot 10^5$
- $1 \leq A_i \lt 2^{30}$ for each valid $i$
- $1 \leq M \leq N$

**Subtask**
**Subtask #1 (10 points):** $1 \leq N, Q \leq 1,000$

**Subtask #2 (90 points):** original constraints

## Constraints

- $1 \leq N, Q \leq 2 \cdot 10^5$
- $1 \leq A_i \lt 2^{30}$ for each valid $i$
- $1 \leq M \leq N$

## Sample

**Sample input**

```
4
1 3 5 2
2
1
2
```

**Sample output**

```
11
34
```

<details><summary>Explanation</summary>

In the first query, the answer is just the sum of elements of $A$ (modulo $998,244,353$), which is $1+3+5+2 = 11$.

In the second query, the answer is the sum of bitwise XORs for all subsequences with length $1$ or $2$, which is $1+3+5+2 + (1 \oplus 3) + (1 \oplus 5) + (1 \oplus 2) + (3 \oplus 5) + (3 \oplus 2) + (5 \oplus 2) = 34$.

</details>

## Approach

Handle each bit separately. If $c$ of the $N$ numbers have bit $b$, a subsequence contributes $2^b$ exactly when it contains an odd number of those $c$ elements. Let $f_k$ be (number of size-$k$ subsets with an even count) minus (number with an odd count); then the number with an odd count is $(\binom{N}{k} - f_k) / 2$.

$f_k$ is the coefficient of $z^k$ in $F(z) = (1 - z)^c (1 + z)^{N - c}$. Taking the logarithmic derivative, $(1 - z^2) F' = \bigl((N - 2c) - N z\bigr) F$, and comparing coefficients gives

$$(k + 1) f_{k+1} = (N - 2c) f_k - (N - k + 1) f_{k-1}, \qquad f_0 = 1,\; f_1 = N - 2c,$$

so all $f_k$ follow in linear time without any convolution.

The recurrence depends on the bit only through $c$, so bits with the same count are merged by adding their weights $2^b$; there are at most 30 groups. Accumulate, for every size $k$, the total contribution of subsequences of exactly that size, then take prefix sums over $k$ so that a query $M$ is a single lookup.

## Solution

```python
import sys


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(tokens)
    counts = [0] * 30
    for _ in range(n):
        x = next(tokens)
        while x:
            v = x & -x
            counts[v.bit_length() - 1] += 1
            x -= v
    MOD = 998244353
    inverse = [0, 1] + [0] * (n - 1)
    for k in range(2, n + 1):
        inverse[k] = MOD - MOD // k * inverse[MOD % k] % MOD
    binom = [1] * (n + 1)
    for k in range(1, n + 1):
        binom[k] = binom[k - 1] * (n - k + 1) % MOD * inverse[k] % MOD
    groups = {}
    for b, count in enumerate(counts):
        if count:
            groups[count] = (groups.get(count, 0) + (1 << b)) % MOD
    answers = [0] * (n + 1)
    half = (MOD + 1) // 2
    for count, weight in groups.items():
        drift = n - 2 * count
        previous = 1
        current = drift % MOD
        weight = weight * half % MOD
        for k in range(1, n + 1):
            answers[k] = (answers[k] + weight * (binom[k] - current)) % MOD
            previous, current = (current, (drift * current - (n - k + 1) * previous) * inverse[k + 1] % MOD if k < n else 0)
    for k in range(1, n + 1):
        answers[k] = (answers[k] + answers[k - 1]) % MOD
    q = next(tokens)
    print('\n'.join((str(answers[next(tokens)]) for _ in range(q))))


if __name__ == "__main__":
    main()
```

## Edge cases

- A bit present in no element contributes nothing and is skipped.
- $M$ may equal $N$; the recurrence is not advanced past $k = N$.
- Division by 2 and by $k + 1$ are modular inverses modulo $998244353$.
- For $k = 1$ the odd count is simply $c$, so the answer for $M = 1$ is the sum of the array.

## Dry run

`A = [1, 3, 5, 2]`: bit 0 occurs 3 times, bit 1 twice, bit 2 once.

For $k = 1$: $f_1 = N - 2c$, so the odd count is $(4 - (4 - 2c)) / 2 = c$. Contribution $1 \cdot 3 + 2 \cdot 2 + 4 \cdot 1 = 11$, the answer for $M = 1$.

For $k = 2$: $f_2 = ((N - 2c) f_1 - N f_0) / 2$ gives $0, -2, 0$ for $c = 3, 2, 1$, so the odd counts are $(6 - f_2)/2 = 3, 4, 3$ and the contribution is $3 + 8 + 12 = 23$. The answer for $M = 2$ is $11 + 23 = 34$.

---

Same problem grouped by topic: [../docs/combinatorics/SUMXOR2.md](../docs/combinatorics/SUMXOR2.md)
