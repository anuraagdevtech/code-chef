---
topic: Arrays
subtopic: Ordered condition checks
time: $O(N)$ per test case
space: $O(1)$
---
Three rules, and the **order** in which they are tested is what makes the solution correct:

1. All $N$ tests pass → $100$.
2. Otherwise, all of the first $M$ pass → $K$.
3. Otherwise → $0$.

Rule 2 carries the qualifier $M < N$, so a submission passing everything scores $100$, never $K$. Checking the prefix first would wrongly award $K$ to a perfect submission — sample case 3 is there to catch exactly that, with all four tests passing and the answer $100$.

In Python each check is a single `all(...)` over a slice, which short-circuits on the first failure:

- `all(v == 1 for v in a)` for the full set
- `all(v == 1 for v in a[:m])` for the prefix

Sample case 2 is the partial-credit case: the first two pass and the third fails, scoring $K = 50$.

Sample case 4 is the one that punishes a loose reading. Four of five tests pass — more than in case 2 — yet the score is $0$, because the failure sits at position $3$, *inside* the first $M = 3$. Partial credit depends on an unbroken **prefix**, not on a count of passes. A solution comparing the number of passes against $M$ would wrongly award $30$ here.

The constraint $M < N$ guarantees the two rules never collide, so there is no ambiguity about which applies.

## Edge cases

- **The full-pass check must come first.** The third row passes every test, which also means it passes the first $M$; testing the prefix first would award $K = 50$ instead of $100$. This ordering is the entire difficulty of the problem.
- **Passing the prefix but failing later** (the second row, where test $3$ fails): exactly $K$.
- **Failing inside the prefix** (the first and fourth rows): $0$, no matter how many later tests pass — the fourth row fails only test $3$ of $5$ and still scores nothing.
- **$M < N$ is guaranteed**, so subtask 1 is a strict prefix and the two conditions are genuinely distinct.
- **Subtask 1 is the *first* $M$ tests specifically**, not any $M$ of them, so the prefix slice is the right test.

## Dry run

| $N, M, K$ | verdicts | all pass? | first $M$ pass? | output |
|---|---|:---:|:---:|---:|
| $4, 2, 50$ | $1, 0, 1, 1$ | no | no | `0` |
| $3, 2, 50$ | $1, 1, 0$ | no | yes | `50` |
| $4, 2, 50$ | $1, 1, 1, 1$ | **yes** | yes | `100` |
| $5, 3, 30$ | $1, 1, 0, 1, 1$ | no | no | `0` |

Row 3 satisfies both conditions, which is why the full-pass branch has to be checked first.
