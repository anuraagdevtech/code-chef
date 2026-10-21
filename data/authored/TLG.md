---
topic: Arrays
subtopic: Running totals with a tracked maximum
time: $O(N)$
space: $O(1)$
---
The winner is not the player with the higher final score — it is whoever held the **largest lead at the end of any single round**. Sample case aside, those are genuinely different questions: in the worked example Player 2 finishes ahead on total score, yet Player 1 wins because of a $58$-point lead after round 1.

The solution is one pass maintaining two running totals. After adding each round's scores, the current lead is $|s_1 - s_2|$ and the leader is whoever is ahead. Track the largest lead seen so far along with its owner, and report that pair at the end.

Only the running sums and the best-so-far need storing, so this is $O(N)$ time and $O(1)$ space — the per-round table in the statement is an explanation, not a data structure to build.

Two details decide correctness. The lead must be computed from **cumulative** scores, not the round's own scores; using per-round values would make round 1 and round 5 look similar when their cumulative pictures are nothing alike. And the comparison for a new best should be strict (`>`), so that the *earliest* round achieving a given maximum is kept — though with the winner determined by the lead's magnitude, ties in lead value between the same leader change nothing either way.

The input is a single test case: $N$, then $N$ pairs. Output is the winning player's number and that maximum lead, space-separated.

## Edge cases

- **The lead is measured on cumulative totals, not on the round's own scores.** In the sample, round $2$ has a per-round gap of $45$, far larger than the cumulative lead of $13$ at that point — using the round's difference gives a different and wrong answer.
- **The maximum can occur in the first round and never be beaten**, which is exactly what happens here: the lead of $58$ after round $1$ survives all five rounds.
- **A tie in the running totals** gives a lead of $0$, which cannot beat the initial best, so the strict `>` keeps the earlier holder and no tie handling is needed.
- **Input shape**: $N$ followed by the rounds, with no test-case count; the output is two numbers on one line.

## Dry run

| round | scores | total 1 | total 2 | lead | best so far |
|---:|---|---:|---:|---:|---|
| 1 | $140, 82$ | 140 | 82 | 58 | **1 with 58** |
| 2 | $89, 134$ | 229 | 216 | 13 | 1 with 58 |
| 3 | $90, 110$ | 319 | 326 | 7 | 1 with 58 |
| 4 | $112, 106$ | 431 | 432 | 1 | 1 with 58 |
| 5 | $88, 90$ | 519 | 522 | 3 | 1 with 58 |

Output `1 58`. Note player $2$ leads from round $3$ onward but never by much.
