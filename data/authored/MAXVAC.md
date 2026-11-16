---
topic: Greedy
subtopic: Vacations per run of holidays, plus the best gain from bridging one workday
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
A maximal run of $\ell$ consecutive holidays allows $\lfloor \ell / X \rfloor$ vacations, and runs are independent. Without any change the answer is the sum of that over all runs.

Turning one workday into a holiday merges the run on its left, the day itself and the run on its right into one run of length $\ell_1 + \ell_2 + 1$ (either side may be empty). The gain is

$$\Bigl\lfloor \frac{\ell_1 + \ell_2 + 1}{X} \Bigr\rfloor - \Bigl\lfloor \frac{\ell_1}{X} \Bigr\rfloor - \Bigl\lfloor \frac{\ell_2}{X} \Bigr\rfloor,$$

and no other run is affected. Splitting the string at every `1` lists the runs in order, including empty ones between adjacent workdays, so consecutive entries of that list are exactly the pairs separated by one workday. Add the best gain, or 0 if no flip helps.

## Edge cases

- No workday at all: there is nothing to flip.
- Adjacent workdays give empty runs, which the split keeps as zeros.
- $X = 1$: every holiday is a vacation and a flip always adds one (if a workday exists).
- The flip is optional.

## Dry run

`S = 0010001`, `X = 2`.

Runs: `2, 3, 0` (the last one is the empty run after the final `1`). Base: $1 + 1 + 0 = 2$.

- flip the first workday: $\lfloor 6/2 \rfloor - 1 - 1 = 1$
- flip the last one: $\lfloor 4/2 \rfloor - 1 - 0 = 1$

Answer $2 + 1 = 3$.
