---
topic: Trees
subtopic: Level widths of perfect subtrees as constant-width segments with arithmetic-geometric sums
time: $O(N \log N + D \cdot B \log N + Q (\sqrt{N} + D))$ with $D = O(\sqrt{N})$ branching depths and $B$ distinct anchors queried
space: $O(N + D \cdot B)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
For a non-negative $x$ the maximum over permutations is reached by sorting the distances increasingly, so $W(x) = \sum_i d_i x^{i-1}$ with $d$ sorted. In a perfect subtree the sorted distances are simply the levels in order: level $t$ contributes the distance $t$ to $w_t$ consecutive powers, where $w_t$ is the width of that level.

In a perfect tree every vertex above the leaf level has a child, so widths never decrease, and they change only below vertices with two or more children. Since the widths sum to at most $N$, a subtree has $O(\sqrt{N})$ distinct widths. Group the levels into segments of constant width; inside a segment with width $w$ the contribution is $\sum_t t \cdot y^{\text{offset} + w t} \cdot (y^w - 1)/(y - 1)$, an arithmetic-geometric series with ratio $y^w$ that has a closed form.

To find the segments of a subtree quickly, for every depth keep the branching vertices one level above it sorted by Euler-tour entry time, with prefix sums of (children $-$ 1). The width gain at a depth for the subtree of $v$ is then a range sum over the Euler interval of $v$. A vertex on a chain of single children has the same segments as the first branching vertex below it (its *anchor*), shifted by the chain length, so segment lists are cached per anchor.

The queries are online (xor-ed with the previous answer). $y = 1$ is handled by plain sums of distances; the geometric sum is evaluated by doubling so that $y^w = 1$ needs no division, and when a query spans many segments the powers of $y$ come from baby-step/giant-step tables.

## Edge cases

- $y = 1$ makes the closed form divide by zero; the answer is the sum of all distances.
- $y^w \equiv 1$ for some width must not be divided by either, hence the division-free geometric sum.
- A query vertex inside a unary chain shifts every distance of its anchor's list by the chain length.
- The decoded vertex and $y$ depend on the previous answer, so queries cannot be reordered.

## Dry run

Tree with edges `1-2, 1-3, 2-4, 2-5, 3-6`, query vertex 1 with $y = 1$.

Level widths are 1, 2, 3 at distances 0, 1, 2, and all three widths differ, so there are three segments of one level each. With $y = 1$ the value is the plain sum of distances: $0 \cdot 1 + 1 \cdot 2 + 2 \cdot 3 = 8$.

The next query is decoded with 8: the pair `10 10` becomes vertex $10 \oplus 8 = 2$ and $y = 2$. Its subtree has distances `0 1 1`, so $W = 0 + 1 \cdot 2 + 1 \cdot 4 = 6$.
