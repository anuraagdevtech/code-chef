# 60. Airlines

> CodeChef problem code [`SPCP2`](https://www.codechef.com/problems/SPCP2) &middot; difficulty **712** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Ceiling division with a clamp |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

An airline operates $X$ aircraft every day. Each aircraft can carry up to $100$ passengers.
One day, $N$ passengers would like to travel to the same destination. What is the minimum number of new planes that the airline must buy to carry all $N$ passengers?

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line containing two space-separated integers $X$ and $N$ — the number of aircraft the airline owns and the number of passengers travelling, respectively.

**Output**

- For each test case, output the minimum number of planes the airline needs to purchase.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X \leq 10^6$
- $1 \leq N \leq 10^6$

**Subtasks**

- **Subtask 1 (10 points):** $1 \leq M \leq 10$
- **Subtask 2 (20 points):** The sum of $N$ across all test cases won't exceed $20$.
- **Subtask 3 (70 points):** No further constraints.

## Sample

**Sample input**

```
3
4 600
3 523
8 245
```

**Sample output**

```
2
3
0
```

<details><summary>Explanation</summary>

**Test case $1$:** The airline needs at least $6$ planes to carry $600$ passengers. They already have $4$, so they must purchase $2$ more.

**Test case $2$:** The airline needs at least $6$ planes to carry $523$ passengers. They already have $3$, so they must purchase $3$ more.

**Test case $3$:** The airline needs at least $3$ planes to carry $245$ passengers. They already have $8$, so there's no need to purchase any more.

</details>

## Approach

Each aircraft seats $100$ passengers, so carrying $N$ people needs

$$\left\lceil \frac{N}{100} \right\rceil$$

planes in total — the leftover passengers still need a whole aircraft, so this rounds up. The airline already owns $X$, so it must buy the shortfall:

$$\max\left(0,\; \left\lceil \frac{N}{100} \right\rceil - X\right)$$

Both operations are load-bearing. The ceiling handles sample case 2, where $523$ passengers need $6$ planes rather than $5$ — the final plane carries just $23$ people. The clamp handles sample case 3, where $245$ passengers need $3$ planes but the airline already has $8$; the answer is $0$, not a negative number. Surplus aircraft cannot be un-bought.

This is the same clamp-after-ceiling shape as the chess-ratings and candy-packet problems, and the ordering matters for the same reason: computing `n // 100 - x` and then rounding would mix the two roundings together. Resolve the requirement first, compare against stock second.

In integers the ceiling is `(n + 99) // 100`.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, n = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        needed = (n + 99) // 100      # a part-full plane still flies
        out.append(str(max(0, needed - x)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
