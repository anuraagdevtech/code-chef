---
topic: Number Theory
subtopic: Enumerate periodic row-major positions and test column-major divisibility
time: $O(S\log S)$ per test case for $S=NM$
space: $O(S)$ for the output
complexity_note: Auxiliary space excludes the buffered input and output.
---
For step $d=K+1$, each hero destroys indices $0,d,2d,\ldots$ in its own ordering, giving $\lfloor(S-1)/d\rfloor+1$ destroyed cells. Use inclusion-exclusion to subtract their overlap.

For each row-major destroyed index $x$, its row and column are `divmod(x,M)`, so its column-major index is `column*N+row`. The second hero destroys it exactly when that index is divisible by $d$. Enumerating only the first hero's destroyed indices costs $\sum_{d=1}^S O(S/d)=O(S\log S)$ across all answers.

## Edge cases

- Both heroes always destroy the top-left cell.
- $K=0$ destroys the whole grid.
- $K=S-1$ destroys only the first cell.
- A cell destroyed twice counts once.

## Dry run

For a two-by-three grid and `K=1`, step two gives three destroyed cells per hero. Their overlap has two cells, so the union size is `3+3-2=4`.
