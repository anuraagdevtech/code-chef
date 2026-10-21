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
