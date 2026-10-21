# 235. Remove Element

> [`REMELEM`](https://www.codechef.com/problems/REMELEM) &middot; difficulty **1415** &middot; time limit **1s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | The smallest element as universal partner |
| **CodeChef tags** | `Data Structures`, `Arrays`, `Algorithms`, `Constructive`, `1D Arrays`, `ad-hoc` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

You are given an array $A = [A_1, A_2, \ldots, A_N]$ consisting of $N$ positive integers.

You are also given a constant $K$, using which you can perform the following operation on $A$:
- Choose two distinct indices $i$ and $j$ such that $A_i + A_j \le K$, and remove either $A_i$ or $A_j$ from $A$.

Is it possible to obtain an array consisting of only one element using several (possibly, zero) such operations?

**Input**

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

**Output**

For each test case, print `"YES"` if it is possible to obtain an array consisting of only one element using the given operation, otherwise print `"NO"`.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq N \leq 10^5$
- $1 \leq A_i, K \leq 10^9$
- Sum of $N$ over all test cases does not exceed $2\cdot 10^5$

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
3
1 3
1
3 3
2 2 2
4 7
1 4 3 5
```

**Sample output**

```
YES
NO
YES
```

<details><summary>Explanation</summary>

**Test case $1$:** The length of the array is already $1$.

**Test case $2$:** There is no way to delete an element from the given array.

**Test case $3$:** One possible sequence of operations is:

- Choose $i = 1, j = 4$ and remove $A_j = 5$. Hence the array becomes $[1, 4, 3]$.
- Choose $i = 2, j = 3$ and remove $A_i = 4$. Hence the array becomes $[1, 3]$.
- Choose $i = 1, j = 2$ and remove $A_i = 1$. Hence the array becomes $[3]$, which is of length $1$.

</details>

## Approach

To delete an element $x$, it must be paired with some $y$ where $x + y \leq K$. The **best possible partner is always the array's minimum** $m$, since no other value gives a smaller sum. So $x$ is deletable at all only if $x + m \leq K$.

That gives the test immediately. If even the **largest** element can be paired with the minimum,

$$\min(A) + \max(A) \leq K$$

then every element except $m$ can be deleted one at a time using $m$ as the partner, leaving $m$ alone. If instead $m + \max(A) > K$, the maximum can never be removed by anything — and neither can $m$ be removed while leaving the maximum behind, because that final pair would also exceed $K$. So the array is stuck with at least two elements.

The tempting shortcut is to test the two **smallest** elements, reasoning that the cheapest available pair is what matters. That is wrong, and the counterexample is instructive: $[1, 100, 200]$ with $K = 101$ passes $1 + 100 \leq 101$, yet $200$ can never be deleted and nothing can be paired with it, so the answer is `NO`. The binding constraint is the *largest* element, not the second smallest.

$N = 1$ is a separate case: the array is already a single element and no operation is needed, so the answer is `YES` regardless of $K$ — sample case 1.

Sample case 2, $[2,2,2]$ with $K = 3$, cannot even start, since $2 + 2 > 3$. Sample case 3 has $1 + 5 = 6 \leq 7$, so everything collapses onto the $1$.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        vals = [int(v) for v in data[pos + 2:pos + 2 + n]]
        pos += 2 + n
        if n == 1:
            out.append("YES")           # already a single element
        else:
            # The minimum is the best partner there is, so the maximum is the
            # binding case - not the second smallest.
            out.append("YES" if min(vals) + max(vals) <= k else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **$N = 1$ needs its own branch.** The array is already a single element, so zero operations suffice; the general formula would test $2 A_1 \leq K$ and reject, for example, $A = [5]$ with $K = 3$. The sample's first row happens to pass either way, so it does not expose this.
- **The minimum is the universal partner**, so the *maximum* is the binding case. Checking the two smallest elements instead would accept arrays whose largest element can never be paired off.
- **The minimum is never removed** — it is kept as the survivor — so it stays available as a partner for every other element, which is what makes one comparison enough.
- **All equal** (the second row): $\min + \max = 2 A_1 = 4$, which exceeds $K = 3$ even though each element alone is well under it.
- **Exactly equal to $K$** → `YES`; the condition is non-strict.
- **Sum of $N \leq 2 \cdot 10^5$**: one pass computing both extremes.

## Dry run

| $N$ | $K$ | array | min | max | $\min + \max$ | output |
|---:|---:|---|---:|---:|---:|---|
| 1 | 3 | $1$ | — | — | — (single element) | `YES` |
| 3 | 3 | $2,2,2$ | 2 | 2 | 4 | `NO` |
| 4 | 7 | $1,4,3,5$ | 1 | 5 | 6 | `YES` |

In row 3 the $1$ pairs with $5$, then $4$, then $3$, removing each in turn and surviving itself.

---

Same problem grouped by topic: [../docs/greedy/REMELEM.md](../docs/greedy/REMELEM.md)
