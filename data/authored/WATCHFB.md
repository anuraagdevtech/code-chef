---
topic: Simulation
subtopic: Tracking the at-most-two consistent states
time: $O(N)$ per test case
space: $O(1)$
---
After each reply there are at most **two** candidate scores: $(A, B)$ and $(B, A)$ for an ambiguous reply, or just $(A, B)$ for a labelled one. So the state space never grows, and the whole problem is filtering those candidates against history.

The filter is **monotonicity**: goals accumulate, so the new score must dominate some previously possible score componentwise. Starting from the single state $(0,0)$, each reply becomes

$$\text{new} = \{\,c \in \text{candidates} : \exists\, p \in \text{states},\ c \geq p \text{ in both coordinates}\,\}$$

and the answer is `YES` precisely when every surviving state agrees on the favourite team's goals. That happens either because the reply was labelled, because $A = B$, or because monotonicity eliminated one of the two orderings.

Keeping the whole set of survivors matters: a later reply may be disambiguated by an earlier ambiguous one, and discarding information too early would wrongly report `NO`.

The sample shows each mechanism. The first reply, `2 0 1`, admits both $(0,1)$ and $(1,0)$ — `NO`. The second is labelled, so `YES` and the state collapses to $(3,1)$. The third, `2 2 4`, is ambiguous but $(2,4)$ cannot follow $(3,1)$ — the favourite's score would have dropped — so only $(4,2)$ survives: `YES`. The fourth, `2 5 6`, has both orderings dominating $(4,2)$, so `NO`. The fifth, `2 8 8`, is ambiguous in form but the two orderings coincide: `YES`. And the last, `2 9 10`, is ambiguous again.

Note the ambiguity can return after being resolved, as the last two replies show.

## Edge cases

- **At most two states survive each reply**, since an ambiguous score admits only the two orderings — so the whole history collapses to a tiny candidate set rather than needing a search.
- **Goals only accumulate**, so a candidate is viable only if it dominates some state consistent with the previous replies — that monotone filter is what prunes the ambiguity.
- **Equal scores are unambiguous even when the teams are unnamed**, which is why `a == b` collapses to a single candidate (the fifth reply, $8$ to $8$).
- **A type-1 reply names the teams**, so it always leaves one state — and it can retroactively resolve nothing, but it does narrow the future.
- **The answer is `YES` when all surviving states agree on the favourite team's score**, which is the deducible case — the second reply becomes deducible even though the first was not.
- **The first reply with distinct scores is always ambiguous**, since both orderings dominate the initial $0$–$0$.
- **At least one consistent sequence is guaranteed**, so the surviving set is never empty.

## Dry run

The sample's six replies, tracking the viable states as (favourite, other):

| reply | candidates | viable after filtering | deducible? |
|---|---|---|---|
| `2 0 1` | $(0,1)$, $(1,0)$ | both | `NO` |
| `1 3 1` | $(3,1)$ | $(3,1)$ | `YES` |
| `2 2 4` | $(2,4)$, $(4,2)$ | $(4,2)$ only — $(2,4)$ cannot follow $(3,1)$ | `YES` |
| `2 5 6` | $(5,6)$, $(6,5)$ | both | `NO` |
| `2 8 8` | $(8,8)$ | $(8,8)$ | `YES` |
| `2 9 10` | $(9,10)$, $(10,9)$ | both | `NO` |

The third reply is resolved by the second: a favourite-team score of $2$ would mean goals were lost.
