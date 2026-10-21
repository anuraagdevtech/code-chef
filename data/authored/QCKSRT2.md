---
topic: Sorting
subtopic: Which pivot choices preserve stability
time: $O(n)$
space: $O(n)$
---
A sort is **stable** when elements comparing equal keep their original relative order. Here the pairs are compared on their first component only, so two pairs sharing a first component are "equal" and must not be reordered.

The modified quicksort partitions around the chosen pivot **element**, placing that element ahead of the others that tie with it. So picking a pivot that is **not the earliest** occurrence of its key drags it in front of equal elements that originally preceded it — breaking stability.

Hence a pivot index $i$ is safe exactly when no earlier index shares its first component:

$$\text{valid} \iff a_j \neq a_i \text{ for all } j < i$$

— that is, $i$ is the **first occurrence** of its key.

The sample makes this concrete. The pairs are $(1,2), (2,3), (2,1), (3,2)$ with keys $1, 2, 2, 3$. Index $2$ holds the *second* pair with key $2$, so choosing it pulls $(2,1)$ ahead of $(2,3)$ — exactly the reordering the explanation flags. Indices $0$, $1$ and $3$ are each the first sighting of their key, giving three valid choices: `0 1 3`.

Randomising over this restricted set is what reconciles the two goals: the pivot is still chosen at random (so the expected running time stays $O(n \log n)$), but only among choices that cannot disturb equal elements.

Tracking seen keys in a set makes this a single pass. Note that the second components are irrelevant throughout — they are the payload the stability requirement protects, not part of the comparison.
