---
topic: Disjoint Set Union
subtopic: Interleave the components, then permute equal strengths inside each
time: $O((N + M)\,\alpha(N))$ per test case after factorial precomputation
space: $O(N + M)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Friendship is transitive, so the people fall into groups of friends - the connected components of the friendship graph, found with a disjoint-set union. Within one group the order is dictated by strength, while different groups do not constrain each other.

Count the sequences in two stages.

- Choose which positions of the sequence belong to which group: a multinomial coefficient $N! / \prod_g (\text{size}_g)!$.
- Inside a group the members appear in the order of their strengths, which fixes everything except the relative order of members with equal strength; each set of $z$ members sharing a group and a strength can be arranged in $z!$ ways.

The answer is the product of these factors modulo $10^9 + 7$. A Counter over (component root, strength) gives the sizes of the equal-strength sets.

## Edge cases

- No friendships: every person is a separate group and all $N!$ orders are counted.
- One group with distinct strengths: exactly one sequence.
- Equal strengths in different groups do not interact.
- Factorials are precomputed once up to the maximum $N$.

## Dry run

Second sample: friendships `2-3` and `4-5`, strengths `6 4 4 3 1`.

Groups: `{1}`, `{2, 3}`, `{4, 5}`. Interleavings: $5! / (1! \, 2! \, 2!) = 30$.

In `{2, 3}` both strengths are 4, so the two can swap: factor $2!$. In `{4, 5}` the strengths differ: factor 1.

Answer $30 \cdot 2 = 60$.
