# 1649 &middot; Minimise Maximum Subarray Sum

> CodeChef problem code [`MINIMISEMAX`](https://www.codechef.com/problems/MINIMISEMAX) &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Two independent lower bounds that are jointly attainable |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/greedy/MINIMISEMAX.md](../docs/greedy/MINIMISEMAX.md)

## Question

You are given two positive integers $X$ and $Y$.
Consider an array $A$ consisting of $X$ occurrences of $1$ and $Y$ occurrences of $-2$.

You can rearrange the elements of $A$ in any order.
Rearrange the elements to **minimize** the maximum sum over all subarrays of $A$.
Find the maximum subarray sum of such rearrangement of $A$.

**Input**

- The first line contains a single integer $T$, denoting the number of test cases.
- The only line of each test case contains two space-separated integers $X$ and $Y$, denoting the number of occurrences of $1$ and $-2$ respectively.

**Output**

For each test case, print the maximum sum of subarray if you rearrange $A$ optimally.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq X,Y \leq 10^6$

## Sample

**Sample input**

```
4
1 1
1 3
5 1
2 2
```

**Sample output**

```
1
1
3
1
```

<details><summary>Explanation</summary>

**Test case $1$:** Here either $A = [1,-2]$ or $A = [-2, 1]$. In both cases, maximum subarray sum is $1$.

**Test case $2$:** The array consists of one $1$ and three $-2$. Thus, maximum subarray sum would be $1$.

**Test case $3$:** Consider $A = [1, 1, -2, 1, 1, 1]$. The maximum subarray sum here is $3$.

</details>

## Approach

Two unavoidable costs bound the answer from below, and spreading the ones evenly meets both.

**The largest block.** The $Y$ copies of $-2$ cut the array into at most $Y+1$ maximal runs of ones, so some run holds at least $\lceil X/(Y+1) \rceil$ ones, and that run is itself a subarray.

**The whole array.** The full array is always a subarray, with sum $X - 2Y$ regardless of the order.

So the answer is at least $\max\bigl(\lceil \frac{X}{Y+1} \rceil,\; X - 2Y\bigr)$, and distributing the ones as evenly as possible — one $-2$ between consecutive runs — attains it. The reason is that taking $k$ consecutive runs yields roughly $kq - 2(k-1) = k(q-2) + 2$ where $q = \lfloor X/(Y+1) \rfloor$, which is **linear in $k$**: it is maximised at $k = 1$ or at $k = Y+1$, the two bounds above. No intermediate $k$ can beat them.

Clustering the $-2$s never helps, since it reduces the number of runs and so enlarges the biggest one.

$$\text{answer} = \max\!\left(\left\lceil \frac{X}{Y+1} \right\rceil,\; X - 2Y\right)$$

The samples land on each bound. $X = 5, Y = 1$ gives $\max(3, 3) = 3$, where the two bounds coincide — the arrangement $1\,1\,1\,{-2}\,1\,1$ has a block of three and a total of three. $X = 2, Y = 2$ gives $\max(1, -2) = 1$ via $1\,{-2}\,1\,{-2}$, and $X = 1$ with either $Y$ gives $1$, since a single $1$ is always a subarray.

The answer is never below $1$ because $X \geq 1$, so the empty-subarray convention never comes into play.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Biggest run of ones, versus the whole array's fixed sum.
        block = -(-x // (y + 1))
        whole = x - 2 * y
        out.append(str(block if block > whole else whole))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
