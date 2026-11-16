---
topic: Stacks
subtopic: Nearest strictly smaller element to the right with a monotonic stack
time: $O(N)$
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Each chef delegates to the nearest chef ahead of him (larger index) with strictly smaller seniority; if that chef is at index $i_2$ the contribution is $i_2 - i_1 + 1$, and a chef with no junior ahead contributes 1. The answer is the product of all contributions modulo $10^9 + 7$.

"Nearest strictly smaller to the right" is the textbook monotonic-stack query. Scan from the front of the queue (index $N$) to the back, keeping a stack of indices whose values are strictly increasing from bottom to top. For the current chef pop everything that is not smaller than him; the top of the stack, if any, is his junior.

## Edge cases

- Equal seniority is not junior, so equal values are popped (`>=`).
- Chefs with no junior ahead multiply the product by 1.
- The value $K$ in the input is not needed.
- Take the product modulo $10^9 + 7$ as it grows.

## Dry run

`A = [1, 2, 1, 2]`, scanning from the right.

| index | value | stack before (values) | junior | factor |
|---:|---:|---|---|---:|
| 4 | 2 | - | none | 1 |
| 3 | 1 | 2 | none (2 is popped) | 1 |
| 2 | 2 | 1 | index 3 | $3 - 2 + 1 = 2$ |
| 1 | 1 | 1, 2 | none (both popped) | 1 |

Answer 2.
