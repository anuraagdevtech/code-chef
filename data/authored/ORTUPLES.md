---
topic: Combinatorics
subtopic: Independent bits with an eight-case table
time: $O(20)$ per test case
space: $O(1)$
---
OR acts on each bit separately, and the three constraints involve only ORs, so the $20$ bit positions are **completely independent**. The total is a product of per-bit counts, and each per-bit count is a tiny finite question: given the bits $p, q, r$ of $P, Q, R$, how many $(a,b,c) \in \{0,1\}^3$ satisfy $a \mathbin{|} b = p$, $b \mathbin{|} c = q$, $c \mathbin{|} a = r$?

Enumerating all eight patterns of $(p,q,r)$:

| $(p,q,r)$ | count |
|---|---|
| $(0,0,0)$ | 1 |
| $(0,1,1)$, $(1,0,1)$, $(1,1,0)$ | 1 |
| $(1,1,1)$ | 4 |
| $(0,0,1)$, $(0,1,0)$, $(1,0,0)$ | 0 |

The zero rows are the ones that matter. A single $1$ among $p, q, r$ is **contradictory**: if $p = q = 0$ then $a = b = c = 0$, forcing $r = 0$ too. So any bit where exactly one of the three has a one makes the whole answer $0$ — and since the counts multiply, one such bit is fatal.

The $(1,1,1)$ row gives $4$: all of $(0,1,1)$, $(1,0,1)$, $(1,1,0)$ and $(1,1,1)$ work, i.e. at most one of $a, b, c$ may be zero.

$$\text{answer} = \prod_{b=0}^{19} \mathrm{count}\bigl(P_b, Q_b, R_b\bigr)$$

The samples exercise each row. $P,Q,R = 10, 12, 14$ has one bit in the $(1,1,1)$ pattern (bit $3$) and the rest contributing factors of $1$, so the answer is $4$. $0, 5, 5$ has only $(0,0,0)$ and $(0,1,1)$ bits, so exactly one triple works. And $0, 0, 7$ has bits with $r = 1$ alone, so the answer is $0$.

## Edge cases

- **The bits are independent**, so the count is a product over the $20$ bit positions of a tiny per-bit count — enumerated once into an eight-entry table.
- **Three of the eight patterns are contradictory.** If exactly one of $P, Q, R$ has the bit, no assignment of $a, b, c$ can produce it: a bit present in one OR but absent from another forces the shared variable to $0$, which then makes the first OR impossible.
- **The all-ones pattern has four solutions** — $(a,b,c)$ equal to $(0,1,1)$, $(1,0,1)$, $(1,1,0)$ or $(1,1,1)$ — which is where all the counting happens.
- **The all-zeros pattern has exactly one**, with every variable clear.
- **A single contradictory bit zeroes the answer** (the third row, where $R$ has bits that $P$ and $Q$ lack), so the loop breaks out early.
- **The product can be as large as $4^{20} \approx 10^{12}$**, past 32-bit.
- **All three inputs are below $2^{20}$**, which matches the bound on $A, B, C$ — so no bit above position $19$ ever needs considering.

## Dry run

First sample: $P = 10$, $Q = 12$, $R = 14$ — binary $01010$, $01100$, $01110$.

| bit | $(P, Q, R)$ | solutions |
|---:|---|---:|
| 0 | $(0,0,0)$ | 1 |
| 1 | $(1,0,1)$ | 1 |
| 2 | $(0,1,1)$ | 1 |
| 3 | $(1,1,1)$ | **4** |
| 4+ | $(0,0,0)$ | 1 |

Product `4`. Bit $3$ is the only one where all three agree, and it alone admits the four choices.
