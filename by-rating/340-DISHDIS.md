# 340. Dish Distribution

> [`DISHDIS`](https://www.codechef.com/problems/DISHDIS) &middot; difficulty **1596** &middot; time limit **0.5s** &middot; Jump from 2* to 3* (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Bounded compositions via a prefix-sum convolution |
| **Complexity class** | Product of two sizes $O(n m)$ |
| **Time** | $O(nm)$ per test case |
| **Space** | $O(n)$ |

## Question

Chef feels that being the Head Chef is a very difficult job. More than cooking, managing the kitchen and distributing the work between various cooks proves to be a tiring task. There are many dishes to be prepared. And he has a team of talented cooks to do this for him. But the Chef always has a problem distributing tasks among them. For a cook i, the Chef wants to give him *atleast* xi dishes to prepare in a day. But different cooks have different capacities. Any cook i can cook *atmost* yi number of dishes in a single day. Chef is very aware of every cook's capability and will not give anyone more work than his maximum capacity. Now, he wants you to help him out here.

Your task will be simple: Tell him the number of ways in which he can distribute the given number of dishes among his team.

**Input:**

First line contains T, number of tests.
Each test begins with a single line containing 2 space separated integers: n and m, the number of dishes to be prepared and the number of cooks in Chef's team.

Then follow m lines. The ith line contains 2 space separater integers which are the corresponding xi and yi.

**Output:**

For every test case, output a single integer: the number of ways of distributing the work mod 1000000007.

**Constraints:**

1<=T<=50

1<=n,m<=100

0<=xi,yi<=100

## Constraints

1<=T<=50
1<=n,m<=100
0<=xi,yi<=100

## Sample

**Sample input**

```
1
3 2
0 3
1 3
```

**Sample output**

```
3
```

<details><summary>Explanation</summary>

**Test case $1$:** Chef can distribute the dishes in the following three ways:
- $0$ dishes for the first cook and $3$ dishes for the second cook.
- $1$ dish for the first cook and $2$ dishes for the second cook.
- $2$ dishes for the first cook and $1$ dish for the second cook.

</details>

## Approach

The dishes are indistinguishable, so a distribution is a tuple $(d_1, \ldots, d_m)$ with $x_i \leq d_i \leq y_i$ and $\sum d_i = n$ — a **bounded composition** of $n$. Processing cooks one at a time gives

$$\mathrm{dp}_i[j] = \sum_{d = x_i}^{\min(y_i,\, j)} \mathrm{dp}_{i-1}[j - d]$$

with $\mathrm{dp}_0[0] = 1$. Done literally this is $O(nm \cdot 101)$ per test, and with $T = 50$ that is tens of millions of operations for no reason.

The inner sum is a **contiguous window** of the previous row, so one prefix-sum array $P[j] = \sum_{u \leq j} \mathrm{dp}_{i-1}[u]$ collapses it to a subtraction:

$$\mathrm{dp}_i[j] = P[j - x_i] - P[j - y_i - 1]$$

treating out-of-range indices as $0$. Each cook is then $O(n)$ and the whole test $O(nm)$. Doing the subtraction under the modulus can go negative, so add $\mathrm{MOD}$ before reducing.

One edge case the bounds permit: $x_i$ and $y_i$ are independent, so a cook may have $x_i > y_i$ — an empty range, making the answer $0$ outright. Also $x_i$ may be $0$, so a cook can be given nothing.

The sample has $n = 3$ with ranges $[0,3]$ and $[1,3]$. The three distributions are $(0,3)$, $(1,2)$ and $(2,1)$; $(3,0)$ is excluded because the second cook must receive at least one dish. Note that *every* dish must be handed out — the count is of distributions summing to exactly $n$, not at most $n$.

## Solution

```python
import sys

MOD = 1_000_000_007


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m = int(data[pos]), int(data[pos + 1])
        pos += 2
        ranges = [(int(data[pos + 2 * i]), int(data[pos + 2 * i + 1])) for i in range(m)]
        pos += 2 * m
        dp = [0] * (n + 1)
        dp[0] = 1
        for lo, hi in ranges:
            if lo > hi:                 # an empty range admits nothing
                dp = [0] * (n + 1)
                break
            pref = [0] * (n + 2)
            for j in range(n + 1):
                pref[j + 1] = (pref[j] + dp[j]) % MOD
            nxt = [0] * (n + 1)
            for j in range(n + 1):
                # Window [j - hi, j - lo] of the previous row.
                top = j - lo
                if top < 0:
                    continue
                bottom = j - hi
                if bottom < 0:
                    bottom = 0
                nxt[j] = (pref[top + 1] - pref[bottom]) % MOD
            dp = nxt
        out.append(str(dp[n] % MOD))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **A prefix sum turns the inner loop from $O(n)$ into $O(1)$.** The transition sums the previous row over the window $[j - y_i,\, j - x_i]$, and without the prefix array the DP would be $O(nm \cdot n)$.
- **The window must be clipped at zero**, since $j - y_i$ can be negative — and skipped entirely when $j - x_i < 0$, which means cook $i$ cannot even meet their minimum.
- **An empty range ($x_i > y_i$) admits nothing**, so the whole count collapses to $0$; the explicit check avoids relying on the window arithmetic to produce it.
- **$x_i$ may be $0$**, letting a cook take nothing — the sample's first cook has a minimum of $0$.
- **Only $dp[n]$ is read at the end**, so distributions that use fewer than $n$ dishes are correctly excluded.
- **The modular subtraction needs a final `%`**, because `pref[top+1] - pref[bottom]` can be negative after reduction.
- **$n, m \leq 100$** keeps the table at $10^4$ transitions per case, trivial at $T \leq 50$.

## Dry run

Sample: $n = 3$ dishes, cooks with ranges $[0,3]$ and $[1,3]$.

| cook 1 takes | cook 2 takes | valid? |
|---:|---:|:---:|
| 0 | 3 | yes |
| 1 | 2 | yes |
| 2 | 1 | yes |
| 3 | 0 | **no** (below cook 2's minimum of 1) |

Output `3`.

---

Same problem grouped by topic: [../docs/dynamic-programming/DISHDIS.md](../docs/dynamic-programming/DISHDIS.md)
