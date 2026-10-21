# 348. Bench Press

> [`BENCHP`](https://www.codechef.com/problems/BENCHP) &middot; difficulty **1611** &middot; time limit **1.5s** &middot; 1600 to 1800 difficulty problems (Level 3)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Frequency pairing for a symmetric load |
| **CodeChef tags** | `Data Structures`, `Arrays`, `Algorithms`, `Frequency Arrays`, `Greedy`, `Implementation` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

In the gym, Chef prefers to lift at least $W$ grams during a bench press and if that's impossible, Chef considers his workout to be incomplete and feels bad.

The rod weighs $W_r$ grams and there are $N$ other weights lying on the floor that weigh $w_1, w_2, ..., w_N$ grams. To maintain balance and to ensure that there is no unnecessary load due to torque, it's important that the weights added to the left side are symmetric to the weights added to the right side. It is not required to use all of the weights. It is also not required to use any weights at all, if Chef feels satisfied lifting only the rod.

For example:

 - $1$ $2$ $2$ $1$ $|$Rod Center$|$ $1$ $1$ $1$ $3$ is a wrong configuration, but

 - $1$ $2$ $3$ $1$ $|$Rod Center$|$ $1$ $3$ $2$ $1$ is a right configuration.

Find whether Chef will be able to collect the required weights to feel satisfied.

**Input**
- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- Each test case contains two lines of input.
- The first line contains three space-separated integers $N, W, W_r$.
- The second line contains $N$ space-separated integers $w_1, w_2, \ldots, w_N$.

**Output**
For each test case, output the answer in a single line: "YES" if Chef will be satisfied after his workout and "NO" if not (without quotes).

You may print each character of each string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

**Constraints**
- $1 \leq T \leq 10$
- $1 \leq N \leq 10^5$
- $1 \leq W \leq 2\cdot 10^5$
- $1 \leq w_i \leq 10^5$
- $1 \leq W_r \leq 2\cdot 10^4$

**Subtasks**
**Subtask #1 (30 points):** $w_i = 1$ for all valid $i$

**Subtask #2 (70 points):** original constraints

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 10^5$
- $1 \leq W \leq 2\cdot 10^5$
- $1 \leq w_i \leq 10^5$
- $1 \leq W_r \leq 2\cdot 10^4$

## Sample

**Sample input**

```
3
2 5 10 
2 2
7 100 50
100 10 10 10 10 10 90 
6 100 40 
10 10 10 10 10 10
```

**Sample output**

```
YES
NO
YES
```

<details><summary>Explanation</summary>

**Test case 1:** Since the weight of the rod is at least the required weight to be lifted, Chef will feel satisfied after the workout.

**Test case 2:** The configuration having maximum weight is:

$10$ $10$ $|$Rod Center$|$ $10$ $10$

So the maximum total weight Chef can lift is $50 + 4 \cdot 10 = 90$ which is less than the required amount to get satisfied.

**Test case 3:** The configuration having maximum weight is:

$10$ $10$ $10$ $|$Rod Center$|$ $10$ $10$ $10$

So the maximum total weight Chef can lift is $40 + 6\cdot 10 = 100$ which is equal to the required amount to get satisfied.

</details>

## Approach

Symmetry means the multiset of plates on the left equals the multiset on the right, so every plate used must be **matched by an identical twin**. A weight occurring $c$ times therefore contributes at most $\lfloor c/2 \rfloor$ matched pairs, and each pair adds $2w$ to the bar.

There is no trade-off to optimise: using more weight is never harmful, since the goal is only to reach $W$. So the maximum achievable load is

$$W_r + 2\sum_{w} \left\lfloor \frac{c_w}{2} \right\rfloor \cdot w$$

and the answer is `YES` exactly when that reaches $W$. The floor is where the odd leftovers vanish — a lone plate is dead weight, because putting it on one side would unbalance the bar.

The rod alone may already suffice, which is why no plates are required: sample 1 has $W_r = 10 \geq W = 5$, so the two $2$s are irrelevant.

Sample 2 is the odd-leftover trap. The plates are $100, 10 \times 5, 90$, and only the $10$s pair up — twice, since the fifth is stranded — so the best load is $50 + 2(2 \cdot 10) = 90$, short of $100$. Naively summing all plates would give $230$ and the wrong answer: the heavy $100$ and $90$ are unusable precisely because each is unique.

Sample 3 is the exact boundary: six $10$s give three pairs, so $40 + 60 = 100$ meets $W = 100$ — the requirement is *at least* $W$, so equality passes.

## Solution

```python
import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, want, rod = int(data[pos]), int(data[pos + 1]), int(data[pos + 2])
        counts = Counter(int(x) for x in data[pos + 3:pos + 3 + n])
        pos += 3 + n
        # Only matched twins can go on the bar; odd leftovers are dead weight.
        load = rod + 2 * sum(w * (c // 2) for w, c in counts.items())
        out.append("YES" if load >= want else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/greedy/BENCHP.md](../docs/greedy/BENCHP.md)
