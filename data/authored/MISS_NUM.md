---
topic: Brute Force
subtopic: Guessing which two values are the sum and difference
time: $O(1)$ per test case — twelve candidate assignments
space: $O(1)$
---
The four written values are $a+b$, $a-b$, $ab$ and $\lfloor a/b \rfloor$ in unknown order. Trying to identify them by size is fragile — the product is usually largest but not always, and the quotient can tie with others.

Instead, exploit that **two of them determine everything**. If we guess which value is the sum $s$ and which is the difference $d$, then

$$a = \frac{s+d}{2}, \qquad b = \frac{s-d}{2}$$

There are only $4 \times 3 = 12$ ordered choices, so try them all. For each, require $s+d$ to be even (otherwise $a$ is not an integer) and both $a$ and $b$ to lie in $[1, 10^4]$, then **verify** by recomputing all four quantities and comparing the sorted lists against the sorted input.

Verifying the full multiset rather than just the two unused values is what makes this safe: it automatically handles duplicates among the four numbers, which a positional check would mishandle.

The problem guarantees uniqueness when a solution exists, so the first match can be returned immediately.

Sample case 1, $[-1, 72, 0, 17]$: taking $s = 17$ and $d = -1$ gives $a = 8$, $b = 9$, and recomputing yields $17, -1, 72, 0$ — the same multiset, so the answer is `8 9`. Note the output order matters: $a$ first, and here $a < b$, which is why the difference is the negative value.

Sample case 2 exhausts all twelve assignments without a match and prints `-1 -1`.

The guarantee that at most one of the four is negative is a consistency hint — only $a-b$ can be — but the verification step makes relying on it unnecessary.

## Edge cases

- **The sum and difference pin down $a$ and $b$.** From $s = a+b$ and $d = a-b$ we get $a = (s+d)/2$ and $b = (s-d)/2$, so guessing which two of the four written values are the sum and the difference leaves nothing to search — twelve ordered pairs in all.
- **The parity check comes first**: if $s + d$ is odd the candidate cannot yield integers, so it is discarded before dividing.
- **The recovered pair must be verified against the whole multiset**, not just against $s$ and $d$ — the product and the quotient must match too. Comparing sorted lists handles duplicates for free.
- **The range $[1, 10^4]$ must be enforced** on the recovered values, or a wildly wrong candidate could accidentally reproduce some of the numbers.
- **At most one of the four can be negative** (only $a - b$ can be), which is a useful sanity check on the input but not needed by the algorithm.
- **No solution** → `-1 -1` (the second row), printed as a pair rather than a single value.
- **Uniqueness is guaranteed** when a solution exists, so the first match can be returned immediately.

## Dry run

First sample: the written values are $-1, 72, 0, 17$.

Trying $s = 17$ and $d = -1$:

| step | value |
|---|---:|
| $a = (17 + (-1))/2$ | 8 |
| $b = (17 - (-1))/2$ | 9 |
| $a + b$ | 17 ✓ |
| $a - b$ | $-1$ ✓ |
| $a \cdot b$ | 72 ✓ |
| $\lfloor a/b \rfloor$ | 0 ✓ |

All four match, so the output is `8 9`.
