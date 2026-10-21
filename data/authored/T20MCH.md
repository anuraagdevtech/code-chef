---
topic: Basic Math
subtopic: Best-case bound
time: $O(1)$
space: $O(1)$
---
The question is whether Team B *can* win, not whether it is likely, so the right move is to compute their **maximum possible** final score and compare it against the target.

An over consists of $6$ balls scoring at most $6$ runs each, so an over yields at most $36$ runs. Team B has $20 - O$ overs left, so the best they can finish on is

$$C + 36(20 - O)$$

They win if that strictly exceeds $R$, since the problem requires a higher score and a tie is not a win.

Framing it as an upper bound is what makes this a one-liner rather than a search. Any question of the form "is it possible to reach a target" becomes "is the optimum at least the target" — there is nothing to simulate once the best case is in hand.

The sample is deliberately tight: $648 + 36 \times 2 = 720$ against $R = 719$, a margin of exactly one run. Using a per-over maximum of $30$, or forgetting that $20 - O$ overs remain rather than $O$, flips the answer.

Two details to note. There is **no $T$** here — a single line of three integers is the whole input. And the input order is $R, O, C$: target, overs bowled, then runs scored, which is not the order the prose introduces them in.

## Edge cases

- **The best case exactly ties the target**: the two sample runs differ by a single run, $719$ and $720$, against a best possible $720$. A tie is not a win, so the comparison must be **strict** — this pair exists to catch `>=`.
- **One over left** ($O = 19$): the best case adds only $36$.
- **A T20 has $20$ overs**, so the overs remaining are $20 - O$; using $O$ itself inverts the whole calculation.
- **$36$ per over** is $6$ balls at $6$ runs each, the theoretical ceiling — the constraint $C \leq 36 \cdot O$ confirms the same rate applies to what has already been scored.
- **Input order is $R$, $O$, $C$**, with no test-case count.

## Dry run

Sample 1: $R = 719$, $O = 18$, $C = 648$.

| step | value |
|---|---|
| overs left | $20 - 18 = 2$ |
| best possible extra | $2 \times 36 = 72$ |
| best final score | $648 + 72 = 720$ |
| $720 > 719$? | yes |
| output | `YES` |

Sample 2 is identical but with $R = 720$: now $720 > 720$ fails, so `NO`.
