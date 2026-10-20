# 165. Chef and Spells

> CodeChef problem code [`CHFSPL`](https://www.codechef.com/problems/CHFSPL) &middot; difficulty **965** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Total minus the extremum |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | Level up from 1* to 2* (Level 2) |

## Question

Chef has three spells. Their powers are $A$, $B$, and $C$ respectively. Initially, Chef has $0$ hit points, and if he uses a spell with power $P$, then his number of hit points increases by $P$.

Before going to sleep, Chef wants to use exactly two spells out of these three. Find the maximum number of hit points Chef can have after using the spells.

**Input**

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains three space-separated integers $A$, $B$, and $C$.

**Output**

For each test case, print a single line containing one integer — the maximum number of hit points.

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq A, B, C \leq 10^8$

**Subtasks**

**Subtask #1 (100 points):** original constraints

## Sample

**Sample input**

```
2
4 2 8
10 14 18
```

**Sample output**

```
12
32
```

<details><summary>Explanation</summary>

**Example case 1:** Chef has three possible options:
- Use the first and second spell and have $4 + 2 = 6$ hitpoints.
- Use the second and third spell and have $2 + 8 = 10$ hitpoints.
- Use the first and third spell and have $4 + 8 = 12$ hitpoints.

Chef should choose the third option and use the spells with power $4$ and $8$ to have $12$ hitpoints.

**Example case 2:** Chef should use the spells with power $14$ and $18$.

</details>

## Approach

Chef casts exactly two of the three spells and wants the largest total, so he drops the weakest:

$$A + B + C - \min(A, B, C)$$

Phrasing it as "total minus the minimum" rather than "sum of the two largest" keeps it to two cheap passes and avoids sorting or a top-two scan. It is the same shape as the discus and sale problems, and it generalises directly to picking $n-1$ of $n$ items.

Ties need no special handling: `min` returns the value once, so if two spells share the lowest power only one copy is dropped. With powers $5, 5, 9$ the answer is $14$, not $9$.

Note the word **exactly** — Chef must use two spells, not "at most two". Since all powers are positive that distinction never bites here, because using more is always better. It would matter if negative powers were allowed, where the best "at most two" choice might be to cast nothing.

Sample case 1 drops the $2$ from $\{4, 2, 8\}$ for $12$; case 2 drops the $10$ for $32$.

Powers reach $10^8$, so the sum of two reaches $2 \times 10^8$ — inside 32 bits, but worth a glance in a fixed-width language.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        p = list(map(int, data[1 + 3 * i:4 + 3 * i]))
        # Use two of three: drop the weakest, once, even if tied.
        out.append(str(sum(p) - min(p)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
