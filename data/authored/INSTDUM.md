---
topic: Prefix Sums
subtopic: Running total compared against the index
time: $O(N)$ per test case
space: $O(1)$
---
Strike rate after $i$ balls is $\frac{\text{runs}}{i} \times 100$, so it equals exactly $100$ precisely when the runs scored so far equal the balls faced:

$$\text{prefix sum}_i = i$$

No division is needed at all — clearing it turns a floating-point comparison into an integer identity, which is both exact and faster. Comparing `total / i * 100 == 100` would be the fragile version.

So the solution is a single pass maintaining a running total, incrementing a counter whenever that total matches the current ball number. Only the running sum needs storing, so this is $O(N)$ time and $O(1)$ space — no prefix array required, since each prefix is consumed immediately.

Sample case 3 is the all-ones case where the condition holds after every ball, giving $3$. Sample case 1 matches at balls $1$ and $3$ — after $[1]$ the total is $1$, and after $[1,0,2]$ it is $3$ — giving $2$. Sample case 2 never matches, since the opening $2$ runs off a single ball puts the total permanently ahead.

The efficiency constraints are worth reading: $T$ reaches $10^5$ and $N$ reaches $10^5$, but the **sum of $N$** is capped at $10^6$. That bound is the setter saying a linear pass per test case is intended and safe, while anything quadratic is not. Reading the whole input in one go rather than line by line matters at this volume.

## Edge cases

- **No match at all** (the second row): the answer is $0$, so zero is legitimate output.
- **Every prefix matches** (all ones): the answer is $N$ — the running total tracks the index exactly.
- **A zero run breaks a match and a later run restores it.** In the first row the totals are $1, 1, 3, 6$ against indices $1, 2, 3, 4$: a match at index $1$, lost at $2$ because of the zero, regained at $3$. So the count is not monotone and the whole prefix has to be walked.
- **$A_i$ may be $0$ or as large as $6$**, so the total can jump well past the index and never come back.
- A strike rate of exactly $100$ means runs equal balls faced, which is the condition $\text{total} = i$.

## Dry run

First sample, runs $1, 0, 2, 3$:

| ball $i$ | run | total | $\text{total} = i$? |
|---:|---:|---:|:---:|
| 1 | 1 | 1 | yes |
| 2 | 0 | 1 | no |
| 3 | 2 | 3 | yes |
| 4 | 3 | 6 | no |

Two matches, so the output is `2`. The third sample ($1,1,1$) matches at every ball, giving `3`.
