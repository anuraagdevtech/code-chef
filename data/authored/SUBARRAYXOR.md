---
topic: Constructive
subtopic: Choose the prefix xors first - make them 0, 1, ..., N
time: $O(N)$ per test case
space: $O(N)$ for the output
complexity_note: Auxiliary space excludes the buffered input and output.
---
The xor of a subarray $[L, R]$ equals $P_R \oplus P_{L-1}$, where $P$ is the prefix-xor array with $P_0 = 0$. It is non-zero for every subarray exactly when all $N + 1$ prefix values are pairwise distinct.

So pick the prefix values directly: $P_i = i$. Then $A_i = P_i \oplus P_{i-1} = i \oplus (i - 1)$, a number of the form $2^k - 1$, which is at least 1 and at most $2N$ - well inside the allowed range for $N \le 10^5$.

## Edge cases

- $A_i$ is never 0 because $i \ne i - 1$.
- The largest element is below $2^{18}$, under the $10^6$ limit.
- Many arrays are valid (powers of two, primes, ...), so the judge uses a checker.
- $N = 1$ prints `1`.

## Dry run

`N = 6`: $A = 1, 3, 1, 7, 1, 3$.

Prefix xors: `1 2 3 4 5 6` - all distinct and non-zero, so no subarray has xor 0. For example the subarray `3 1 7` has xor $P_4 \oplus P_1 = 4 \oplus 1 = 5$.
