---
topic: Sorting
subtopic: Counting Pareto maxima of two orderings
time: $O(N \log N)$ per test case
space: $O(N)$
---
Trainer $i$ beats $j$ in at least one arena unless $j$ is stronger in **both**. So

$$\text{strength}_i = (N-1) - \#\{\,j : A_j > A_i \text{ and } B_j > B_i\,\}$$

Maximising strength means minimising the number of trainers who dominate you, and the trainer with the largest $A$ is dominated by nobody. So the maximum strength is exactly $N-1$, and the qualifiers are the trainers with **zero** dominators — the **Pareto maxima** of the two orderings.

Counting them is one sweep. Sort by $A$ descending; a trainer is non-dominated exactly when its $B$ exceeds the largest $B$ among all trainers with a bigger $A$:

$$\text{qualifies}_i \iff B_i > \max\{\,B_j : A_j > A_i\,\}$$

so a running maximum of $B$ decides each trainer in $O(1)$. Distinct powers in each arena mean no ties to worry about.

The samples lay out the shapes. $A = [1,2], B = [3,4]$ has the second trainer ahead in both, so only one qualifies. Swapping to $B = [2,1]$ makes each better in one arena, so both qualify at strength $1$. $A = [1,2,3], B = [1,4,2]$ qualifies the $A$-leader and the $B$-leader but not the first trainer, who trails in both. And the five-trainer case qualifies three: the $A = 5$, $A = 4$ and $A = 1$ trainers, the last one on the strength of its chart-topping $B = 6$.

## Edge cases

- **The top strength is always $N-1$**, so the question is which trainers achieve it. A Pokemon fails to beat another only when that other wins *both* arenas, so strength $N-1$ means nobody dominates it in both — a Pareto maximum.
- **Such a trainer always exists** (the one with the highest ground power is undominated), which is why the maximum strength is $N-1$ rather than something that must be computed.
- **Sorting by descending ground power turns domination into a running maximum**: a trainer qualifies iff its water power beats every trainer already seen, all of which have greater ground power.
- **Both arenas can produce a winner** (the second sample row, where each beats the other in one arena): then both have strength $1 = N-1$ and both qualify.
- **Total domination** (the first row) leaves exactly one qualifier.
- **The powers are distinct within each arena**, so no tie-break is needed and the strict `>` is safe.
- **Sum of $N \leq 2 \cdot 10^5$**: one sort and one pass.

## Dry run

Fourth sample: ground powers $2, 3, 5, 4, 1$ and water powers $4, 2, 1, 5, 6$.

| trainer (by descending ground) | ground | water | beats every water so far? | qualified |
|---:|---:|---:|:---:|---:|
| 3 | 5 | 1 | yes (nothing before) | 1 |
| 4 | 4 | 5 | yes | 2 |
| 2 | 3 | 2 | no | 2 |
| 1 | 2 | 4 | no | 2 |
| 5 | 1 | 6 | yes | **3** |

Output `3`. Trainer $5$ is weakest on the ground but strongest in the water, so nobody dominates it in both.
