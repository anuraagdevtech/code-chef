[&larr; 539. Galactik Football](539-GALACTIK.md) &middot; [Index](README.md) &middot; [541. Birthday Gift &rarr;](541-CHEFGIFT.md)

# 540. Physical Exercise

> [`PHCUL`](https://www.codechef.com/problems/PHCUL) &middot; difficulty **1865** &middot; time limit **2s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Geometry |
| **Technique** | Precomputed nearest finish, then all pairs in both visiting orders |
| **Complexity class** | Product of two sizes $O(n m)$ |
| **Time** | $O(N \cdot M + (N + M) \cdot K)$ per test case |
| **Space** | $O(N + M + K)$ |

## Question

Chef decided to exercise by running somewhere from ShareChat. He chose three sets of points in a plane:
- A set of $N$ points (numbered $1$ through $N$): for each valid $i$, the $i$-th of them has coordinates $(a_i, b_i)$.
- A set of $M$ points (numbered $1$ through $M$): for each valid $i$, the $i$-th of them has coordinates $(c_i, d_i)$.
- A set of $K$ points (numbered $1$ through $K$): for each valid $i$, the $i$-th of them has coordinates $(e_i, f_i)$.

ShareChat has coordinates $(x, y)$. Chef must choose one point $(a_j, b_j)$, one point $(c_k, d_k)$, and one point $(e_l, f_l)$. Then, he starts running from ShareChat, visits the chosen points $(a_j, b_j)$ and $(c_k, d_k)$ in any order, and then runs to the point $(e_l, f_l)$, where he finishes his run.

Help Chef find the minimum distance he has to run.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $x$ and $y$.
- The second line contains three space-separated integers $N$, $M$ and $K$.
- The third line contains $2N$ space-separated integers $a_1, b_1, a_2, b_2, \ldots, a_N, b_N$.
- The fourth line contains $2M$ space-separated integers $c_1, d_1, c_2, d_2, \ldots, c_M, d_M$.
- The fifth line contains $2K$ space-separated integers $e_1, f_1, e_2, f_2, \ldots, e_K, f_K$.

**Output**
For each test case, print a single line containing one real number ― the minimum distance.

Your answer will be considered correct if its absolute or relative error does not exceed $10^{-6}$.

**Constraints**
- $1 \le T \le 5,000$
- $1 \le N, M, K \le 5,000$
- $0 \le x, y \le 10^9$
- $0 \le a_i, b_i \le 10^9$ for each valid $i$
- $0 \le c_i, d_i \le 10^9$ for each valid $i$
- $0 \le e_i, f_i \le 10^9$ for each valid $i$
- the sum of $N+M+K$ over all test cases does not exceed $15,000$

**Subtasks**
**Subtask #1 (50 points):** $1 \le N, M, K \le 100$

**Subtask #2 (50 points):** original constraints

## Constraints

- $1 \le T \le 5,000$
- $1 \le N, M, K \le 5,000$
- $0 \le x, y \le 10^9$
- $0 \le a_i, b_i \le 10^9$ for each valid $i$
- $0 \le c_i, d_i \le 10^9$ for each valid $i$
- $0 \le e_i, f_i \le 10^9$ for each valid $i$
- the sum of $N+M+K$ over all test cases does not exceed $15,000$

## Sample

**Sample input**

```
2
1 4
3 2 2
4 4 2 0 8 1
10 1 3 1
1 3 9 5
6 4
2 2 3
7 10 5 7
1 6 2 3
1 8 0 7 0 2
```

**Sample output**

```
8.1820424980
8.6995968482
```

<details><summary>Explanation</summary>

**Example case 1:**

![](https://codechef_shared.s3.amazonaws.com/download/Images/NOV19/PHCUL/sample-1.jpg)

- The black point is ShareChat,
- Points from the first set are red.
- Points from the second set are green.
- Points from the third set are blue.
- The black line corresponds to Chef's run.

Chef should run from $(1, 4)$ to $(3, 1)$, then to $(2, 0)$ and then to $(1, 3)$. The distance is $\sqrt{13}+\sqrt{2}+\sqrt{10} \doteq 8.1820424980$.

**Example case 2:**

![](https://codechef_shared.s3.amazonaws.com/download/Images/NOV19/PHCUL/sample-2.jpg =240x303)

Chef should run from $(6, 4)$ to $(5, 7)$, then to $(1, 6)$ and then to $(0, 7)$. The distance is $\sqrt{10}+\sqrt{17}+\sqrt{2} \doteq 8.6995968482$.

</details>

## Approach

A run is start $\to$ first visited point $\to$ second visited point $\to$ finish, where the two middle points come one from each of the first two sets, in either order.

Once the last middle point is fixed, the finish point should simply be the one nearest to it. So precompute, for every point of the first two sets, its distance from ShareChat and its distance to the nearest point of the third set. Then enumerate every pair $(A_i, C_j)$ and take

$$|A_i C_j| + \min(\text{start}(A_i) + \text{end}(C_j),\; \text{start}(C_j) + \text{end}(A_i)).$$

The sum of $N \cdot M$ over tests is small enough for the quadratic enumeration.

## Solution

```python
import sys
from math import hypot


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        x, y = (next(tokens), next(tokens))
        n, m, k = (next(tokens), next(tokens), next(tokens))
        first = [(next(tokens), next(tokens)) for _ in range(n)]
        second = [(next(tokens), next(tokens)) for _ in range(m)]
        finish = [(next(tokens), next(tokens)) for _ in range(k)]
        start_to_first = [hypot(u - x, v - y) for u, v in first]
        start_to_second = [hypot(u - x, v - y) for u, v in second]
        first_to_finish = [min((hypot(u - r, v - s) for r, s in finish)) for u, v in first]
        second_to_finish = [min((hypot(u - r, v - s) for r, s in finish)) for u, v in second]
        best = float('inf')
        for i, (u, v) in enumerate(first):
            for j, (r, s) in enumerate(second):
                best = min(best, hypot(u - r, v - s) + min(start_to_first[i] + second_to_finish[j], start_to_second[j] + first_to_finish[i]))
        out.append('%.10f' % best)
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- Both visiting orders must be tried; the cheaper one depends on the geometry.
- Points may coincide with each other or with ShareChat, giving zero-length legs.
- The answer is a real number; ten decimals are printed and an error of $10^{-6}$ is tolerated.
- `math.hypot` avoids overflow and loss of precision in the squared distance.

## Dry run

Start $(0,0)$, first set $\{(1,0)\}$, second set $\{(2,0)\}$, finish set $\{(3,0)\}$.

Distances from the start: 1 and 2. Distances to the nearest finish: 2 and 1. The pair is 1 apart, so the two orders cost $1 + (1 + 1) = 3$ and $1 + (2 + 2) = 5$.

Answer `3.0000000000`.

---

Same problem grouped by topic: [../docs/geometry/PHCUL.md](../docs/geometry/PHCUL.md)
