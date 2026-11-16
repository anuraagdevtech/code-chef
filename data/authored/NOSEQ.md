---
topic: Constructive
subtopic: Balanced base-K digits read off from the residue
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
The sum is a base-$K$ expansion of $S$ whose digits are restricted to $-1, 0, 1$. Look at it modulo $K$: only $B_1$ matters, so $B_1 \equiv S \pmod K$.

For $K > 2$ the residues $0$, $1$ and $K - 1$ correspond to the digits $0$, $1$ and $-1$ and are all different, so the digit is forced; any other residue makes the task impossible. Subtract the digit, divide by $K$ and continue with the next position. After $N$ digits the remaining value must be 0.

For $K = 2$ the residues 1 and $K - 1$ coincide and the code takes the digit $+1$, which produces the ordinary binary representation. That is sufficient: with digits in $\{-1, 0, 1\}$ the largest reachable value is $2^N - 1$, and every positive $S$ up to that bound is already reached by plain binary.

## Edge cases

- A residue other than $0$, $1$, $K-1$ means no sequence exists.
- $S$ too large for $N$ digits leaves a non-zero remainder at the end.
- The digit $-1$ makes the quotient round up: $(S + 1) / K$.
- Any valid sequence is accepted; for $K > 2$ it is unique anyway.

## Dry run

`N = 3, K = 6, S = 36`:

| step | value | residue | digit | next value |
|---:|---:|---:|---:|---:|
| 1 | 36 | 0 | 0 | 6 |
| 2 | 6 | 0 | 0 | 1 |
| 3 | 1 | 1 | 1 | 0 |

Output `0 0 1`. For `N = 5, K = 5, S = 7` the first residue is 2, so the answer is `-2`.
