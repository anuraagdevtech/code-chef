---
topic: Simulation
subtopic: Track which original position every final value comes from
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
The transformation only copies values, so every final entry is a copy of some original entry. Simulate the $N$ steps on indices instead of values: start with `source[i] = i` and, in step $i$, set `source[i] = source[P_i]`, reading the current (possibly already overwritten) value. At the end `source[i]` names the original position whose value ends up at $i$.

The final array is constant exactly when all original positions that occur as a source hold the same value. Call these the surviving positions; all other positions are overwritten before they are ever read by a survivor and are completely free.

- If the surviving positions contain two different non-zero values, the answer is 0.
- Otherwise the zeros among the survivors are all forced to the common value: if some survivor is non-zero that value is fixed, else it can be chosen in $M$ ways.
- Every zero at a non-surviving position contributes an independent factor $M$.

The answer is $M^{\text{free zeros} + [\text{no fixed survivor}]}$ modulo $10^9 + 7$.

## Edge cases

- Steps are sequential: step $i$ may read a position that an earlier step already changed.
- Non-zero entries at non-surviving positions impose nothing.
- A fixed point $P_i = i$ simply keeps its own value in that step.
- $M$ is up to $10^9$, so the power is computed modularly.

## Dry run

`P = [3, 1, 2]`, `A = [0, 0, 0]`, `M = 2`.

Sources: step 1 copies from position 3: `[3, 2, 3]`; step 2 copies from position 1, which now holds source 3: `[3, 3, 3]`; step 3 copies from position 2: `[3, 3, 3]`.

Only position 3 survives and it is a zero: $M$ choices for it. Positions 1 and 2 are free zeros: $M^2$.

Answer $2^3 = 8$.
