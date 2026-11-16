---
topic: Combinatorics
subtopic: Index parity classes must be uniform in value parity
time: $O(N)$ per test case
space: $O(\max N)$ for factorials
complexity_note: Auxiliary space excludes the buffered input and output.
---
A pair of positions with odd $i + j$ consists of one odd position and one even position, and every such pair is constrained. So the condition says: for every odd position $i$ and every even position $j$, $A_i + A_j \equiv K \pmod 2$.

- $K = 0$: every odd-position value has the same parity as every even-position value. For $N \ge 2$ both classes are non-empty, so all values must share one parity; then every permutation works: $N!$, otherwise 0.
- $K = 1$: all odd positions hold one parity and all even positions the other. There are $\lceil N/2 \rceil$ odd positions and $\lfloor N/2 \rfloor$ even ones. If the number of odd values $o$ equals $\lceil N/2 \rceil$ the odd values can fill the odd positions, in $o! \cdot (N - o)!$ ways; if $o = \lfloor N/2 \rfloor$ they can fill the even positions, again $o! \cdot (N - o)!$ ways. For even $N$ with $o = N/2$ both placements exist and the count doubles.

For $N = 1$ there is no pair and the single permutation counts.

## Edge cases

- $N = 1$: answer 1 regardless of $K$.
- The values are distinct, so permutations of the array are counted without any division.
- Even $N$ with exactly half odd values gives the factor 2 for $K = 1$.
- Only parities of the values are used.

## Dry run

`N = 3, K = 1, A = [1, 2, 3]`: two odd values, and there are $\lceil 3/2 \rceil = 2$ odd positions.

The odd values go to positions 1 and 3 ($2!$ ways) and the even value to position 2 ($1!$): answer 2 - `[1, 2, 3]` and `[3, 2, 1]`.

`N = 4, K = 0, A = [17, 13, 21, 3]`: all odd, so all $4! = 24$ permutations work.
