---
topic: Dynamic Programming
subtopic: Merge DP where appending a zero costs the ones already placed
time: $O(N^2)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
An inversion is a `1` placed before a `0`. Build the merged string left to right; the state is how many characters have been taken from each string, $(i, j)$. The number of ones already placed is then known - ones among the first $i$ characters of $A$ plus ones among the first $j$ of $B$ - regardless of the order in which they were merged.

Appending a `1` creates no new inversion. Appending a `0` creates one inversion with every `1` already placed. So

$$\text{cost}(i, j) = \min\bigl(\text{cost}(i-1, j) + w_A,\; \text{cost}(i, j-1) + w_B\bigr),$$

where $w_A$ is the number of ones in the state $(i, j)$ if $A_i$ is `0` (else 0), and similarly for $w_B$; the appended character is a zero, so counting ones "including" it changes nothing. A prefix count of ones in $B$ and a running count for $A$ give the weights in $O(1)$. Only one row of the table is kept.

## Edge cases

- Inversions inside $A$ and inside $B$ are unavoidable and are included automatically.
- If one string is all zeros it should simply go first, which the DP finds.
- The answer can reach about $N^2$.
- The first row and the first column are the costs of taking characters from one string only.

## Dry run

`A = 00001`, `B = 11110`.

Take the four zeros of $A$ first: no ones are placed yet, cost 0. The final `0` of $B$ has to come after the four ones of $B$, so it costs at least 4; placing the `1` of $A$ after it avoids a fifth inversion.

Merged string `0000 1111 0 1`: answer 4.
