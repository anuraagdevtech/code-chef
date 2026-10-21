---
topic: Sorting
subtopic: Two-stage selection
time: $O(N \log N)$ per test case
space: $O(N)$
---
The selection runs in two passes, and they must be applied **in order**.

**Stage 1** admits everyone whose throw reaches the qualifying mark: $A_i \geq M$. This is a threshold, not a ranking — any number of players may clear it, possibly more than $X$.

**Stage 2** only fires if stage 1 produced **fewer than $X$** qualifiers. It then tops up the field with the longest throws among those *not already in*, until $X$ players are selected.

Two things are easy to get wrong. The top-up draws only from the **non-qualifiers**, so a player already admitted is not reconsidered. And stage 2 never *removes* anyone — if stage 1 already yielded more than $X$ players, they all stay and the final count exceeds $X$.

Sample case 2 is exactly that overflow: the mark is a lenient $5000$, all three players clear it, and the answer lists three even though $X = 2$.

Sample case 1 is the opposite extreme: nobody reaches $8000$, so stage 1 is empty and the two longest throws fill both spots.

Sample case 3 mixes them: two players clear $6000$, and one more is drawn from the remainder — the $5999$, not the $5998$.

Output is the count followed by the IDs **in increasing order**, so the selected set is sorted by ID at the end even though the top-up ranked by distance. The guarantee that all $A_i$ are distinct means that ranking has no ties to break.
