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
