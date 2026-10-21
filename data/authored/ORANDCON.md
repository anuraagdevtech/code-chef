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
