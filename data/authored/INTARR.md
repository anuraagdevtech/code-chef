---
topic: Constructive
subtopic: Zigzag from the sorted halves, tried in both orientations
time: $O(N \log N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
No three consecutive elements may be monotone, even weakly, so the array must strictly alternate: every inner element is a strict peak or a strict valley.

Sort the values and split them into a lower and an upper half. Putting the lower half on one parity of positions and the upper half on the other gives the alternation as long as each low element is strictly below both of its neighbours. Writing both halves in the same (descending) order pairs the $k$-th largest low with the $k$-th and $(k+1)$-th largest highs, which keeps equal values as far apart as possible.

Two orientations exist - valleys on the even indices, or peaks on the even indices - and for odd $N$ they use differently sized halves. Build the first, verify it directly, and if it fails build and verify the second. If both fail, print $-1$.

## Edge cases

- $N \le 2$: any order is interesting.
- A value occurring more than about half of the time makes the task impossible (for example `2 2 2`).
- For odd $N$ the extra element goes to the even indices, so the two orientations really differ.
- Any valid arrangement is accepted.

## Dry run

`A = [2, 6, 5, 2]`, sorted `2 2 5 6`.

Lower half `2 2`, upper half `5 6`, both reversed: even indices get `2 2`, odd indices get `6 5`.

Arrangement `2 6 2 5`: 6 is a peak and the second 2 is a valley, so it is valid.
