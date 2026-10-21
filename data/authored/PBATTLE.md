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
