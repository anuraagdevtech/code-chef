---
topic: Constructive
subtopic: Three explicit families, impossible only for powers of two
time: $O(1)$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Three constructions cover almost everything:

- $N$ divisible by 3: $A = B = C = N/3$ gives $3 \cdot N/3$.
- $N$ odd, $N \ge 3$: $(1, 1, (N-1)/2)$ gives $1 + 2 \cdot (N-1)/2 = N$.
- $N = 2^a \cdot m$ with $m$ odd and $m \ge 3$: scale the previous idea by $2^a$: $(2^a, 2^a, 2^a (m-1)/2)$ gives $2^a + 2 \cdot 2^a (m-1)/2 = 2^a m$.

What is left are $N < 3$ and the powers of two, and those are impossible. Sort the exponents of 2 in $A, B, C$ as $x \le y \le z$; the three lcms then have exponents $y, z, z$. If $y < z$ the sum is $2^y$ times (odd + even), an odd number that is at least $1 + 2 + 2 = 5$; if $y = z$ it is $2^y$ times a sum of three odd numbers, an odd number at least 3. Either way the sum has an odd factor greater than 1.

## Edge cases

- $N = 1, 2$: three positive lcms sum to at least 3.
- Powers of two (4, 8, 16, ...) have no solution.
- Multiples of 3 that are also even are handled by the first rule.
- Any valid triple is accepted.

## Dry run

- `N = 6`: divisible by 3 - `2 2 2`.
- `N = 7`: odd - `1 1 3`: $1 + 3 + 3 = 7$.
- `N = 20 = 4 * 5`: `4 4 8`: $4 + 8 + 8 = 20$.
- `N = 8`: a power of two - `-1`.
