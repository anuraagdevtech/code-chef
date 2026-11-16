---
topic: Dynamic Programming
subtopic: Keep a subtree optimally or remove it for one penalty
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Let $dp[u]$ be the best profit obtainable from the subtree at $u$. Removing the entire subtree yields $-X$. Keeping $u$ yields $A_u+\sum dp[v]$ over its children, because their choices are independent.

Take the larger of those alternatives. Build a parent-first traversal iteratively and evaluate its reverse order so every child is complete before its parent.

## Edge cases

- Removing the root is allowed and yields $-X$.
- A removed subtree incurs one penalty, regardless of its size.
- The optimal profit can be negative.

## Dry run

For chain values `[1,-5,-10]` and penalty 5, the leaf chooses removal, giving `-5`; its parent also chooses removal, giving `-5`; the root keeps itself and that choice, giving `1-5=-4`.
