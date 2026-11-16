---
topic: Arrays
subtopic: All rotations answered at once with a sliding-window maximum over runs
time: $O(N + Q)$
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
A right shift only moves the starting point of a circular array, so there are just $N$ different arrays. Double the array; the array after $s$ shifts is the window of length $N$ starting at position $(-s) \bmod N$. Precompute the longest run of ones for every window and answer each `?` with a lookup, capped at $K$.

For every position store the length of the run of ones ending there. Inside a window, the longest run is the maximum of these values, except that a run reaching back past the left edge of the window has to be clipped to the part inside. Keep a deque of (position, run length) with decreasing lengths, as in the sliding-window maximum. Run lengths ending later inside the same run are larger, so only the front entry can be clipped; while its clipped value is no better than the next entry, drop it.

## Edge cases

- The answer is capped at $K$, and also at $N$ when the array is all ones (the clipping takes care of that).
- An all-zero array answers 0.
- Shifts are counted modulo $N$, so a long string of `!` costs nothing extra.
- The query string is read as bytes: 33 is `!`.

## Dry run

`A = [1, 1, 0, 1, 1]`, `K = 3`, queries `?!?!?`.

Doubled array `1 1 0 1 1 1 1 0 1 1`; longest run inside each window of length 5 by start: start 0 gives 2, start 4 gives 3 (`1 1 1 0 1`), start 3 gives 4 (`1 1 1 1 0`).

- `?` with 0 shifts: start 0, answer $\min(3, 2) = 2$.
- after one `!`: start 4, answer 3.
- after two: start 3, answer $\min(3, 4) = 3$.
