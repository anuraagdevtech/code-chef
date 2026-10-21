---
topic: Basic Math
subtopic: Maximum against the sum of the rest
time: $O(1)$ per test case
space: $O(1)$
---
A monopoly exists when some company's profit strictly exceeds the combined profit of the other three. The naive reading suggests four separate checks — $P > Q+R+S$, then $Q > P+R+S$, and so on — which works but repeats itself.

A cleaner formulation: only the **largest** company can possibly dominate, since if any company beats the sum of the rest then the largest certainly does. So let $M = \max(P, Q, R, S)$ and $S_{\text{total}} = P + Q + R + S$. The rest sum to $S_{\text{total}} - M$, and the condition becomes

$$M > S_{\text{total}} - M \quad\Longleftrightarrow\quad 2M > S_{\text{total}}$$

This is the same "strict majority" shape that appeared in the Mahasena problem — one element outweighing everything else is always $2 \times \text{part} > \text{whole}$. Recognising the pattern means the code is two built-in calls and a comparison, and it generalises to any number of companies without a longer chain of `or`s.

Strictness matters at the boundary: if the largest exactly equals the sum of the others, $2M = S_{\text{total}}$ and the answer is `NO`. All profits are at least $1$, so no company can dominate by default.

Sample case 2 ($30, 20, 6, 4$) has $M = 30$ against a total of $60$, exactly the tie, and correctly answers `NO`.

## Edge cases

- **Exact tie**, $2\max = \text{sum}$: the sample's $30\,20\,6\,4$ has max $30$ and sum $60$, so $60 > 60$ fails and the answer is `NO`. The comparison must be **strict**, and this row is there to catch `>=`.
- **Two values tied for largest** ($5\,5\,1\,1$): max $5$, sum $12$, so `NO` — neither copy can dominate, and taking "the maximum" rather than "a maximum" causes no trouble because the test only uses its value.
- **All four equal** ($1\,1\,1\,1$): $2 > 4$ fails, `NO`.
- **One value dominating** ($1\,1\,1\,10$): $20 > 13$, `YES`.
- **Only the largest can possibly dominate**, so checking the maximum alone is sufficient — there is no need to test all four.

## Dry run

| $P$ | $Q$ | $R$ | $S$ | max | sum | $2\max > \text{sum}$ | output |
|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 1 | 1 | 10 | 10 | 13 | $20 > 13$ yes | `YES` |
| 30 | 20 | 6 | 4 | 30 | 60 | $60 > 60$ no | `NO` |
| 100 | 90 | 3 | 4 | 100 | 197 | $200 > 197$ yes | `YES` |
| 14 | 15 | 16 | 17 | 17 | 62 | $34 > 62$ no | `NO` |

Row 2 is the exact tie; row 3 is a narrow win by three.
