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

## Edge cases

- **More than $X$ may qualify on merit, and all of them advance.** The second row has three players past the mark with $X = 2$, and the answer sends all three — the top-up is a floor, not a cap.
- **Top-ups come only from the non-qualifiers**, longest throws first, which is why the already-qualified ids must be excluded from the candidate sort.
- **The qualifying mark is inclusive.** The third row's throw of exactly $6000$ cm meets $M = 6000$ and qualifies outright.
- **All $A_i$ are distinct**, so the top-up order is unambiguous and no tie-break at the cut is needed.
- **Nobody may qualify at all** (the first row, with $M = 8000$ against throws near $5000$), in which case the whole field of $X$ comes from the top-up.
- **The output is the count followed by the sorted ids**, so the set must be sorted at the end regardless of the order it was assembled in.
- **$X \leq N$ is guaranteed**, so the top-up never runs out of candidates.

## Dry run

Third sample: $N = 4$, $M = 6000$, $X = 3$, throws $5999, 5998, 6000, 6001$.

| id | throw | $\geq M$? |
|---:|---:|:---:|
| 1 | 5999 | no |
| 2 | 5998 | no |
| 3 | 6000 | **yes** |
| 4 | 6001 | **yes** |

Two qualified, one short of $X = 3$. The best non-qualifier is id $1$ at $5999$, so it is added.

Output `3 1 3 4`.
