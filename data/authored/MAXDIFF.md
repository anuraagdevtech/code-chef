---
topic: Sorting
subtopic: Taking an extreme K-subset
time: $O(N \log N)$ per test case
space: $O(N)$
---
The son carries exactly $K$ items and Chef carries the other $N - K$. If the chosen $K$ weigh $S$ out of a total $W$, the gap between the two loads is

$$|W - 2S|$$

Maximising that means pushing $S$ as far from $W/2$ as possible — so $S$ should be either the **smallest** possible or the **largest** possible sum of $K$ items. After sorting, those are the first $K$ and the last $K$ entries, and the answer is the larger of the two resulting gaps.

Both candidates are genuinely needed in general, which is easy to miss. The statement says Chef carries the heavier group, so intuitively the son takes the lightest items — and for sample case 1 that is right: the son takes $2 + 4 = 6$, leaving Chef $23$, a gap of $17$. Taking the two heaviest would give only $7$.

But which extreme wins depends on $K$ relative to $N$. When $K$ is large, handing the son the $K$ **heaviest** items can leave a bigger imbalance, because he is carrying most of the shipment anyway. Evaluating both and taking the maximum covers either case without needing to work out the crossover.

Sample case 2 is the degenerate one: eight identical weights mean every $K$-subset sums the same, so both candidates agree at $|8 - 6| = 2$.

The absolute value matters because the chosen group may be the heavier one; without it the second candidate would come out negative and lose the `max` spuriously.

## Edge cases

- **Both extremes must be evaluated.** Giving the son the $K$ lightest is a different outcome from the $K$ heaviest, and which wins depends on $K$ and the weights: in the first row the lightest choice gives $17$ and the heaviest only $7$.
- **All weights equal** (the second row): the answer is $|N - 2K| = |8 - 6| = 2$, not $0$ — the difference comes from the group *sizes*, since $K < N$ forces unequal counts.
- **$K < N$ is guaranteed**, so neither group is ever empty and both slices are valid.
- **The result is an absolute difference**, so it does not matter which of the two gets the larger total; taking `abs` of both candidates covers it.
- **Only the $K$ smallest or $K$ largest can be optimal**, because swapping an interior item for a more extreme one moves the two sums further apart.
- Weights up to $10^5$ with $N \leq 100$ keeps every sum small.

## Dry run

First sample: weights $8, 4, 5, 2, 10$ sorted to $2, 4, 5, 8, 10$, total $29$, $K = 2$.

| son's share | son's sum | other's sum | difference |
|---|---:|---:|---:|
| lightest two: $2, 4$ | 6 | 23 | **17** |
| heaviest two: $8, 10$ | 18 | 11 | 7 |

Output `17`.
