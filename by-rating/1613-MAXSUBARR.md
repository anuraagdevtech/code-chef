# 1613 &middot; Maximum Subarray 

> CodeChef problem code [`MAXSUBARR`](https://www.codechef.com/problems/MAXSUBARR) &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Kadane plus a freely orderable block |
| **CodeChef tags** | `Data Structures`, `Mathematics`, `Algorithms`, `Greedy`, `Arrays`, `Basic Math`, `Kadane Algorithm` |
| **CodeChef category** | easy |
| **Time** | $O(N + M)$ per test case |
| **Space** | $O(N + M)$ |

Same write-up grouped by topic: [../docs/greedy/MAXSUBARR.md](../docs/greedy/MAXSUBARR.md)

## Question

Given two arrays $A$ and $B$ of sizes $N$ and $M$ respectively. You can apply the following operation until the array $B$ is non-empty:
- Choose either the **first** or the **last** element of array $B$.
- Insert the chosen element to either the **front** or the **back** of array $A$.
- Delete the chosen element from array $B$.

For example, let $A = [9, 7]$ and $B = [1, 3, 2]$. In one operation, we can choose either $X = 1$ or $X = 2$ (first or last element of array $B$). We can insert $X$ in array $A$ and make it either $A = [X, 9, 7]$ or $A = [9, 7, X]$. The chosen $X$ is deleted from array $B$. Thus, it will become either $B = [3, 2]$ (when chosen $X$ is $1$) or $B = [1, 3]$ (when chosen $X$ is $2$).

Find the **maximum sum** of any subarray of the array $A$ that you can achieve after performing exactly $M$ operations.

Note: A subarray of an array is formed by deleting some (possibly zero) elements from the beginning of the array and some (possible zero) elements from the end of the array. A subarray can be empty as well.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of $4$ lines of input.
    - The first line of each test contains a single integer $N$, the size of array $A$.
    - The next line contains $N$ space-separated integers, denoting elements of array $A$.
    - The third line of each test contains a single integer $M$, the size of array $B$.
    - The next line contains $M$ space-separated integers, denoting elements of array $B$.

**Output**

For each test case, output on a new line the **maximum sum** of any subarray of the array $A$ that you can achieve after performing exactly $M$ operations.

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 10^5$
- $1 \leq M \leq 10^5$
- $-10^8 \leq A_i, B_i \leq 10^8$

## Sample

**Sample input**

```
3
5
3 26 -79 72 23
2
66 44
1
81
1
-97
5
10 -5 14 -20 4
3
-10 5 -2
```

**Sample output**

```
205
81
24
```

<details><summary>Explanation</summary>

**Test case $1$:**
- Operation $1$: Add the first element of array $B$ to the back of array $A$. Thus, $A = [3, 26, -79, 72, 23, 66]$ and $B = [44]$.
- Operation $2$: Add the first element of array $B$ to the back of array $A$. Thus, $A = [3, 26, -79, 72, 23, 66, 44]$ and $B = []$.

The, maximum sum subarray of array $A$ is $[72, 23, 66, 44]$ having sum $72+23+66+44=205$.

**Test case $2$:**
- Operation $1$: Add the first element of array $B$ to the front of array $A$. Thus, $A = [-97, 81]$ and $B = []$.

The, maximum sum subarray of array $A$ is $[81]$ having sum $81$.

**Test case $3$:**
- Operation $1$: Add the last element of array $B$ to the back of array $A$. Thus, $A = [10, -5, 14, -20, 4, -2]$ and $B = [-10, 5]$.
- Operation $2$: Add the last element of array $B$ to the front of array $A$. Thus, $A = [5, 10, -5, 14, -20, 4, -2]$ and $B = [-10]$.
- Operation $3$: Add the first element of array $B$ to the front of array $A$. Thus, $A = [-10, 5, 10, -5, 14, -20, 4, -2]$ and $B = []$.

The, maximum sum subarray of array $A$ is $[5, 10, -5, 14]$ having sum $5+10-5+14 = 24$.

</details>

## Approach

The operations look restrictive, but two observations dissolve them.

First, **any element of $B$ can be made adjacent to $A$**. To use a middle element of $B$, peel the elements in front of it off and push them onto the *front* of $A$, then push the one you want onto the back. So the block of $B$-elements sitting immediately to the right of $A$ can be any subset of $B$, and the unwanted ones are parked on the other side, outside the subarray.

Second, **order within that block is irrelevant** — only its sum enters the answer. So the best block is simply all the positive elements of $B$:

$$P = \sum_{b \in B,\ b > 0} b$$

A chosen subarray of the final array is then one of three shapes: entirely inside $A$; a suffix of $A$ extended rightwards into the appended block; or a prefix of $A$ extended leftwards into the prepended block. (Spanning both sides is covered, since all of $A$ is itself a suffix of $A$, and the positives can all go to one end.) Hence

$$\text{answer} = \max\bigl(\mathrm{kadane}(A),\ P + \max(0, \mathrm{maxSuffix}(A)),\ P + \max(0, \mathrm{maxPrefix}(A))\bigr)$$

The empty subarray is allowed, so every term is floored at $0$ and the answer is never negative. Taking $P$ alone — an empty suffix — covers the case where the $B$-block beats everything in $A$.

Sample 1 shows the suffix branch winning: $A = [3,26,-79,72,23]$ has best suffix $95$ and $P = 110$, giving $205$, well above Kadane's $95$. Sample 3 shows the prefix branch: the best prefix $10 - 5 + 14 = 19$ plus $P = 5$ gives $24$, beating the suffix route's $4 + 5$. And sample 2 has $B = [-97]$, so $P = 0$ and the answer is just $A$ itself — note that all $M$ operations still happen, but the unwanted element is parked where it cannot hurt.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = [int(x) for x in data[pos + 1:pos + 1 + n]]
        m = int(data[pos + 1 + n])
        pos += 2 + n
        # Order inside the appended block never matters, only its sum.
        gain = sum(v for v in (int(x) for x in data[pos:pos + m]) if v > 0)
        pos += m

        best = run = 0
        for v in a:                       # Kadane, empty subarray allowed
            run = max(0, run + v)
            best = max(best, run)
        total = 0
        best_pre = 0
        for v in a:
            total += v
            best_pre = max(best_pre, total)
        best_suf = 0
        total = 0
        for v in reversed(a):
            total += v
            best_suf = max(best_suf, total)
        out.append(str(max(best, gain + best_pre, gain + best_suf)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N + M)$ per test case
- **Space:** $O(N + M)$
