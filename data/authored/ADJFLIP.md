---
topic: Constructive
subtopic: Ones on even positions minus ones on odd positions never changes
time: $O(N)$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
An operation flips two equal neighbours, one on an even index and one on an odd index. `00 -> 11` adds a one on each parity and `11 -> 00` removes one from each, so

$$D = \#\{\text{ones on even indices}\} - \#\{\text{ones on odd indices}\}$$

is invariant.

It is also the only invariant. Complement every character on an odd index: an equal pair `00` or `11` becomes an unequal pair `01` or `10`, and flipping both characters of the original pair turns into swapping the two characters of the transformed pair. So in the transformed string the allowed moves are exactly "swap two adjacent different characters", which can rearrange the string arbitrarily while keeping its number of ones - and that number is $D$ plus a constant.

So the string can be made constant exactly when $D$ equals the value of $D$ for one of the two constant strings: 0 for all zeros; for all ones, 0 if $N$ is even and 1 if $N$ is odd (0-based indices).

## Edge cases

- Already constant strings answer Yes.
- $N = 1$: always Yes.
- For even $N$ both targets require $D = 0$.
- A perfectly alternating string has no legal move at all, and its $D$ is far from the targets unless it is very short.

## Dry run

`S = 110110` (indices 0-5): ones on even indices 0 and 4, ones on odd indices 1 and 3, so $D = 0$ - Yes.

`S = 0101010`: all three ones are on odd indices, $D = -3$; the targets are 0 and 1 - No.
