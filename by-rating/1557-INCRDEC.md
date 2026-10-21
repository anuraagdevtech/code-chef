# 1557 &middot; Increasing Decreasing

> CodeChef problem code [`INCRDEC`](https://www.codechef.com/problems/INCRDEC) &middot; time limit **1s** &middot; Jump from 2* to 3* (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Multiplicity bounds for a bitonic arrangement |
| **CodeChef category** | main |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |

Same write-up grouped by topic: [../docs/constructive/INCRDEC.md](../docs/constructive/INCRDEC.md)

## Question

Chef received a new sequence $A_1, A_2, \ldots, A_N$. He does not like arbitrarily ordered sequences, so he wants to permute the elements of $A$ in such a way that it would satisfy the following condition: there is an integer $p$ ($1 \le p \le N$) such that the first $p$ elements of the new (permuted) sequence are strictly increasing and the last $N-p+1$ elements are strictly decreasing.

Help Chef and find a permutation of the given sequence which satisfies this condition or determine that no such permutation exists. If there are multiple solutions, you may find any one.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

### Output
For each test case:
- If there is no permutation of $A$ that satisfies the given condition, print a single line containing the string `"NO"` (without quotes).
- Otherwise, print two lines.
- The first of these lines should contain the string `"YES"` (without quotes).
- The second line should contain $N$ space-separated integers ― the elements of your permuted sequence.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 10^5$
- $1 \le A_i \le 2 \cdot 10^5$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $10^6$

### Subtasks
**Subtask #1 (50 points):**
- $N \le 10^3$
- $A_i \le 2 \cdot 10^3$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $10^4$

**Subtask #2 (50 points):** original constraints

## Constraints

- $1 \le T \le 100$
- $1 \le N \le 10^5$
- $1 \le A_i \le 2 \cdot 10^5$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $10^6$

## Sample

**Sample input**

```
5
4
1 3 2 4
4
1 3 2 4
6
1 10 10 10 20 15
5
1 1 2 2 3
4
1 2 3 3
```

**Sample output**

```
YES
1 2 3 4
YES
4 3 2 1
NO
YES
1 2 3 2 1
NO
```

## Approach

The target shape is a single peak: $a_1 < \cdots < a_p > a_{p+1} > \cdots > a_N$. Both arms are **strictly** monotone, so each arm uses any value at most once, and the peak belongs to both arms. That pins down feasibility entirely:

- every value occurs **at most twice** — once on the way up, once on the way down;
- the **maximum** occurs **exactly once** — it must be the peak, since every other position is strictly below its neighbour toward the peak.

Those two conditions are also sufficient, and the construction reads straight off them. Sort the distinct values ascending to form the ascending arm; then let the descending arm be the values with multiplicity two, in descending order:

$$[\,v_1,\, v_2,\, \ldots,\, v_m,\ \underbrace{\ldots}_{\text{doubled values, descending}}\,]$$

The ascending arm is strictly increasing because the $v_i$ are distinct, and the descending arm is strictly decreasing for the same reason. The join is strict because the maximum $v_m$ is unique, so the first element of the descending arm is strictly below it — which is exactly why the "maximum occurs once" condition is needed and not merely convenient.

The samples cover each failure mode. $[1,10,10,10,20,15]$ fails on multiplicity three. $[1,2,3,3]$ has all counts at most two but the maximum $3$ doubled, so no legal peak exists. $[1,1,2,2,3]$ satisfies both and yields `1 2 3 2 1`.

Note the first two samples are the identical input printed twice, with the expected outputs `1 2 3 4` and `4 3 2 1` — both valid, since $p$ may be $N$ (an empty descending arm) or $1$ (an empty ascending arm). Our construction always produces the former shape when every value is distinct.

## Solution (Python)

```python
import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        counts = Counter(int(x) for x in data[pos + 1:pos + 1 + n])
        pos += 1 + n
        top = max(counts)
        # Two arms, so twice is the ceiling; the peak cannot be shared.
        if max(counts.values()) > 2 or counts[top] != 1:
            out.append("NO")
            continue
        values = sorted(counts)
        doubled = [v for v in reversed(values) if counts[v] == 2]
        out.append("YES")
        out.append(" ".join(map(str, values + doubled)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N \log N)$ per test case
- **Space:** $O(N)$
