[&larr; 662. Musical Rods](MUSROD.md) &middot; [Index](../../README.md) &middot; [711. Two Piles &rarr;](SPLITMIN.md)

# 687. Chef and Ants

> CodeChef problem code [`ANTSCHEF`](https://www.codechef.com/problems/ANTSCHEF) &middot; difficulty **2244** &middot; time limit **2s**

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | Swap identities at collisions, then count meetings ray by ray |
| **Time** | $O(S \log S)$ per test case, $S$ the total number of ants |
| **Space** | $O(S)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

Chef has been researching ant colonies for many years and finally discovered all their secrets.

An ant colony consists of $N$ distinct lines (numbered $1$ through $N$) that pass through a point $\mathsf{O}$, which is the queen's home. For each valid $i$, there are $M_i$ ants on the $i$-th line.

For each valid $i$ and $j$, the $j$-th ant on the $i$-th line initially has a non-zero coordinate $X_{i,j}$ with the following meaning:
- The distance of this ant from $\mathsf{O}$ is $|X_{i,j}|$.
- Let's choose a direction along the $i$-th line from $\mathsf{O}$. The exact way in which this direction is chosen does not matter here, it only needs to be the same for all ants on the same line.
- If $X_{i,j}$ is positive, this ant is at the distance $|X_{i,j}|$ from $\mathsf{O}$ in the chosen direction. Otherwise, it is at this distance from $\mathsf{O}$ in the opposite direction.

In other words, two ants $j$ and $k$ on a line $i$ are at the same side of $\mathsf{O}$ if the signs of $X_{i,j}$ and $X_{i,k}$ are the same or on opposite sides if the signs are different.

All ants move with the same constant speed. Initially, all of them are moving towards $\mathsf{O}$. Whenever two or more ants meet (possibly at $\mathsf{O}$), all of these ants turn around and start moving in the opposite directions with the same speed. We call this a *collision*. Even if an ant reaches $\mathsf{O}$ without meeting an ant there, it keeps moving in the same direction. An ant may change direction multiple times.

Help Chef find the total number of collisions between ants. Note that even if more than two ants meet, it counts as only one collision.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- $N$ lines follow. For each valid $i$, the $i$-th of these lines contains an integer $M_i$, followed by a space and $M_i$ space-separated integers $X_{i,1}, X_{i,2}, \ldots, X_{i,M_i}$.

**Output**
For each test case, print a single line containing one integer ― the number of collisions between ants.

**Constraints**
- $1 \leq T \leq 1,000$
- $1 \leq N \leq 2 \cdot 10^5$
- $1 \leq M_i \leq 5 \cdot 10^5$ for each valid $i$
- $1 \leq |X_{i,j}| \leq 10^9$ for each valid $i,j$
- $X_{i,j} \lt X_{i,j+1}$ for each valid $i,j$
- the sum of $N$ over all test cases does not exceed $2 \cdot 10^5$
- the sum of $M_1 + M_2 + \ldots + M_N$ over all test cases does not exceed $10^6$

**Subtasks**
**Subtask #1 (30 points):** $N = 1$

**Subtask #2 (70 points):** original constraints

## Constraints

- $1 \leq T \leq 1,000$
- $1 \leq N \leq 2 \cdot 10^5$
- $1 \leq M_i \leq 5 \cdot 10^5$ for each valid $i$
- $1 \leq |X_{i,j}| \leq 10^9$ for each valid $i,j$
- $X_{i,j} \lt X_{i,j+1}$ for each valid $i,j$
- the sum of $N$ over all test cases does not exceed $2 \cdot 10^5$
- the sum of $M_1 + M_2 + \ldots + M_N$ over all test cases does not exceed $10^6$

## Sample

**Sample input**

```
1
2
2 -2 1
1 2
```

**Sample output**

```
2
```

<details><summary>Explanation</summary>

**Example case 1:** First, the ants on the first line collide at the coordinate $-1/2$ and change directions. Finally, ant $2$ on the first line collides with the only ant on the second line; this happens at $\mathsf{O}$. No collisions happen afterwards.

</details>

## Approach

All ants walk towards $\mathsf{O}$ at the same speed, and ants that meet turn around. When two ants meet head-on and both reverse, the picture is the same as if they had passed through each other, so follow "ghosts" that keep going instead of the real ants - the set of meeting points is unchanged.

A ghost at distance $d$ reaches $\mathsf{O}$ at time $d$. What happens there depends on whether the distance is shared:

- If several ants (on any lines) have the same distance $d$, they all arrive together: one collision at $\mathsf{O}$, and each ghost turns back along the side it came from.
- If the distance is unique, the ghost walks through $\mathsf{O}$ and continues outward on the opposite side of its own line.

After that the ghost walks outward for ever, and every ant still walking inward on that same ray - same line, the relevant side, larger distance - meets it exactly once. Two outgoing ghosts never meet, and each off-centre collision is one outgoing-incoming meeting, so it is counted once.

So the answer is the number of shared distances, plus, for every ant, the number of ants on its line with a larger distance on the side it leaves along: its own side if its distance is shared, the opposite side otherwise. Sorting each line by distance and keeping the remaining counts per side gives these numbers in one pass.

## Solution (Python)

```python
import sys
from collections import Counter


def solve(tokens):
    n = next(tokens)
    lines = []
    distance_count = Counter()
    for _ in range(n):
        k = next(tokens)
        coords = [next(tokens) for _ in range(k)]
        lines.append(coords)
        distance_count.update((abs(coord) for coord in coords))
    collisions = sum((v > 1 for v in distance_count.values()))
    for coords in lines:
        negative_left = sum((coord < 0 for coord in coords))
        positive_left = len(coords) - negative_left
        for coord in sorted(coords, key=abs):
            if coord < 0:
                negative_left -= 1
            else:
                positive_left -= 1
            if distance_count[abs(coord)] > 1:
                collisions += negative_left if coord < 0 else positive_left
            else:
                collisions += positive_left if coord < 0 else negative_left
    return str(collisions)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Complexity

- **Time:** $O(S \log S)$ per test case, $S$ the total number of ants
- **Space:** $O(S)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- A collision of many ants at $\mathsf{O}$ counts once.
- Ants on different lines can only meet at $\mathsf{O}$.
- Two ants on the same line at equal distances on opposite sides also meet at $\mathsf{O}$.
- The counts can be large when one line holds many ants: about $M^2 / 2$.

## Dry run

Line 1 has ants at $-2$ and $1$; line 2 has an ant at $2$.

Distance 2 is shared (line 1 and line 2): one collision at $\mathsf{O}$. Distance 1 is unique.

- The ant at $1$ (line 1) passes through $\mathsf{O}$ onto the negative side, where the ant at $-2$ is still coming in: 1 meeting (at $-1/2$).
- The ants at distance 2 turn back at $\mathsf{O}$; nobody farther out is left on their rays.

Answer $1 + 1 = 2$.

---

Same problem in rating order (#649 of 735): [../../by-rating/649-ANTSCHEF.md](../../by-rating/649-ANTSCHEF.md)
