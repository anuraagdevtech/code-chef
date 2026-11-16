---
topic: Bit Manipulation
subtopic: Independent bits - free exactly where A and B differ
time: $O(1)$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
$F(X) = (B \mid X) - (A \mathbin{\&} X)$. Since $A \mathbin{\&} X$ is a submask of $X$, which is a submask of $B \mid X$, the subtraction never borrows and each bit position contributes independently: bit of $(B \mid X)$ minus bit of $(A \mathbin{\&} X)$.

| $a$ | $b$ | $x = 0$ | $x = 1$ |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 1 |
| 1 | 1 | 1 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |

Where the bits of $A$ and $B$ are equal exactly one choice of $x$ is optimal; where they differ both choices give the same contribution. The number of maximising $X$ is therefore $2^{\text{popcount}(A \oplus B)}$.

## Edge cases

- $C = 0$: only $X = 0$ exists and the answer is 1.
- Bits of $X$ above those of $A$ and $B$ are positions where both are 0, so $x = 1$ is forced there.
- $A = B$ gives exactly one optimal $X$, the complement of $A$ within $C$ bits.
- $C$ itself does not appear in the formula because $A, B < 2^C$.

## Dry run

`A = 1, B = 2, C = 3`: $A \oplus B = 3$ has two set bits, so the answer is $2^2 = 4$.

Bit 2 is 0 in both numbers, forcing $x = 1$; bits 0 and 1 are free. The optimal values are $X = 4, 5, 6, 7$.
