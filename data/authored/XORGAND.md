---
topic: Prefix Sums
subtopic: The comparison reduces to equal bit lengths
time: $O(N + Q)$ per test case
space: $O(N)$
---
Compare $M \oplus X$ with $M \mathbin{\&} X$ at the **highest bit either number has**, position $h = \mathrm{bitlen}(M \mathbin{|} X) - 1$. At any bit, the two results differ only in two situations: when exactly one of $M, X$ has the bit (XOR gets $1$, AND gets $0$) and when both have it (XOR gets $0$, AND gets $1$). Above $h$ both are zero, so bit $h$ decides everything:

- both $M$ and $X$ carry bit $h$: the AND wins, so $M$ is **not** mystical;
- exactly one carries it: the XOR wins, so $M$ **is** mystical.

Both carry the top bit of $M \mathbin{|} X$ exactly when $M$ and $X$ have the **same bit length** (and are non-zero). So the whole condition is

$$M \text{ is mystical} \iff \mathrm{bitlen}(M) \neq \mathrm{bitlen}(X)$$

with $M = X = 0$ correctly excluded, since then both sides are $0$ and the inequality is strict.

So each query is a counting problem over at most $32$ classes: precompute, for each bit length, a prefix count over the array, and answer with

$$(R - L + 1) \;-\; \#\{\,i \in [L,R] : \mathrm{bitlen}(A_i) = \mathrm{bitlen}(X)\,\}$$

in $O(1)$. That turns what looks like a per-element bitwise test into one subtraction — essential with $\sum N$ and $\sum Q$ both at $2 \times 10^5$.

With $A = [1,2,3,4,5]$ the bit lengths are $1,2,2,3,3$. The query $(1,5,4)$ has $\mathrm{bitlen}(4) = 3$, so the two matching elements are excluded and the answer is $5 - 2 = 3$. The query $(2,5,2)$ has $\mathrm{bitlen}(2) = 2$, excluding $2$ and $3$, giving $4 - 2 = 2$.
