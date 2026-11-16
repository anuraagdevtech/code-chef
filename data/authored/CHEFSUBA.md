---
topic: Arrays
subtopic: Window sums on the doubled array, then a sliding maximum per rotation
time: $O(N + P)$
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
A shift just moves the start of a circular array. Double the array; after $s$ right shifts the current array is the length-$N$ window starting at $(-s) \bmod N$.

The values are 0 or 1, so the best frame always uses the full width $K$ (capped at $N$). Let `frame_sum[i]` be the number of ones in positions $i \dots i+K-1$ of the doubled array, from prefix sums. A frame fits inside the rotation starting at $t$ when its start lies in $[t, t + N - K]$, so the answer for that rotation is the maximum of `frame_sum` over a window of $N - K + 1$ consecutive starts - a sliding-window maximum with a monotone deque. All $N$ rotations are precomputed and each `?` is a lookup.

## Edge cases

- $K \ge N$: the frame sees the whole array, and the answer is the total number of ones.
- Frames may not wrap around the end of the current array - that is why the window of valid starts has length $N - K + 1$.
- Only the shift count modulo $N$ matters.
- The request string is read as bytes: 33 is `!`.

## Dry run

`A = [1, 0, 0, 1, 1]`, `K = 3`, requests `?!!?`.

Doubled array `1 0 0 1 1 1 0 0 1 1`, frame sums by start `1 1 2 3 2 1 1 2`.

- `?` with 0 shifts: valid starts are 0-2 with sums `1 1 2`, answer 2.
- two shifts later the rotation starts at 3 (`1 1 1 0 0`): starts 3-5 have sums `3 2 1`, answer 3.
