---
topic: Greedy
subtopic: Mirror differences, removed in signed layers
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Let $d_i = A_i - A_{N+1-i}$ for the positions $i$ of the left half; the array is a palindrome when all $d_i$ are 0.

Adding 1 on a range that lies in the right half lowers $d$ by 1 on a contiguous range of mirrored indices, and a range in the left half raises $d$ by 1 on a contiguous range. A range that crosses the centre changes both members of the innermost pairs equally, so those cancel and the net effect is again $\pm 1$ on a contiguous range of $d$. Hence the task is: bring $d$ to zero with the fewest operations of the form "add $+1$ or $-1$ to a contiguous range".

Positive and negative parts must be handled by different kinds of operations, and inside a part of constant sign the classical layer argument applies: scanning from left to right, a new operation has to start whenever the magnitude rises above the previous one, so position $i$ costs $\max(0, |d_i| - |d_{i-1}|)$; when the sign changes, all $|d_i|$ layers are new.

## Edge cases

- Already a palindrome: 0.
- For odd $N$ the middle element has no partner and is ignored.
- A sign change between neighbours cannot share any operation.
- The count can be as large as $10^9$ per pair.

## Dry run

`A = [2, 6, 4, 3, 4, 1]`: $d = (2 - 1,\; 6 - 4,\; 4 - 3) = (1, 2, 1)$.

- $d_1 = 1$: one new layer (cost 1).
- $d_2 = 2$: one more layer than before (cost 1).
- $d_3 = 1$: fewer layers, nothing new.

Answer 2: one range covers all three pairs, a second covers only the middle pair.
