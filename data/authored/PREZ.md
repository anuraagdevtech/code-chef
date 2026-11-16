---
topic: Greedy
subtopic: Maintain the exact cost of zeroing each prefix
time: $O(N)$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
For a prefix ending with digit $d$, let $r=(-d)\bmod10$ be its required number of increments modulo ten. Reading right to left, consecutive required residues determine the least nonnegative number of operations ending at each boundary.

When extending a prefix, replace its old last-position cost `previous` by the new last-position cost `required`, and add `(previous-required) % 10` for the new internal boundary. This updates the exact minimum cost in constant time. Prefix feasibility is monotone, since making a longer prefix zero also makes every shorter prefix zero.

## Edge cases

- Zero digits may still need operations if later digits change them.
- Costs can exceed ten because operations end at different boundaries.
- With $K=0$, only an already-zero prefix is feasible.

## Dry run

For `380`, required residues are `7,2,0`. Prefix costs are `7`, `7-7+2+5=7`, and `7-2+0+2=7`. Budget 5 reaches none; budget 9 reaches all three.
