---
topic: Bit Manipulation
subtopic: Bits are independent, so count per column
time: $O(N \log \max A)$ per test case
space: $O(1)$
---
An operation picks a **single** bit position $p$ and flips it in at most $K$ chosen elements. Since it never touches any other bit, the $30$ bit positions are **completely independent problems** — the work for bit $p$ cannot help bit $q$.

For bit $p$, let $c_p$ be how many elements currently have it set. Every one of those must be flipped, and each operation flips at most $K$ of them, so bit $p$ needs exactly

$$\left\lceil \frac{c_p}{K} \right\rceil$$

operations — the bound is tight because the chosen indices are free, so every operation can flip a full $K$ until the last.

Summing over the bits gives the answer:

$$\sum_{p} \left\lceil \frac{c_p}{K} \right\rceil$$

Separating a problem by bit position is the standard move whenever the operation is XOR with a power of two, and here it turns an apparently tangled search into $30$ independent counting problems.

Working the sample, $A = [3, 6, 10]$ with $K = 2$: in binary $0011$, $0110$, $1010$. The column counts are $1, 3, 1, 1$ for bits $0$ through $3$, giving $1 + 2 + 1 + 1 = 5$.

Note bit $1$ is the only column needing two operations — three elements at two per operation. Bits set in a single element still cost one operation each, which is why the total exceeds the largest column count.

Counting columns is one pass over the array per bit, or equivalently one pass accumulating all $30$ counters at once.

## Edge cases

- **One operation touches exactly one bit position**, so the $30$ bit columns are completely independent and the answer is a sum over them — no interaction to reason about.
- **A column with $c$ set bits needs $\lceil c/K \rceil$ operations**, since each operation can clear at most $K$ of them and there is never a reason to flip a zero bit on.
- **Already all zero** → $0$ operations, which falls out of every column having $c = 0$.
- **$K \geq N$ makes each non-empty column cost exactly one**, so the answer is the number of distinct bit positions used anywhere in the array.
- **$A_i$ up to $10^9$** fits in $30$ bits, so the column array is a fixed $30$ entries regardless of $N$.
- **The low-bit trick** (`x & -x`) walks only the set bits, so a sparse value costs far less than $30$ steps per element.
- **$A_i$ may be $0$** and contributes nothing to any column.

## Dry run

Sample: $K = 2$, $A = 3, 6, 10$ — binary $0011$, $0110$, $1010$.

| bit | which elements have it | count $c$ | $\lceil c/2 \rceil$ |
|---:|---|---:|---:|
| 0 | 3 | 1 | 1 |
| 1 | 3, 6, 10 | 3 | 2 |
| 2 | 6 | 1 | 1 |
| 3 | 10 | 1 | 1 |

Total `5`. Bit $1$ is the only column needing two operations, since three indices exceed $K = 2$.
