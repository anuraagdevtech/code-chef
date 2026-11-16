---
topic: Constructive
subtopic: Blocks with a computable contribution, separated by ones
time: $O(D / 99998 + 1)$ per test case
space: $O(D / 99998 + 1)$ for the output
complexity_note: Auxiliary space excludes the buffered input and output.
---
Three observations make the sum easy to control.

- A subarray of equal values has min = gcd and contributes 0.
- A subarray containing a 1 has min = gcd = 1 and contributes 0. So a 1 between two blocks makes them independent.
- Take $k$ copies of $a$ followed by a single $a + 1$. Subarrays inside the copies contribute 0, the single $a + 1$ contributes 0, and each of the $k$ subarrays that end at the last element and include at least one $a$ has minimum $a$ and gcd 1 (consecutive integers are coprime), contributing $a - 1$. The block is worth $k (a - 1)$.

Write $D = 99998 \cdot q + r$ with $0 \le r < 99998$. A block of $q$ copies of 99999 followed by 100000 is worth $99998 \cdot q$, and the two-element block $r + 1, r + 2$ is worth $r$. Put a 1 between them when both are present; for $D = 0$ print the single element 1. The length is about $D / 99998 + 4$, far below the limit.

## Edge cases

- $D = 0$: the array `1`.
- $r = 0$ or $q = 0$: only one of the two blocks is printed, without a separator.
- All values stay within $[1, 10^5]$: the largest are 99999 and 100000.
- Many arrays are valid, so the output is validated by a checker.

## Dry run

`D = 200`: $q = 0$, $r = 200$. Output the block `201 202`: its only non-trivial subarray has min 201 and gcd 1, contributing 200.

`D = 199996 + 5 = 200001`: $q = 2$, $r = 5$. Output `99999 99999 100000 1 6 7`: the first block gives $2 \cdot 99998$, the last gives 5, and everything touching the 1 gives 0.
