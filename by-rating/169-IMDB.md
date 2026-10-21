# 169. Motivation

> [`IMDB`](https://www.codechef.com/problems/IMDB) &middot; difficulty **1098** &middot; time limit **1s** &middot; Level up from 1* to 2* (Level 2)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Maximum over a filtered subset |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

**Read problem statements in [Russian](https://www.codechef.com/download/translated/LTIME94/russian/IMDB.pdf)**
Chef has been searching for a good motivational movie that he can watch during his exam time. His hard disk has $X$ GB of space remaining. His friend has $N$ movies represented with $(S_i, R_i)$  representing (space required, IMDB rating). Help Chef choose the single best movie (highest IMDB rating) that can fit in his hard disk.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $X$.
- $N$ lines follow. For each valid $i$, the $i$-th of these lines contains two space-separated integers $S_i$ and $R_i$.

**Output**
For each test case, print a single line containing one integer - the highest rating of an IMDB movie which Chef can store in his hard disk.

**Constraints**
- $1 \leq T \leq 10$
- $1 \leq N \leq 5 \cdot 10^4$
- $1 \leq X \leq 10^9$
- $1 \leq S_i, R_i \leq 10^9$ for each valid $i$
- $X \ge S_i$ for atleast one valid $i$

**Subtasks**
**Subtask #1 (100 points):** original constraints

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 5 \cdot 10^4$
- $1 \leq X \leq 10^9$
- $1 \leq S_i, R_i \leq 10^9$ for each valid $i$
- $X \ge S_i$ for atleast one valid $i$

## Sample

**Sample input**

```
3
1 1
1 1
2 2
1 50
2 100
3 2
1 51
3 100
2 50
```

**Sample output**

```
1
100 
51
```

<details><summary>Explanation</summary>

**Example case 1:** Since there is only $1$ movie available and requires space equivalent to the empty space in the hard disk, Chef can only obtain maximum IMDB rating of $1$.

**Example case 2:** Since out of the $2$ available movies, both can fit in the free memory, we only care to take the one with higher rating, i.e, rating of $max(50, 100) = 100$.

**Example case 3:** Since out of the $3$ available movies, only the first and the last movies fit in the free memory, we only care to take the one with higher rating amongst these $2$, i.e, rating of $\max(51, 50) = 51$.

</details>

## Approach

Chef wants the highest-rated movie that **fits**, so the answer is

$$\max \{\, R_i : S_i \leq X \,\}$$

a single pass keeping a running maximum over the qualifying entries only.

The guarantee that $X \geq S_i$ for at least one $i$ means the filtered set is never empty, so no sentinel or "no answer" case is needed — but it is worth noticing the guarantee rather than assuming it, since a running maximum seeded at $0$ would silently return $0$ on an empty set.

The trap is sorting. It is tempting to sort by rating and scan for the first that fits, or to sort by size — both work, but both are $O(N \log N)$ for no benefit, and with $N$ up to $5 \times 10^4$ the single $O(N)$ pass is simply better. Nothing here needs order.

Equally, this is **not** a knapsack: Chef picks exactly one movie, so sizes do not combine and there is no packing decision. The word "single best" in the statement is what rules that out.

Sample case 3 is the discriminating one. The movies are $(1, 51)$, $(3, 100)$ and $(2, 50)$ with $X = 2$. The best rating overall is $100$, but that movie needs $3$ GB and does not fit; among those that do, the best is $51$. A solution ignoring the size filter would answer $100$.

Note the inclusive comparison: a movie of exactly $X$ GB fits.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, x = int(data[pos]), int(data[pos + 1])
        pos += 2
        best = 0
        for i in range(n):
            s, r = int(data[pos + 2 * i]), int(data[pos + 2 * i + 1])
            # Only movies that fit are candidates; exactly X GB still fits.
            if s <= x and r > best:
                best = r
        pos += 2 * n
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/arrays/IMDB.md](../docs/arrays/IMDB.md)
