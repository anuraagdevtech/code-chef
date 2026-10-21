# 469. Pokemon Battles

> CodeChef problem code [`PBATTLE`](https://www.codechef.com/problems/PBATTLE) &middot; difficulty **1739** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | Counting Pareto maxima of two orderings |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

There are $N$ Pokemon trainers numbered from $1$ to $N$. Each trainer has **one** Pokemon. All the trainers have arrived to participate in a contest.
There are two battle arenas, one in ground and other in water. Each Pokemon may have different power in both the arenas.
When two Pokemon fight in an arena, the Pokemon having higher power in that arena wins. It is guaranteed that all Pokemon have **distinct** powers in the same arena to avoid any ties.

The *strength* of a Pokemon trainer is determined to be the number of other Pokemon his Pokemon can defeat in **at least one** arena.

It is known that only the Pokemon trainers with the **highest** *strength* will qualify for the next round (multiple trainers may have the same strength). Find the number of Pokemon trainers who will qualify for the next round.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three lines of input.
    - The first line of each test case contains a single integer $N$, denoting the number of Pokemon trainers.
    - The second line will contain $N$ space-separated integers, $A_{1},A_{2},\ldots,A_{N}$, where $A_{i}$ denotes the power of the Pokemon of $i^{th}$ trainer in the ground arena.
    - The third line will contain $N$ space-separated integers, $B_{1},B_{2},\ldots,B_{N}$, where $B_{i}$ denotes the power of the Pokemon of $i^{th}$ trainer in the water arena.

**Output**

For each test case, output on a new line the number Pokemon trainers who will qualify for the next round.

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^{5}$
- $1 \leq A_i, B_i \leq 10^{9}$
- The elements of array $A$ are distinct.
- The elements of array $B$ are distinct.
- The sum of $N$ over all test cases won't exceed $2\cdot 10^{5}$.

## Sample

**Sample input**

```
4
2
1 2
3 4
2
1 2
2 1
3
1 2 3
1 4 2
5
2 3 5 4 1
4 2 1 5 6
```

**Sample output**

```
1
2
2
3
```

<details><summary>Explanation</summary>

**Test case 1:** The second trainer's Pokemon can defeat the first trainer's Pokemon in both arenas so his strength is $1$. Similarly, the first trainer's Pokemon can not defeat the second trainer's Pokemon in any arena so his strength will be $0$. Hence, only the second trainer will qualify.

**Test case 2:** The second trainer's Pokemon can defeat the first trainer's Pokemon in ground arena so his strength is $1$ and the first trainer's Pokemon can defeat the second trainer's Pokemon in water arena so his strength will also be $1$. Hence both of them will qualify.

**Test case 4:** The maximum strength possible is $4$. There are $3$ trainers with strength $4$:
- Trainer $3$: Trainer $3$'s pokemon has ground power equal to $5$, so, it can defeat all other $4$ pokemons in the ground arena. Thus, the trainer's strength is $4$.
- Trainer $4$: Trainer $4$'s pokemon has ground power equal to $4$. It can beat the pokemons having ground power less than $4$. These belong to trainers $1, 2,$ and $5$. Similarly, it has water power equal to $5$. Thus, it can also beat trainer $3$'s pokemon which has water power $1$. Thus, total strength of this trainer is $4$.
- Trainer $5$: Trainer $5$'s pokemon has water power equal to $6$, so, it can defeat all other $4$ pokemons in the water arena. Thus, the trainer's strength is $4$.

</details>

## Approach

Trainer $i$ beats $j$ in at least one arena unless $j$ is stronger in **both**. So

$$\text{strength}_i = (N-1) - \#\{\,j : A_j > A_i \text{ and } B_j > B_i\,\}$$

Maximising strength means minimising the number of trainers who dominate you, and the trainer with the largest $A$ is dominated by nobody. So the maximum strength is exactly $N-1$, and the qualifiers are the trainers with **zero** dominators — the **Pareto maxima** of the two orderings.

Counting them is one sweep. Sort by $A$ descending; a trainer is non-dominated exactly when its $B$ exceeds the largest $B$ among all trainers with a bigger $A$:

$$\text{qualifies}_i \iff B_i > \max\{\,B_j : A_j > A_i\,\}$$

so a running maximum of $B$ decides each trainer in $O(1)$. Distinct powers in each arena mean no ties to worry about.

The samples lay out the shapes. $A = [1,2], B = [3,4]$ has the second trainer ahead in both, so only one qualifies. Swapping to $B = [2,1]$ makes each better in one arena, so both qualify at strength $1$. $A = [1,2,3], B = [1,4,2]$ qualifies the $A$-leader and the $B$-leader but not the first trainer, who trails in both. And the five-trainer case qualifies three: the $A = 5$, $A = 4$ and $A = 1$ trainers, the last one on the strength of its chart-topping $B = 6$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = [int(x) for x in data[pos + 1:pos + 1 + n]]
        b = [int(x) for x in data[pos + 1 + n:pos + 1 + 2 * n]]
        pos += 1 + 2 * n
        # Strongest ground power first; a trainer survives if its water power
        # beats everything already seen.
        best_water = 0
        qualified = 0
        for i in sorted(range(n), key=lambda j: -a[j]):
            if b[i] > best_water:
                qualified += 1
                best_water = b[i]
        out.append(str(qualified))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N \log N)$ per test case
- **Space:** $O(N)$

> CodeChef tags: `Algorithms`
