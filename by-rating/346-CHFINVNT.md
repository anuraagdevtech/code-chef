# 346. Chef and Bulb Invention

> [`CHFINVNT`](https://www.codechef.com/problems/CHFINVNT) &middot; difficulty **1607** &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Counting residues below a threshold in closed form |
| **CodeChef tags** | `Mathematics`, `Basic Math`, `Arithmetic` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef is trying to invent the light bulb that can run at room temperature without electricity. So he has $N$ gases numbered from $0$ to $N - 1$ that he can use and he doesn't know which one of the $N$ gases will work but we do know it.

Now Chef has worked on multiple search algorithms to optimize search. For this project, he uses a modulo-based search algorithm that he invented himself. So first he chooses an integer $K$ and selects all indices $i$ in increasing order such that $i \bmod K = 0$ and test the gases on such indices, then all indices $i$ in increasing order such that $i \bmod K = 1$, and test the gases on such indices, and so on.

Given $N$, the index of the gas $p$ that will work, and $K$, find after how much time will he be able to give Chefland a new invention assuming that testing $1$ gas takes $1$ day.

For example, consider $N = 5, p = 2$ and $K = 3$.
- On the $1^{st}$ day, Chef tests gas numbered $0$ because $0 \bmod 3 = 0$.
- On the $2^{nd}$ day, Chef tests gas numbered $3$ because $3 \bmod 3 = 0$.
- On the $3^{rd}$ day, Chef tests gas numbered $1$ because $1 \bmod 3 = 1$.
- On the $4^{th}$ day, Chef tests gas numbered $4$ because $4 \bmod 3 = 1$.
- On the $5^{th}$ day, Chef tests gas numbered $2$ because $2 \bmod 3 = 2$.

So after $5$ days, Chef will be able to give Chefland a new invention

**Input**

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains three space-separated integers $N$, $p$, and $K$.

**Output**

For each test case, print a single line containing one integer — after how much time Chef will be able to give Chefland a new invention assuming that testing $1$ gas takes $1$ day.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N, K \leq 10^9$
- $0 \leq p < N$

**Subtasks**

**Subtask #1 (100 points):** Original constraints

## Sample

**Sample input**

```
4
10 5 5
10 6 5
10 4 5
10 8 5
```

**Sample output**

```
2
4
9
8
```

<details><summary>Explanation</summary>

**Test case $1$:** On the day $1$ Chef will test gas numbered $0$ and on the day $2$ Chef will test gas numbered $5$.

**Test case $2$:** On the day $1$ Chef will test gas numbered $0$, on the day $2$ Chef will test gas numbered $5$, on the day $3$ Chef will test gas numbered $1$, and on the day $4$ Chef will test gas numbered $6$.

**Test case $3$:** On the day $1$ Chef will test gas numbered $0$, on the day $2$ Chef will test gas numbered $5$, on the day $3$ Chef will test gas numbered $1$, on the day $4$ Chef will test gas numbered $6$, on the day $5$ Chef will test gas numbered $2$, on the day $6$ Chef will test gas numbered $7$, on the day $7$ Chef will test gas numbered $3$, on the day $8$ Chef will test gas numbered $8$, and on the day $9$ Chef will test gas numbered $4$.

**Test case $4$:** On the day $1$ Chef will test gas numbered $0$, on the day $2$ Chef will test gas numbered $5$, on the day $3$ Chef will test gas numbered $1$, on the day $4$ Chef will test gas numbered $6$, on the day $5$ Chef will test gas numbered $2$, on the day $6$ Chef will test gas numbered $7$, on the day $7$ Chef will test gas numbered $3$, and on the day $8$ Chef will test gas numbered $8$.

</details>

## Approach

The testing order groups indices by residue: first every $i \equiv 0$, then every $i \equiv 1$, and so on, each group in increasing order. So the day gas $p$ is tested is

$$\text{day} = \#\{\,i < N : i \bmod K < r\,\} \;+\; \left\lfloor \frac{p}{K} \right\rfloor + 1$$

where $r = p \bmod K$. The second term is $p$'s rank inside its own group — $p$ is the $(\lfloor p/K \rfloor + 1)$-th index with that residue — and the first counts everything tested in earlier groups.

That count cannot be summed group by group, since $K$ reaches $10^9$. Split $[0, N)$ into complete blocks of $K$ instead: with $q = \lfloor N/K \rfloor$ and $\rho = N \bmod K$, each complete block contributes exactly $r$ indices with residue below $r$, and the trailing partial block holds residues $0 \ldots \rho-1$, contributing $\min(r, \rho)$:

$$\#\{\,i < N : i \bmod K < r\,\} = qr + \min(r, \rho)$$

The $\min$ is the part that is easy to get wrong — the last block is short, so it may not contain all $r$ of the small residues.

Working through the statement's worked example, $N = 5$, $p = 2$, $K = 3$: $r = 2$, $q = 1$, $\rho = 2$, so earlier groups cover $1 \cdot 2 + 2 = 4$ indices and $p$ is first in its group, giving day $5$.

The samples show the ordering effect clearly: with $N = 10$ and $K = 5$, gas $5$ is tested on day $2$ (it is second in group $0$, after gas $0$), while gas $4$ waits until day $9$ because its residue group is last.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, p, k = (int(data[1 + 3 * i]), int(data[2 + 3 * i]), int(data[3 + 3 * i]))
        r = p % k
        full, tail = n // k, n % k
        # Each full block of K holds r small residues; the short tail may not.
        earlier = full * r + (r if r < tail else tail)
        out.append(str(earlier + p // k + 1))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/basic-math/CHFINVNT.md](../docs/basic-math/CHFINVNT.md)
