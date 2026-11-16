---
topic: Dynamic Programming
subtopic: Longest chain of boundaries whose prefix value rises by exactly one
time: $O(N)$ expected per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Replace ones by $+1$ and zeros by $-1$ and let $h_x$ be the prefix sum just before position $x$ ($h_1 = 0$, defined for $x = 1 \dots N + 1$). The subarray $B[x_i : x_j - 1]$ has (ones $-$ zeros) $= h_{x_j} - h_{x_i}$.

The condition for all pairs is therefore $h_{x_j} - h_{x_i} = j - i$, which holds for all pairs as soon as it holds for consecutive ones: a good sequence is a chain of boundaries, increasing in position, whose heights go up by exactly 1 at each step.

Scan the boundaries from left to right. Let `best_at[v]` be the longest chain found so far that ends at a boundary of height $v$, together with that boundary. A chain ending at the current boundary of height $s$ extends the best chain ending at height $s - 1$, so its length is `best_at[s - 1] + 1`; store it if it improves `best_at[s]`, and remember the predecessor to rebuild the chain. The longest chain overall is the answer; its boundaries are printed in increasing order.

## Edge cases

- A single boundary is always a good sequence, so the answer is at least 1.
- All ones: every boundary is used, length $N + 1$.
- Heights can be negative, so a dictionary is used.
- Several longest chains may exist, so the output is validated by a checker.

## Dry run

`A = [0, 1, 1, 0, 1, 1]`. Heights at boundaries 1-7: `0 -1 0 1 0 1 2`.

Chain lengths: boundary 1 (height 0): 1. Boundary 2 (height $-1$): 1. Boundary 3 (height 0): extends boundary 2, length 2. Boundary 4 (height 1): 3. Boundary 5 (height 0): 2. Boundary 6 (height 1): 3. Boundary 7 (height 2): 4.

One longest chain is `2 3 4 7` with heights $-1, 0, 1, 2$; the sample's `2 5 6 7` is another.
