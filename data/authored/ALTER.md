---
topic: Number Theory
subtopic: Divisibility plus an alternation constraint
time: $O(1)$ per test case
space: $O(1)$
---
Alice gains $A$ on each of her work days and Bob gains $B$ on each of his, so reaching exactly $P$ and $Q$ requires

$$a = \frac{P}{A}, \qquad b = \frac{Q}{B}$$

to both be **whole numbers** — otherwise the targets are simply unreachable.

But divisibility alone is not enough, and this is where the problem has its teeth. Because they work on **alternating** days, after $d$ days one of them has worked $\lceil d/2 \rceil$ times and the other $\lfloor d/2 \rfloor$. So the two work counts can never differ by more than one:

$$|a - b| \leq 1$$

That covers all three legal shapes — equal counts after an even number of days, or one ahead after an odd number — and it does not matter which of them takes the odd days, since both orderings are allowed.

Sample case 2 shows divisibility passing while the alternation fails: $P = 3$ with $A = 1$ needs three Alice-days, but $Q = 2$ with $B = 2$ needs only one Bob-day, and a gap of $2$ is impossible. Sample case 4 is the same failure with a gap of $2$ between three and five.

Sample case 3 is the off-by-one case that must be **accepted**: $a = 1$ and $b = 2$ differ by exactly one, which happens naturally after three days with Bob starting.

A strict equality check would reject it, and a check omitting the gap entirely would accept cases 2 and 4 — both halves are load-bearing.

## Edge cases

- **Divisibility first**: each person's total must be an exact multiple of their per-day gain, so $P \bmod A$ and $Q \bmod B$ must both be zero. The fourth row passes this and still fails.
- **Alternation bounds the day counts.** They work on alternate days, so the two counts can differ by at most one — $|P/A - Q/B| \leq 1$. The second row needs $3$ days from Alice and $1$ from Bob, which no alternating schedule produces.
- **A difference of exactly one is fine** (the third row: one day for Alice, two for Bob), since whoever starts gets the extra day.
- **Equal counts are fine too** (the first row), corresponding to an even total number of days.
- **$P, Q \geq 1$**, so both day counts are at least one and the degenerate "nobody works" case cannot arise.
- **Which of them takes the odd days is not fixed**, which is exactly why the bound is on the absolute difference rather than on a signed one.

## Dry run

| $A$ | $B$ | $P$ | $Q$ | Alice's days | Bob's days | difference | output |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 2 | 1 | 2 | 1 | 1 | 0 | `YES` |
| 1 | 2 | 3 | 2 | 3 | 1 | **2** | `NO` |
| 4 | 3 | 4 | 6 | 1 | 2 | 1 | `YES` |
| 3 | 5 | 9 | 25 | 3 | 5 | **2** | `NO` |
