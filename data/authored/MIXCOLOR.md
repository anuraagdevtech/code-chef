---
topic: Arrays
subtopic: Counting duplicates
time: $O(N)$ per test case
space: $O(N)$
---
Each mixing operation changes the value of **exactly one** colour — the receiver becomes $x + y$ while the donor keeps its value. So every operation can fix at most one offending colour, and the question is how many colours must change.

If a value occurs $c$ times, then $c - 1$ of those copies must be altered, since only one may keep it. Summing over all values:

$$\sum_v (c_v - 1) \;=\; N - (\text{number of distinct values})$$

That is a lower bound, and it is achievable: because $A_i \geq 1$, every mix **strictly increases** the receiver's value, so repeatedly mixing a duplicate with the current maximum pushes it above everything present and creates a fresh value each time. No operation is ever wasted.

So the answer is simply $N$ minus the size of the set of values — one pass into a Python `set`.

Sample case 1, $[1,2,3]$, is already distinct and needs nothing. Sample case 2, $[2,1,2]$, has two colours sharing the value $2$, so one of them must be mixed — a single operation.

Values reach $10^9$, so hashing into a set is the right structure rather than an array indexed by value. With $N$ up to $10^5$ and $T \leq 10$ this is comfortable.

Note the answer depends only on **how many** duplicates there are, never on their values — the arithmetic of the mixing never enters the count.

## Edge cases

- **Every *extra* copy costs one operation**, not every duplicated colour: three of a kind needs two mixes, so the answer is $N - \mathrm{distinct}$ rather than the number of colours that repeat.
- **All distinct** (the first row) → $0$.
- **All identical** → $N - 1$.
- **There are always spare colours to mix into**, since the palette is unbounded while $N$ is finite — so each duplicate really is fixable in one operation and the lower bound is achieved.
- **$A_i$ up to $10^9$ with no tie to $N$**, so a set is needed rather than a counting array; the raw byte tokens serve as keys with no integer conversion.
- **$N = 1$** → one colour, zero operations.

## Dry run

| colours | distinct | $N - \mathrm{distinct}$ |
|---|---:|---:|
| $1, 2, 3$ | 3 | `0` |
| $2, 1, 2$ | 2 | `1` |

In the second row one of the two $2$s is repainted to any unused colour.
