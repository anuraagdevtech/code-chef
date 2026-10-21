# 1781 &middot; Minion Chef and Bananas

> CodeChef problem code [`MINEAT`](https://www.codechef.com/problems/MINEAT) &middot; time limit **2s** &middot; Jump from 2* to 3* (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Binary Search |
| **Technique** | Searching the answer on a monotonic predicate |
| **CodeChef category** | main |
| **Time** | $O(N \log \max A)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/binary-search/MINEAT.md](../docs/binary-search/MINEAT.md)

## Question

Minion Chef likes to eat bananas a lot. There are **N** piles of bananas in front of Chef; for each **i** (1 ≤ **i** ≤ **N**), the **i**-th pile contains **A_i** bananas.

Chef's mother wants her to eat the bananas and be healthy. She has gone to the office right now and will come back in **H** hours. Chef would like to make sure that she can finish eating all bananas by that time.

Suppose Chef has an *eating speed* of **K** bananas per hour. Each hour, she will choose some pile of bananas. If this pile contains at least **K** bananas, then she will eat **K** bananas from it. Otherwise, she will simply eat the whole pile (and won't eat any more bananas during this hour).

Chef likes to eat slowly, but still wants to finish eating all the bananas on time. Therefore, she would like to choose the minimum **K** such that she is able to eat all the bananas in **H** hours. Help Chef find that value of **K**.

**Input**

- The first line of the input contains a single integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The first line of each test case contains two space-separated integers **N** and **H** denoting the number of piles and the number of hours after which Chef's mom will come home.

- The second line contains **N** space-separated integers **A_1, A_2, ..., A_N**.

**Output**

For each test case, print a single line containing one integer — the minimum possible value of **K**.

**Constraints**

- 1 ≤ **T** ≤ 10

- 1 ≤ **N** ≤ 10^5

- **N** ≤ **H** ≤ 10^9

- 1 ≤ **A_i** ≤ 10^9 for each valid **i**

**Subtasks**

**Subtask #1 (30 points):**

- 1 ≤ **N** ≤ 100

- **A_i** ≤ 10^3 for each valid **i**

**Subtask #2 (70 points):** original constraints

## Constraints

- 1 ≤ T ≤ 10
- 1 ≤ N ≤ 10^5
- N ≤ H ≤ 10^9
- 1 ≤ A_i ≤ 10^9 for each valid i

## Sample

**Sample input**

```
3
3 3
1 2 3
3 4
1 2 3
4 5
4 3 2 7
```

**Sample output**

```
3
2
4
```

<details><summary>Explanation</summary>

**Test case $1$:** Chef can choose $K = 3$ bananas per hour. This way,
- In the first hour, Chef eats the pile $1$ as the number of bananas in the pile is less than equal to $3$.
- In the second hour, Chef eats the pile $2$ as the number of bananas in the pile is less than equal to $3$.
- In the third hour, Chef eats the pile $3$ as the number of bananas in the pile is less than equal to $3$.

 Chef can finish eating all the bananas in $3$ hours. It can be shown that $3$ bananas per hour is the minimum possible speed with which Chef can finish all bananas in $3$ hours.

**Test case $2$:** Chef can choose $K = 2$ bananas per hour. This way,
- In the first hour, Chef eats the pile $1$ as the number of bananas in the pile is less than equal to $2$.
- In the second hour, Chef eats the pile $2$ as the number of bananas in the pile is less than equal to $2$.
- In the third hour, Chef eats the $2$ bananas from pile $3$. $1$ banana is left in pile $3$.
- In the fourth hour, Chef eats the remaining banana from pile $3$ as the number of bananas in the pile is less than equal to $2$.

 Chef can finish eating all the bananas in $4$ hours. It can be shown that $2$ bananas per hour is the minimum possible speed with which Chef can finish all bananas in $4$ hours.

**Test case $3$:** Chef can choose $K = 4$ bananas per hour. This way,
- In the first hour, Chef eats the pile $1$ as the number of bananas in the pile is less than equal to $4$.
- In the second hour, Chef eats the pile $2$ as the number of bananas in the pile is less than equal to $4$.
- In the third hour, Chef eats the pile $3$ as the number of bananas in the pile is less than equal to $4$.
- In the fourth hour, Chef eats the $4$ bananas from pile $4$. $3$ bananas are left in pile $4$.
- In the fifth hour, Chef eats the remaining bananas from pile $4$ as the number of bananas in the pile is less than equal to $4$.

 Chef can finish eating all the bananas in $5$ hours. It can be shown that $4$ bananas per hour is the minimum possible speed with which Chef can finish all bananas in $5$ hours.

</details>

## Approach

At speed $K$, a pile of $A_i$ bananas takes $\lceil A_i / K \rceil$ hours, because Chef commits a whole hour to one pile even when the remainder is small. So the total time is

$$f(K) = \sum_{i} \left\lceil \frac{A_i}{K} \right\rceil$$

The key structural fact is that $f$ is **non-increasing** in $K$: eating faster never takes longer. So the predicate "$f(K) \leq H$" is false for small $K$ and true for all $K$ beyond some threshold — exactly the monotone shape that **binary search on the answer** needs.

Search $K$ over $[1, \max A]$; the upper end suffices because at that speed every pile falls in one hour, needing $N \leq H$ hours, which the constraints guarantee.

Each evaluation of $f$ costs one pass, so the whole thing is $O(N \log \max A)$ — about $30$ passes rather than the $10^9$ a linear scan over $K$ would need.

The ceiling must be computed in integers as `(a + k - 1) // k`; a float division would drift at $A_i$ up to $10^9$.

The samples show the threshold moving with the budget. With piles $[1,2,3]$ and $H = 3$ — exactly the number of piles — Chef has one hour per pile, so $K$ must cover the largest pile outright: $K = 3$. Give her one extra hour ($H = 4$) and $K = 2$ suffices, since the $3$-pile may then take two hours.

Sample case 3 lands exactly on the budget: $K = 4$ costs $1+1+1+2 = 5 = H$, and $K = 3$ costs $7$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, h = int(data[pos]), int(data[pos + 1])
        piles = [int(v) for v in data[pos + 2:pos + 2 + n]]
        pos += 2 + n
        # Hours needed is non-increasing in k, so binary search the threshold.
        lo, hi = 1, max(piles)
        while lo < hi:
            k = (lo + hi) // 2
            if sum((a + k - 1) // k for a in piles) <= h:
                hi = k
            else:
                lo = k + 1
        out.append(str(lo))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N \log \max A)$ per test case
- **Space:** $O(1)$
