---
topic: Sets
subtopic: One-pass tally of mirrored keys
time: $O(N)$ per test case
space: $O(N)$
---
The two equalities $A_i = B_j$ and $A_j = B_i$ say exactly that the ordered pair at $i$ is the **reverse** of the ordered pair at $j$:

$$(A_i, B_i) = (B_j, A_j)$$

So index $i$ carries a key $(A_i, B_i)$ and asks for partners whose key is its mirror image. That reduces the problem to counting mirrored key collisions, with no need to compare values pairwise.

Sweeping $j$ left to right and keeping a tally of the keys seen so far handles the $i < j$ requirement for free: when $j$ arrives, look up $(B_j, A_j)$ in the tally and add its count, then insert $j$'s own key. Every good pair is counted exactly once, at its larger index.

$$\text{answer} = \sum_{j} \#\{\,i < j : (A_i, B_i) = (B_j, A_j)\,\}$$

The self-mirrored case is worth noting: when $A_i = B_i$ the key is its own mirror, so such indices pair with each other. Sample 3, with $A = B = [10,10,10]$, is entirely of this kind and yields $\binom{3}{2} = 3$ — the sweep produces $0 + 1 + 2$, which is the same thing.

Sample 4, $A = [4,8,1,1]$ and $B = [8,4,1,1]$, mixes both kinds: the pair $(1,2)$ is a genuine mirror $(4,8) \leftrightarrow (8,4)$, and the pair $(3,4)$ is self-mirrored, giving $2$. Sample 2 has no collisions at all.

Values reach $10^9$, so the keys must be hashed rather than used as array indices — a `Counter` over tuples is the natural fit, and $\sum N \leq 2 \times 10^5$ keeps it cheap.
