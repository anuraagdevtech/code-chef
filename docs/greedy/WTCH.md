# 374. The Nights Watch

> CodeChef problem code [`WTCH`](https://www.codechef.com/problems/WTCH) &middot; difficulty **1441** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Leftmost-feasible placement |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

## Question

There are $N$ watchtowers built in a row. Each watchtower can only accommodate one person. Some of them are already occupied by members of the Night's Watch. Since the members of the Night's Watch do not get along, no two consecutive towers can be occupied at any moment.

Arya heard that the wildlings are planning an attack. She is not satisfied by the current security, so she plans to place more members of the Night's Watch in the empty towers. What is the maximum number of people she can place in the towers such that no two consecutive towers are occupied afterwards? Note that Arya may not remove anyone from already occupied towers.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The next line contains a single string $S$ with length $N$. For each valid $i$, the $i$-th character of this string is '1' if the $i$-th watchtower is initially occupied or '0' if it is empty.

**Output**
For each test case, print a single line containing one integer — the maximum number of people Arya can place in the towers.

**Constraints**
- $1 \le T \le 1,000$
- $1 \le N \le 10^6$
- $S$ contains only characters '0' and '1'
- initially, no two consecutive towers are occupied
- the sum of $N$ over all test cases does not exceed $10^6$

**Subtasks**
**Subtask #1 (20 points):** initially, all towers are empty

**Subtask #2 (80 points):** original constraints

## Constraints

- $1 \le T \le 1,000$
- $1 \le N \le 10^6$
- $S$ contains only characters '0' and '1'
- initially, no two consecutive towers are occupied
- the sum of $N$ over all test cases does not exceed $10^6$

## Sample

**Sample input**

```
2
6
010001
11
00101010000
```

**Sample output**

```
1
3
```

## Approach

Scan left to right and occupy a tower the moment it is legal — empty, with both neighbours empty. This leftmost-feasible greedy is optimal, and the exchange argument is short: if an optimal solution skips the first legal position $i$, it must leave $i$ free, and it can hold at most one occupant among $\{i, i+1\}$. Replacing that occupant (if any) with $i$ keeps the arrangement valid, since $i-1$ was already free, and does not reduce the count. Repeating pushes any optimum into the greedy's shape.

Placing as early as possible is what matters: a person at $i$ blocks only $i+1$ going forward, whereas a person at $i+1$ blocks $i+2$ as well, so the greedy never costs a later opportunity.

The implementation detail that matters is checking the **already-updated** left neighbour and the **original** right neighbour. Since the greedy writes its placements back into the string as it goes, a single array read handles both — but it means the string must be mutable, so the input is copied into a `bytearray`.

The guarantee that no two towers are initially adjacent means the starting configuration is already valid, so the greedy never has to repair anything.

In `010001` only index $3$ (0-based) qualifies: index $0$ is blocked by the occupant at $1$, and index $4$ is blocked by the occupant at $5$ — and after placing at $3$, index $4$ is doubly blocked. Hence $1$.

In `00101010000` the answer is $3$: index $0$ (its right neighbour being free), then the long tail `0000` at the end, which admits indices $8$ and $10$ — placing at $8$ rather than $9$ is exactly what leaves room for $10$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + 2 * i])
        towers = bytearray(data[2 + 2 * i])
        placed = 0
        for j in range(n):
            # Placing as early as legal never blocks a later opportunity.
            if towers[j] == 0x30 \
                    and (j == 0 or towers[j - 1] == 0x30) \
                    and (j == n - 1 or towers[j + 1] == 0x30):
                towers[j] = 0x31
                placed += 1
        out.append(str(placed))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
