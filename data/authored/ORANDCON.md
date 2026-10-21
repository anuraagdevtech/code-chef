---
topic: Bit Manipulation
subtopic: The expression computes a bitwise majority
time: $O(1)$ per test case
space: $O(1)$
---
Read the expression bit by bit. A bit survives $(A \mid B) \mathbin{\&} (B \mid C) \mathbin{\&} (C \mid A)$ exactly when it is present in all three pairwise ORs — which happens precisely when **at least two of $A, B, C$ carry it**. A bit in only one of them is missing from the OR of the other two, and a bit in none is missing everywhere.

So the expression is the bitwise **majority** of $A$, $B$ and $C$, and the task is to make that majority equal $X$.

The easy construction gives all three numbers every bit of $X$ — a unanimous majority — and then makes them distinct using bits that appear in **only one** number each, so they never reach the majority:

$$A = X, \qquad B = X \mid 2^{27}, \qquad C = X \mid 2^{28}$$

Bit $27$ appears only in $B$ and bit $28$ only in $C$, so neither contributes, while every bit of $X$ appears in all three.

The choice of $27$ and $28$ is dictated by the bounds. Since $X \leq 10^8 < 2^{27}$, those two bits are guaranteed clear in $X$, so they genuinely act as distinct markers. And the largest value, $X \mid 2^{28} \leq 10^8 + 2.69 \times 10^8$, stays under the $10^9$ ceiling — whereas bit $29$ or $30$ would overflow it.

Distinctness is immediate: $A$ has neither marker bit, $B$ has one, $C$ the other.

Checking $X = 3$: the three numbers are $3$, $134217731$ and $268435459$, whose pairwise ORs all contain bits $0$ and $1$ and nothing else in common, giving $3$. **Any valid triple is accepted**, so this is judged by a checker rather than against the sample text.

## Edge cases

- **The expression is a bitwise majority.** Bit $b$ of $(A|B) \mathbin{\&} (B|C) \mathbin{\&} (C|A)$ is set exactly when at least two of $A, B, C$ have bit $b$ — because a bit held by only one of them is missing from the one OR that excludes it.
- **So every bit of $X$ goes into all three**, and the three are separated by marker bits that only one of them holds, which the majority then discards.
- **The markers must be clear in $X$.** Since $X \leq 10^8 < 2^{27}$, bits $27$ and $28$ are guaranteed free — picking a marker inside $X$'s range could collide and corrupt the result.
- **The bound $10^9$ is respected**: the largest output is $X \mid 2^{28} \leq 10^8 + 2.68 \times 10^8$, comfortably under.
- **Distinctness is automatic**, as the three differ in bits $27$ and $28$.
- **$X \geq 1$ is guaranteed**, so no all-zero degenerate case arises — though the construction would handle it.
- **This answer differs from the sample's** (`3 134217731 268435459` against `1 2 3`); the statement allows any valid triple, so a special judge evaluates the expression.

## Dry run

$X = 3 = 11_2$.

| bit | $A = X$ | $B = X \mid 2^{27}$ | $C = X \mid 2^{28}$ | how many have it | majority |
|---:|:---:|:---:|:---:|---:|:---:|
| 0 | 1 | 1 | 1 | 3 | **1** |
| 1 | 1 | 1 | 1 | 3 | **1** |
| 27 | 0 | 1 | 0 | 1 | 0 |
| 28 | 0 | 0 | 1 | 1 | 0 |

The majority is $11_2 = 3 = X$ ✓
