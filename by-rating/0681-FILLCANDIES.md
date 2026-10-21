# 681 &middot; Fill Candies

> CodeChef problem code [`FILLCANDIES`](https://www.codechef.com/problems/FILLCANDIES) &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Ceiling division by a composite capacity |
| **CodeChef tags** | `Mathematics`, `Basic Math` |
| **CodeChef category** | school |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/basic-math/FILLCANDIES.md](../docs/basic-math/FILLCANDIES.md)

## Question

Chef received $N$ candies on his birthday. He wants to put these candies in some bags. A bag has $K$ pockets and each pocket can hold at most $M$ candies. Find the **minimum** number of bags Chef needs so that he can put every candy into a bag.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line containing three space-separated integers $N, K, M$.

**Output**

For each test case, print the minimum number of bags Chef needs so that he can put all the candies in one of the bags.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N, K, M \leq 100$

## Sample

**Sample input**

```
4
6 2 3
3 1 2
8 4 1
25 4 2
```

**Sample output**

```
1
2
2
4
```

<details><summary>Explanation</summary>

**Test case $1$:** Chef puts $3$ candies in the first pocket of a bag and the remaining $3$ candies in the second pocket. Thus Chef will need only one bag.

**Test case $2$:** Chef puts $2$ candies in the only pocket of the first bag and the remaining $1$ candy in the only pocket of the second bag. Thus Chef will need two bags.

**Test case $3$:** Chef puts $4$ candies in the first bag, one candy in each of the $4$ pockets and the same for the second bag. Thus Chef will need two bags.

**Test case $4$:** Chef puts $2$ candies in each of the $4$ pockets of three bags, one candy in a pocket of the fourth bag.

</details>

## Approach

Work out the capacity of one bag first. It has $K$ pockets and each pocket takes at most $M$ candies, so a bag holds $K \cdot M$. Every candy must be placed and bags cannot be split, so the count rounds up:

$$\left\lceil \frac{N}{K \cdot M} \right\rceil$$

written in integers as `(n + k * m - 1) // (k * m)`.

Composing the capacity before dividing is the key move. Dividing by $K$ and then by $M$ in two steps is *not* equivalent once rounding enters — each step would round separately and inflate the result. With $N = 25, K = 4, M = 2$ the correct answer is $\lceil 25/8 \rceil = 4$, whereas rounding up at each stage gives $\lceil \lceil 25/2 \rceil / 4 \rceil = \lceil 13/4 \rceil = 4$ here but diverges on other inputs. Collapsing to a single division by $KM$ avoids the question entirely.

It is also worth seeing that the pockets impose no extra constraint. Candies are interchangeable and may be spread freely across pockets, so a bag is simply a container of size $KM$; nothing is wasted by an awkward split. Had each pocket needed to be filled completely, or had candies come in indivisible groups, the pocket structure would have mattered.

Sample case 2 is the ragged one: $3$ candies into bags of capacity $2$ needs $2$ bags, the second holding a single candy.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, k, m = map(int, data[1 + 3 * i:4 + 3 * i])
        cap = k * m          # compose the capacity, then round up once
        out.append(str((n + cap - 1) // cap))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
