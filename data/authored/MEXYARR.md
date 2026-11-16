---
topic: Greedy
subtopic: Reserve constrained values until their last use and always insert the smallest allowed value
time: $O(N \log N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
If $B_i = v$, the value $v$ must not occur among the first $i$ elements. So a value that appears as a constraint is *reserved* up to the last index at which it is required; before that it may not be placed at all.

Among the values that may be placed, inserting the smallest one is always best: it pushes the mex up as fast as possible, and a prefix mex can never go down, so being as far ahead as the reservations allow never hurts - reserved values act as hard ceilings that keep the mex from overshooting a pending constraint.

So keep a min-heap of the currently allowed values, initially all values in $[0, N]$ that are never required. At each position pop the smallest, append it, advance the running mex, and compare it with $B_i$ if that is not $-1$. If position $i$ is the last occurrence of $B_i$, release that value into the heap. Any mismatch means no valid array exists.

## Edge cases

- $B_1$ can only be 0 or 1 (or $-1$).
- A required mex larger than the position index is impossible and shows up as a mismatch.
- Requirements that decrease from left to right are impossible, because the mex never decreases.
- Any valid array is accepted, so the output is checked rather than compared.

## Dry run

`B = [0, -1, 2, -1, 5, -1, -1]`. Reserved: 0 (until index 1), 2 (until index 3), 5 (until index 5). Allowed at the start: `1 3 4 6 7`.

| index | insert | mex | required | released |
|---:|---:|---:|---:|---|
| 1 | 1 | 0 | 0 | 0 |
| 2 | 0 | 2 | - | |
| 3 | 3 | 2 | 2 | 2 |
| 4 | 2 | 4 | - | |
| 5 | 4 | 5 | 5 | 5 |
| 6 | 5 | 6 | - | |
| 7 | 6 | 7 | - | |

Output `1 0 3 2 4 5 6`.
