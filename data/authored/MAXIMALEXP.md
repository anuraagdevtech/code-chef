---
topic: Basic Math
subtopic: The two residues have one of two possible sums - split it evenly
time: $O(1)$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Let $a = X \bmod K$ and $b = (N - X) \bmod K$. Their sum is congruent to $N$ modulo $K$ and lies in $[0, 2K - 2]$, so with $r = N \bmod K$ it is either $r$ or $r + K$; the larger sum requires $N \ge K$.

For a fixed sum the product $a \cdot b$ is largest when the two parts are as equal as possible. That gives two candidates:

- sum $r$: $X = \lfloor r / 2 \rfloor$;
- sum $r + K$ (only if $N \ge K$): $X = \lfloor (r + K) / 2 \rfloor$.

Both values are at most $N$. Evaluate $F$ at each candidate and print the better one; when the larger sum is not actually attainable (for $r = K - 1$) the second candidate just evaluates to something no better.

## Edge cases

- $K = 1$: every residue is 0 and any $X$ is correct.
- $N < K$: only the sum $r = N$ exists and $X = \lfloor N / 2 \rfloor$.
- $N = 0$: the only choice is $X = 0$.
- Several $X$ can be optimal, so the output is checked by value rather than by text.

## Dry run

`N = 4, K = 7`: $r = 4$ and $N < K$, so the only candidate is $X = 2$ with $F = 2 \cdot 2 = 4$.

`N = 8, K = 3`: $r = 2$. Candidates $X = 1$ with $F = 1 \cdot (7 \bmod 3) = 1$ and $X = 2$ with $F = 2 \cdot (6 \bmod 3) = 0$. Print 1; its value equals that of the sample answer $X = 4$.
