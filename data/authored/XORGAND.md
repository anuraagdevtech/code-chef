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

## Edge cases

- **$(M \oplus X) > (M \mathbin{\&} X)$ holds exactly when $M$ and $X$ have different bit lengths.** If they share a top bit, that bit is set in the AND and cleared in the XOR, so the AND wins outright; if one is strictly wider, its top bit appears in the XOR and in neither the AND nor anything above, so the XOR wins.
- **That reduces each query to a count by bit length**, which a prefix table answers in constant time — no per-query scan of the range.
- **$M = X$ is never mystical**, since equal values share a bit length (and the XOR is $0$).
- **$M = 0$ is mystical against any $X \geq 1$**, because a bit length of $0$ differs from everything positive; and $0$ against $0$ is not.
- **The answer is the complement**: the range size minus the count sharing $X$'s bit length, which is cheaper than summing over the $32$ other widths.
- **$A_i, X < 2^{31}$** so bit lengths run $0 \dots 31$, and the table is sized $33$ rows to index them all safely.
- **Sum of $N$ and $Q$ each up to $2 \cdot 10^5$**, so the $33 \times N$ table is built once per case.

## Dry run

Sample: $A = 1, 2, 3, 4, 5$ with bit lengths $1, 2, 2, 3, 3$.

| query | $X$ | $X$'s bit length | matches in range | range size | answer |
|---|---:|---:|---:|---:|---:|
| $1\ 5$ | 4 | 3 | $4, 5$ → 2 | 5 | `3` |
| $2\ 5$ | 2 | 2 | $2, 3$ → 2 | 4 | `2` |

Checking one: $M = 1$, $X = 4$ gives $1 \oplus 4 = 5 > 1 \mathbin{\&} 4 = 0$ ✓, and the bit lengths $1$ and $3$ do differ.
