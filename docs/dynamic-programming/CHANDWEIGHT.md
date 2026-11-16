[&larr; 703. Merging Binary Strings](MERGEBS.md) &middot; [Index](../../README.md) &middot; [725. Two Counters &rarr;](TWOCOUNTERS.md)

# 716. Chandelier

> CodeChef problem code [`CHANDWEIGHT`](https://www.codechef.com/problems/CHANDWEIGHT) &middot; difficulty **2368** &middot; time limit **2s**

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Requirements propagated outwards from the first support that breaks |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

A linear chandelier is held up by $N$ supports. The $i^{th}$ support initially holds up a weight $W_i$, and will collapse if the weight on it is **more than or equal to** $A_i$. Note that initially, $W_i \lt A_i$ for all $1 \le i \le N$.

Whenever $W_i\ge A_i$ for some support, the following happens:

- The $i^{th}$ support is destroyed;
- Let $x$ and $y$ be uniformly random non-negative integers such that $x+y=W_i$.
Add $x$ to $W_{i-1}$ and add $y$ to $W_{i+1}$.

Note that:
- If either one of the neighbours do not exist, all the weight is added to the remaining neighbour.
- If both neighbours do not exist, the weight dissipates.

For all $1 \le i \le N$, find the **minimum** weight you need to add to $W_i$, so that there is a nonzero chance all supports end up destroyed.

**Input**

- The first line of input contains a single integer $T$, denoting the number of test cases.
- The first line of each test case contains $N$, the number of supports.
- The second line of each test case contains $N$ integers $W_1, W_2, \ldots, W_N$, denoting initial weight on  each support.
- The third line of each test case contains $N$ integers $A_1, A_2, \ldots, A_N$, denoting the minimum load at which a support destroys.

**Output**

For each test, output $N$ space-separated integers. The $i^{th}$ of these should be the **minimum weight** you need to add to the $i^{th}$ chandelier, so that there is a nonzero chance that all supports end up destroyed.

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 3\cdot 10^5$
- $1 \leq W_i \lt A_i \leq 10^9$
- The sum of $N$ over all test cases does not exceed $3\cdot 10^5$.

## Sample

**Sample input**

```
4
3
1 1 1
2 2 2
1
1
1000000000
2
1 1234
2 5678
7
122 179 269 184 250 104 455
398 203 318 340 312 489 464
```

**Sample output**

```
1 1 1
999999999
4443 4444
276 146 49 156 291 385 9
```

<details><summary>Explanation</summary>

**Test case $1$:** The following is possible if we add weight $1$ to support $2$:
- Support $2$ collapses, since $W_2=2\ge 2$. A weight $x=1$ gets added to $W_1$, and a weight $y=1$ gets added to $W_3$.
- Support $1$ collapses, since $W_1=2\ge 2$.
- Support $3$ collapses, since $W_3=2\ge 2$.

If we add zero weight, then nothing would happen and all supports would stay standing. So the answer for $i=2$ is $1$.

**Test case $2$:** We have to add $999999999$ weight to the only support to make it collapse.

**Test case $3$:** Note that we could add a weight of $1$ to support $1$ to make it collapse, but then, there would be no way to make the second support collapse. We can show that we have to add at least $4443$ weight to support $1$ to make it possible for both supports to end up destroyed.

</details>

## Approach

Suppose weight is added to support $i$ until it collapses. Its load is then split between its neighbours in some way, and since we only need a non-zero chance, we may pick the most favourable split at every collapse. After support $i$ is gone, the supports to its left and to its right no longer interact: anything a collapsing support sends towards an already destroyed neighbour is lost.

So define `left_need[j]` as the weight that has to arrive, from the right, on support $j - 1$ in order to destroy all of the supports $0 \dots j - 1$. Support $j - 1$ must reach its limit, and it must also hold at least what the supports further left need, because it passes that on when it collapses:

$$\text{left\_need}[j + 1] = \max(A_j,\; \text{left\_need}[j]) - W_j .$$

`right_need` is defined symmetrically from the other end.

If the added weight goes to support $i$, its final load must be at least its own limit and at least the sum of what the two sides need, so the answer for $i$ is

$$\max\bigl(A_i,\; \text{left\_need}[i] + \text{right\_need}[i + 1]\bigr) - W_i .$$

## Solution (Python)

```python
import sys


def solve(tokens):
    n = next(tokens)
    weight = [next(tokens) for _ in range(n)]
    limit = [next(tokens) for _ in range(n)]
    left_need = [0] * (n + 1)
    right_need = [0] * (n + 1)
    for i in range(n):
        left_need[i + 1] = max(limit[i], left_need[i]) - weight[i]
    for i in range(n - 1, -1, -1):
        right_need[i] = max(limit[i], right_need[i + 1]) - weight[i]
    return ' '.join((str(max(limit[i], left_need[i] + right_need[i + 1]) - weight[i]) for i in range(n)))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- A single support just needs $A_1 - W_1$.
- The end supports have an empty side whose need is 0.
- The needs are never negative, since $W_j < A_j$ makes every term at least 1.
- Values reach about $N \cdot 10^9$.

## Dry run

`W = [1, 1234]`, `A = [2, 5678]`.

`left_need`: `[0, 1, 4444]`, from $\max(2, 0) - 1 = 1$ and $\max(5678, 1) - 1234 = 4444$. `right_need`: `[4443, 4444, 0]`, from $\max(5678, 0) - 1234 = 4444$ and $\max(2, 4444) - 1 = 4443$.

- support 1: $\max(2,\; 0 + 4444) - 1 = 4443$
- support 2: $\max(5678,\; 1 + 0) - 1234 = 4444$

Output `4443 4444`.

---

Same problem in rating order (#680 of 735): [../../by-rating/680-CHANDWEIGHT.md](../../by-rating/680-CHANDWEIGHT.md)
