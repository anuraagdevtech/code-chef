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
