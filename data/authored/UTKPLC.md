---
topic: Conditionals & Case Work
subtopic: Ranking by a given priority order
time: $O(1)$ per test case
space: $O(1)$
---
The preference order arrives as data rather than being fixed, so the solution builds the ranking at runtime: map the first-listed company to rank $0$, the second to $1$, the third to $2$. Utkarsh accepts whichever of his two offers has the **lower** rank.

With a dictionary from company letter to rank, the answer is `min(x, y, key=rank.get)` — one expression, no case analysis. Building the ranking from the input is what keeps this short; hard-coding `A > B > C` would fail sample case 2, where the stated order is `B C A` and the answer for offers `A C` is `C`.

Note that lower rank means *more* preferred, so the selection uses `min`, not `max`. Inverting that is the easy mistake, and sample case 1 would not catch it — there the preference order is `A B C` and the offers are `A B`, where `A` is both first-preferred and alphabetically first.

The constraints guarantee all three letters appear exactly once in the preference line and that the two offers are distinct, so every lookup succeeds and there is never a tie to break.

The input spans two lines per test case — three characters, then two — which the flat token read handles without caring about line boundaries.
