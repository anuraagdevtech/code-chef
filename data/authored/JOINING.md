---
topic: Number Theory
subtopic: Counting residues in a range
time: $O(1)$ per test case
space: $O(1)$
---
Candidate $i$ joins on day $\lceil i/5 \rceil$. When candidate $K$ withdraws, everyone numbered above $K$ shifts down one place, so a candidate originally at position $j > K$ now sits at $j - 1$ and joins on day $\lceil (j-1)/5 \rceil$.

Their day changes only when that shift crosses a day boundary — that is, when

$$\left\lceil \frac{j}{5} \right\rceil \neq \left\lceil \frac{j-1}{5} \right\rceil$$

which happens precisely when $j$ is the **first** candidate of a block of five, i.e. $j \equiv 1 \pmod 5$.

So the answer counts the integers $j$ in $(K, N]$ with $j \equiv 1 \pmod 5$, computed as a difference of two prefix counts.

The insight is that shifting everyone down by one does **not** change most people's day — only those standing exactly at a block boundary move. The naive reading, that everyone after $K$ is affected, would give $N - K$ and fail every sample.

Sample case 4 ($N = 14$, $K = 2$) is the clearest: candidates $6$ and $11$ are the block leaders above $K$, so two people shift to an earlier day, giving $2$. Sample case 1 has only candidate $6$ qualifying. Sample cases 2 and 3 answer $0$ — in case 2 the withdrawal is the last candidate, so nobody shifts at all.

Note that candidates below $K$ are never affected, which is why the count starts strictly above $K$.

## Edge cases

- **$K = N$** (the second row): nobody moves, so $0$.
- **The count of block leaders is $\lceil n/5 \rceil = (n+4)//5$, not $(n+3)//5$.** This is a real off-by-one that the sample catches: leaders are the positions $1, 6, 11, \ldots$, so for $n = 6$ there are two of them, while a $+3$ variant reports one. It was exactly this that a sample run flagged while this solution was being written.
- **Adjacent positions** ($N = 2$, $K = 1$): no leader lies strictly above $K$, so $0$.
- The subtraction counts leaders in the half-open range $(K, N]$, which is why both ends use the same helper rather than an adjusted bound.

## Dry run

Block leaders are the positions $\equiv 1 \pmod 5$: $1, 6, 11, \ldots$

| $N$ | $K$ | leaders $\leq N$ | leaders $\leq K$ | difference | output |
|---:|---:|---:|---:|---:|---|
| 7 | 3 | 2 ($1, 6$) | 1 ($1$) | 1 | `1` |
| 6 | 6 | 2 | 2 | 0 | `0` |
| 2 | 1 | 1 | 1 | 0 | `0` |
| 14 | 2 | 3 ($1,6,11$) | 1 | 2 | `2` |

Row 2 is where $(n+3)//5$ would wrongly give $1$ instead of $2$.
