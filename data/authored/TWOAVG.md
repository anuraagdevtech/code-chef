---
topic: Binary Search
subtopic: Only K into A and 1 into B help; binary search the number of appends
time: $O(N + M + \log \text{answer})$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
To push $mean(A)$ above $mean(B)$, an append to $A$ should be as large as possible ($K$) and an append to $B$ as small as possible (1). If $K = 1$ all values are 1 and the means are always equal: answer $-1$. Otherwise appending enough $K$'s and 1's always works, so an answer exists.

Fix the total number of appends $z$ and let $x$ of them go to $A$. The condition, cross-multiplied to stay in integers, is

$$(S_A + K x)(M + z - x) > (S_B + z - x)(N + x).$$

The difference of the two sides is a quadratic in $x$ with leading coefficient $-(K - 1) < 0$, hence concave: its maximum over the integers of $[0, z]$ is attained at an endpoint or at one of the two integers around the vertex. Testing those four candidates decides whether $z$ appends suffice.

More appends never hurt, so feasibility is monotone in $z$: double an upper bound until it is feasible, then binary search for the smallest feasible $z$.

## Edge cases

- The means may already satisfy the inequality: answer 0.
- The inequality is strict; equality does not count.
- $K = 1$ is the only impossible case.
- Cross-multiplication avoids floating point entirely.

## Dry run

`A = [3, 7, 3, 5, 2, 4]` (sum 24), `B = [8, 3, 5]` (sum 16), `K = 9`.

- $z = 0$: $24 \cdot 3 = 72 > 16 \cdot 6 = 96$? No.
- $z = 1$: appending 9 to $A$ gives $33 \cdot 3 = 99$ against $16 \cdot 7 = 112$; appending 1 to $B$ gives $24 \cdot 4 = 96$ against $17 \cdot 6 = 102$. No.
- $z = 2$, $x = 1$: $33 \cdot 4 = 132 > 17 \cdot 7 = 119$. Yes.

Answer 2.
