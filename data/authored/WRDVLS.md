---
topic: Combinatorics
subtopic: For each value, count subarrays containing exactly that many occurrences
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Group the contributions by value. The indices holding a value $x$ are counted in $w(L, R)$ exactly when the subarray contains exactly $x$ occurrences of $x$, and then all $x$ of them are counted. So the answer is

$$\sum_x x \cdot \#\{\text{subarrays with exactly } x \text{ occurrences of } x\}.$$

For a value $x$ with occurrence positions $p_1 < p_2 < \dots < p_m$ (and sentinels $p_0 = 0$, $p_{m+1} = N + 1$), a subarray contains exactly the occurrences $p_j, \dots, p_{j+x-1}$ when its left end lies in $(p_{j-1}, p_j]$ and its right end in $[p_{j+x-1}, p_{j+x})$. The two choices are independent, giving $(p_j - p_{j-1}) \cdot (p_{j+x} - p_{j+x-1})$ subarrays.

Slide this window of $x$ consecutive occurrences over the list. Values with fewer than $x$ occurrences are skipped, and the total work is the total number of occurrences.

## Edge cases

- A value larger than its number of occurrences never contributes.
- The value 1 contributes for every subarray that contains it exactly once.
- The total is far larger than 32 bits for big inputs.
- Sentinels at both ends make the boundary windows uniform.

## Dry run

`A = [1, 2, 1, 2]` (positions 1-4).

- $x = 1$ at positions 1, 3: window `{1}`: $(1 - 0)(3 - 1) = 2$; window `{3}`: $(3 - 1)(5 - 3) = 4$. Contribution $1 \cdot 6 = 6$.
- $x = 2$ at positions 2, 4: one window `{2, 4}`: $(2 - 0)(5 - 4) = 2$. Contribution $2 \cdot 2 = 4$.

Answer 10.
