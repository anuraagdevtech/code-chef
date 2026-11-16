---
topic: Greedy
subtopic: Colours present in B form free pools; pick the smallest usable value greedily
time: $O(N \log N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
If a colour occurs somewhere in $B$, then all elements of that colour in both arrays can be rearranged arbitrarily among the positions they occupy: any element of $A$ can be exchanged with the $B$ element, and that $B$ element works as a spare slot for further exchanges. If a colour does not occur in $B$, its elements in $A$ cannot be swapped at all and stay where they are.

So each position of $A$ either holds a fixed value, or may receive any still unused value from the pool of its colour (the pool being all $A$ and $B$ values of that colour). We need the resulting sequence to be non-decreasing.

Go through $A$ from left to right, remembering the previous value. At a fixed position, fail if its value is smaller than the previous one. At a free position, take the smallest unused pool value that is at least the previous value - a smaller choice keeps the running value as low as possible and saves the larger pool values for later, so it can never hurt. Pools are sorted once and each keeps a pointer, with a binary search to jump to the first usable value.

## Edge cases

- Elements of $B$ never need to be sorted; they only serve as a reservoir.
- A colour that occurs in $A$ only is frozen even if it occurs many times.
- Pool values skipped because they are too small are never needed again, since the required minimum only grows.
- Colours go up to $2N$ and are used as dictionary keys.

## Dry run

Third sample: `A = [2, 1]` with colours `[2, 1]`, `B = [2, 1]` with colours `[2, 1]`.

Pools: colour 2 holds `{2, 2}`, colour 1 holds `{1, 1}`.

- Position 1 (colour 2): the smallest pool value is 2. Previous becomes 2.
- Position 2 (colour 1): it needs a value $\ge 2$, but its pool only has ones.

Answer No.
