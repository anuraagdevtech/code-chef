# 304. Positive array

> CodeChef problem code [`CIREQ`](https://www.codechef.com/problems/CIREQ) &middot; difficulty **1620** &middot; time limit **2s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Hall's condition on value-capped positions |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

​A `1`-indexed array is called *positive* if every element of the array is greater than or equal to the index on which it lies. Formally, an array $B$ of size $M$ is called positive if $B_i \ge i$ for each $1\le i \le M$.

For example, the arrays $[1], [2, 2], [3, 2, 4, 4]$ are positive while the arrays $[2, 1], [3, 1, 2]$ are not positive.

You are given an array $A$ containing $N$ integers. You want to distribute all elements of the array into some positive arrays. The elements of a positive array might not occur in the order they appear in the array $A$.

Find the **minimum** number of positive arrays that the elements of the array $A$ can be divided into.

Please see the sample cases below for more clarity.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains an integer $N$ — the number of elements in the array $A$.
    - The next line contains $N$ space-separated integers $A_1, A_2,\ldots, A_N$ — the elements of array $A$.

**Output**

For each test case, output on a new line the minimum number of positive arrays that the elements of the array $A$ can be divided into.
​

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq N$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

## Sample

**Sample input**

```
5
3
2 3 3
4
3 1 1 2
3
1 1 1
5
1 2 2 4 5
6
3 2 1 2 2 1
```

**Sample output**

```
1
2
3
2
3
```

<details><summary>Explanation</summary>

**Test case $1$:** The given array is already positive. So the optimal division is $[2,3,3]$.

**Test case $2$:** One possible division is $[1, 2], [1, 3]$.

**Test case $3$:** The only possible division is $[1],[1],[1]$.

**Test case $4$:** One possible division is $[1, 2, 5], [2, 4]$.

**Test case $5$:** One possible division is $[1, 2, 3], [1], [2,2]$.

</details>

## Approach

An element of value $v$ can occupy positions $1, 2, \ldots, v$ of a positive array, and no further — position $i$ demands a value of at least $i$. With $k$ arrays there are exactly $k$ slots at each position index.

So the question is whether the elements can be matched into slots, and **Hall's condition** answers it. The elements with value at most $t$ are confined to positions $1 \ldots t$, which offer only $kt$ slots. So feasibility with $k$ arrays requires, for every $t$,

$$\#\{i : A_i \leq t\} \;\leq\; k\,t$$

and that condition is also sufficient, since the constraint sets are nested intervals. Rearranging gives the answer directly:

$$k = \max_{t} \left\lceil \frac{c_t}{t} \right\rceil, \qquad c_t = \#\{i : A_i \leq t\}$$

Because $A_i \leq N$, the counts $c_t$ come from one counting pass and a prefix sum, so the whole thing is $O(N)$ with no sorting or binary search.

The small values are what force extra arrays — each array can hold only one element of value $1$, since only position $1$ accepts it. Sample case 3, $[1,1,1]$, needs three arrays for exactly that reason, even though the array is tiny.

Sample case 5, $[3,2,1,2,2,1]$, is decided at $t = 2$: five elements are at most $2$, but each array offers only two such slots, so $\lceil 5/2 \rceil = 3$ arrays are needed — more than the $t=1$ bound of $2$ or the $t=3$ bound of $2$. Checking only one threshold would under-count.

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
        freq = [0] * (n + 2)
        for v in data[pos + 1:pos + 1 + n]:
            freq[int(v)] += 1
        pos += 1 + n
        # Elements of value <= t fit only in positions 1..t, which offer k*t
        # slots across k arrays.
        best = 1
        seen = 0
        for value in range(1, n + 1):
            seen += freq[value]
            need = (seen + value - 1) // value
            if need > best:
                best = need
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$

> CodeChef tags: `Data Structures`, `Algorithms`
