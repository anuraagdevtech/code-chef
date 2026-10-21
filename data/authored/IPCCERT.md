---
topic: Arrays
subtopic: Filtering rows on two independent criteria
time: $O(N \cdot K)$
space: $O(1)$
---
A student qualifies when **both** conditions hold: total watch time of at least $M$ minutes, and at most $10$ questions asked.

$$\sum_{j=1}^{K} T_{i,j} \geq M \quad\text{and}\quad Q_i \leq 10$$

Each row of input holds $K$ watch times followed by the question count, so the row is read as $K+1$ values with the last one split off. Mis-slicing that boundary — including $Q_i$ in the watch-time sum, or summing only $K-1$ entries — is the main hazard, and it would produce plausible-looking totals.

The threshold $10$ is a **constant in the statement**, not an input. It is easy to look for a fourth input value that does not exist; the first line holds only $N$, $M$ and $K$.

Note there is **no $T$** here: one dataset, one answer.

Sample walkthrough, with $M = 8$:

| Student | Watch total | Questions | Eligible |
|---|---|---|---|
| 1 | $6$ | $5$ | no — too few minutes |
| 2 | $12$ | $4$ | **yes** |
| 3 | $12$ | $11$ | no — one question too many |
| 4 | $6$ | $12$ | no — both fail |

Only one qualifies. Student 3 is the discriminating case: plenty of watch time but $11 > 10$ questions, so a solution checking only the minutes would answer $2$.

Both comparisons are inclusive — exactly $M$ minutes or exactly $10$ questions still qualifies.

## Edge cases

- **Enough watch time but too many questions** (the third row: $12$ hours watched, $11$ questions): ineligible. Both criteria matter and must be ANDed.
- **Few enough questions but not enough watching** (rows 1 and 4): also ineligible.
- **The question limit of $10$ is a constant from the statement, not an input.** Expecting it on the first line misparses every case.
- **Exactly on either threshold** (watched $= M$, or questions $= 10$): eligible, so both comparisons are non-strict.
- **Input shape**: the first line is $N$, $M$, $K$ — not a test-case count — and each row has $K$ watch times followed by the question count, so the row stride is $K+1$.

## Dry run

$N = 4$, $M = 8$, $K = 4$:

| row | watch times | total | questions | $\geq 8$? | $\leq 10$? | eligible |
|---:|---|---:|---:|:---:|:---:|:---:|
| 1 | $1,2,1,2$ | 6 | 5 | no | yes | no |
| 2 | $3,5,1,3$ | 12 | 4 | yes | yes | **yes** |
| 3 | $1,2,4,5$ | 12 | 11 | yes | no | no |
| 4 | $1,1,1,3$ | 6 | 12 | no | no | no |

One eligible student, so the output is `1`.
