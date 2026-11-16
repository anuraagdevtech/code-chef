---
topic: Basic Math
subtopic: Energy balance gives the shortest completion time
time: $O(1)$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Convert both durations to seconds. For $r$ running seconds, the initial $X$ energy pays for the first $X$ runs; any remaining run requires a resting second beforehand. Hence the least elapsed time is $r+\max(0,r-X)$.

This lower bound is attainable by running until energy is exhausted, then alternating rest and run. Compare it to the deadline.

## Edge cases

- Energy is in seconds, while the input durations are in minutes.
- No rest is needed when $X\geq60R$.
- Finishing exactly at the deadline is allowed.

## Dry run

With `X=60, R=3`, running needs `180` seconds and resting needs `120`, totaling `300`. A five-minute deadline succeeds; four minutes fails.
