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
