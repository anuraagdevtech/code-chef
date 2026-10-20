---
topic: Bit Manipulation
subtopic: The highest differing bit decides an XOR comparison
time: $O(1)$ per test case
space: $O(1)$
---
XOR-ing a common $X$ into two numbers preserves which bits differ between them, so the comparison $(A \oplus X) < (B \oplus X)$ is decided entirely at the **highest bit where $A$ and $B$ differ**. Call it $p$; the bits above $p$ are identical and cancel, and the bits below are irrelevant once bit $p$ separates them.

At that bit, we need $A \oplus X$ to hold $0$ and $B \oplus X$ to hold $1$, which pins down one bit of $X$:

$$X_p = A_p$$

(and equivalently $X_p = 1 - B_p$, consistent because $A_p \neq B_p$).

So each of the two required inequalities fixes exactly one bit of $X$:

- $A < B$ fixes bit $p = \text{msb}(A \oplus B)$ to $A_p$
- $B < C$ fixes bit $q = \text{msb}(B \oplus C)$ to $B_q$

If $p \neq q$ the two constraints are independent, so set those bits and leave the rest at $0$. If $p = q$ they collide: the first demands $X_p = A_p$ and the second $X_p = B_p$, and since $A_p \neq B_p$ at their highest differing bit, no $X$ can satisfy both — the answer is $-1$.

In Python, $\text{msb}(z)$ is `z.bit_length() - 1`, and the inputs are distinct so neither XOR is zero.

Sample case 2, $(3,1,2)$, is the conflict: $3 \oplus 1 = 2$ and $1 \oplus 2 = 3$ both have their top bit at position $1$, and $3$ has a $1$ there while $1$ has a $0$ — irreconcilable, so $-1$.

**Any valid $X$ is accepted**, so this is judged by a checker. Sample case 1 publishes $4$ while this construction yields $0$; both order $1, 2, 3$ correctly, so a verbatim diff would report a false mismatch.
