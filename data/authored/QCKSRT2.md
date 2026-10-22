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

## Edge cases

- **Only the earliest occurrence of a key is a safe pivot.** Pivoting on a later copy pulls it ahead of the equal elements that preceded it, which is exactly the instability the problem is about.
- **Only the first component is compared**, so two pairs with the same first value are "equal" however their second components differ — which is why the set is keyed on the first element alone.
- **Every distinct key contributes exactly one valid index**, so the answer's size is the number of distinct first components.
- **All-distinct keys make every index valid**, and all-equal keys leave only index $0$.
- **The indices are reported in increasing order**, which the left-to-right scan produces naturally.
- **Two things are printed**: the count then the indices.
- **There is no test-case count**: the input is $n$ followed by $2n$ integers, read as pairs.

## Dry run

Sample: the pairs $(1,2), (2,3), (2,1), (3,2)$, so the keys are $1, 2, 2, 3$.

| index | key | first occurrence? | valid pivot |
|---:|---:|:---:|:---:|
| 0 | 1 | yes | ✓ |
| 1 | 2 | yes | ✓ |
| 2 | 2 | no | — |
| 3 | 3 | yes | ✓ |

Output `3` then `0 1 3`. Pivoting on index $2$ would move $(2,1)$ ahead of $(2,3)$.
