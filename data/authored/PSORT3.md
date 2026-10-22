---
topic: Sorting
subtopic: Mixed-direction composite key
time: $O(N \log N)$
space: $O(N)$
---
Two sort levels pointing in **opposite directions**: the second element descending, and ties broken by the first element ascending.

Python sorts tuples ascending throughout, so the descending field is handled by negating it:

$$\text{key} = (-B_i,\ A_i)$$

Negation is clean here because the values are integers; for a non-numeric field the alternative is `sorted(..., reverse=True)` on one pass followed by a stable sort on the other, which is more error-prone.

The sample is built to expose a wrong tie-break. Pairs $(2,6), (2,3), (3,3)$ sort to $(2,6)$ first on the descending $B$, then the two with $B = 3$ are ordered by **ascending** $A$, giving $(2,3)$ before $(3,3)$. A uniform `reverse=True` would wrongly place $(3,3)$ first.

Output is a single flat line of $2N$ integers — each pair printed as its first element then its second, with no separators beyond spaces. Flattening with a generator and one `" ".join` avoids building the string incrementally.

Values reach $10^{18}$, which is inside unsigned 64-bit but at the edge of signed — worth noting that negating such a value for the sort key is safe in Python but would need care in a fixed-width language, where a comparator function is the better route.

With $N$ up to $10^5$ the sort dominates; bulk I/O matters more than the comparison itself.

## Edge cases

- **The two keys pull in opposite directions**, so the sort key negates the second component and leaves the first positive: descending by $B_i$, ascending by $A_i$ on ties.
- **Negation is safe here** because the values are positive integers — on an unbounded or floating type a reverse comparator would be the sturdier choice.
- **The tie-break is genuinely exercised** by the sample: two pairs share $B_i = 3$ and are ordered by their first components, $2$ before $3$.
- **The pairs come from two separate arrays**, zipped by index — not read as interleaved pairs.
- **The output is one flat line** of $2N$ numbers, each pair's components adjacent.
- **$A_i, B_i$ up to $10^{18}$**, so the keys stay exact in Python where a float key would lose precision.
- **There is no test-case count**: the input is $N$, then array $A$, then array $B$.

## Dry run

Sample: $A = 2, 2, 3$ and $B = 6, 3, 3$.

| pair | sort key $(-B_i,\, A_i)$ |
|---|---|
| $(2, 6)$ | $(-6, 2)$ |
| $(2, 3)$ | $(-3, 2)$ |
| $(3, 3)$ | $(-3, 3)$ |

Sorted: $(2,6)$, then $(2,3)$ before $(3,3)$ on the tie. Output `2 6 2 3 3 3`.
