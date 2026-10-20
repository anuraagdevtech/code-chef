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
