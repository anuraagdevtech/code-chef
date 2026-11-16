---
topic: Combinatorics
subtopic: No carries - distribute the set bits of N among three non-empty owners
time: $O(\log N)$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
For non-negative integers, $X + Y + Z \ge X \mid Y \mid Z$, with equality exactly when no bit is set in more than one of the three numbers. Both expressions must equal $N$, so the three numbers have pairwise disjoint bits and together use exactly the set bits of $N$.

So a triple is an assignment of each of the $p = \text{popcount}(N)$ set bits to one of $X, Y, Z$: $3^p$ assignments. All three numbers must be positive, i.e. each must receive at least one bit; by inclusion-exclusion the number of surjective assignments is

$$3^p - 3 \cdot 2^p + 3.$$

The upper bounds $X, Y, Z < N$ follow automatically once all three are positive.

## Edge cases

- Fewer than three set bits: the formula gives 0 for $p = 1$ and $p = 2$.
- The triples are ordered, which the assignment count respects.
- The subtraction must be reduced to a non-negative residue modulo $10^9 + 7$.
- $N < 2^{60}$, so the popcount is at most 60.

## Dry run

`N = 7 = 111_2`, $p = 3$: $27 - 24 + 3 = 6$ - the six orderings of $(1, 2, 4)$.

`N = 3 = 11_2`, $p = 2$: $9 - 12 + 3 = 0$.
