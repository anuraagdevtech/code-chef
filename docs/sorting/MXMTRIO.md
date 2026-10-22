# 214. Maximum Trio

> CodeChef problem code [`MXMTRIO`](https://www.codechef.com/problems/MXMTRIO) &middot; difficulty **1349** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | Choosing extremes for a product |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Level up from 1* to 2* (Level 2) |

## Question

You are given an array $A$ of $N$ elements. For any ordered triplet $(i, j, k)$ such that $i$, $j$, and $k$ are pairwise distinct and $1 \le i, j, k \le N$, the value of this triplet is $(A_i-A_j)\cdot A_k$. You need to find the **maximum** value among all possible ordered triplets.

**Note:** Two ordered triplets $(a, b, c)$ and $(d, e, f)$ are only equal when $a = d$ **and** $b = e$ **and** $c = f$. As an example, $(1, 2, 3)$ and $(2, 3, 1)$ are two different ordered triplets.

**Input**

- The first line of the input contains a single integer $T$ - the number of test cases. The test cases then follow.
- The first line of each test case contains an integer $N$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$.

**Output**

For each test case, output the maximum value among all different ordered triplets.

## Constraints

- $1 \le T \le 100$
- $3 \le N \le 3 \cdot 10^5$
- $1 \le A_i \le 10^6$
- Sum of $N$ over all testcases won't exceed $3 \cdot 10^5$.

**Subtasks**

- **Subtask $1$ (30 points)**: Sum of $N$ over all cases won't exceed $2000$.
- **Subtask $2$ (70 points)**: Original constraint

## Sample

**Sample input**

```
3
3
1 1 3
5
3 4 4 1 2
5
23 17 21 18 19
```

**Sample output**

```
2
12
126
```

<details><summary>Explanation</summary>

- **Test case $1$**: The desired triplet is $(3, 2, 1)$, which yields the value of $(A_3 - A_2) \cdot A_1 = (3 - 1) \cdot 1 = 2$.
- **Test case $2$**: The desired triplet is $(2, 4, 3)$, which yields the value of $(A_2 - A_4) \cdot A_3 = (4 - 1) \cdot 4 = 12$.
- **Test case $3$**: The desired triplet is $(1, 2, 3)$, which yields the value of $(A_1 - A_2) \cdot A_3 = (23 - 17) \cdot 21 = 126$.

</details>

## Approach

Maximise $(A_i - A_j) \cdot A_k$ over three pairwise distinct indices. Every $A_i$ is **at least $1$**, which is what makes the answer a clean choice of extremes.

Since all values are positive, the product is largest when both factors are. The difference is maximised by taking $A_i$ as the largest value and $A_j$ as the smallest. That leaves $A_k$ to be the largest value still available, which after sorting is the **second** largest. So with $a$ sorted ascending:

$$(a_{n-1} - a_0) \cdot a_{n-2}$$

The natural worry is whether sacrificing some difference to free up the maximum for $A_k$ could do better — using $a_{n-2}$ and $a_0$ for the difference while $A_k = a_{n-1}$. Comparing the two:

$$(a_{n-1} - a_0)\,a_{n-2} - (a_{n-2} - a_0)\,a_{n-1} = a_0\,(a_{n-1} - a_{n-2}) \geq 0$$

so the first is always at least as good. Positivity of $a_0$ is exactly what decides it; with zeros or negatives allowed the comparison could flip and the problem would be considerably harder.

The triplet is **ordered** and the indices distinct, so the three chosen positions are genuinely different — guaranteed since $N \geq 3$.

Sample case 2, $[3,4,4,1,2]$, sorts to $[1,2,3,4,4]$: $(4-1) \cdot 4 = 12$. Note the two $4$s occupy separate indices, so using one as $A_i$ and the other as $A_k$ is legal — which is why duplicates need no special handling.

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
        a = sorted(int(v) for v in data[pos + 1:pos + 1 + n])
        pos += 1 + n
        # All values are positive, so take the widest difference and the
        # largest remaining element as the multiplier.
        out.append(str((a[-1] - a[0]) * a[-2]))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N \log N)$ per test case
- **Space:** $O(N)$

## Edge cases

- **The obvious alternative is never better.** Using the second-largest in the difference and the largest as the multiplier gives $(a_{n-1} - a_1) \cdot a_n$, and the chosen form beats it by $a_1 (a_n - a_{n-1}) \geq 0$ — non-negative because every value is positive. The third row shows the gap concretely: $126$ against $92$.
- **All values positive is essential.** With negatives the largest product could come from quite different positions, and this two-line argument collapses.
- **$N = 3$** (the first row): the three elements are forced, and the multiplier is simply the middle one.
- **Duplicates at the top** (the second row, two $4$s): the maximum and second-maximum are equal, which sorted indices handle without a tie-break.
- **All values equal** → the difference is $0$ and so is the answer.
- **Products reach $10^6 \times 10^6 = 10^{12}$**, past 32-bit signed.

## Dry run

Third sample: $23, 17, 21, 18, 19$ sorted to $17, 18, 19, 21, 23$.

| choice | difference | multiplier | product |
|---|---:|---:|---:|
| max $-$ min, times second-max | $23 - 17 = 6$ | 21 | **126** |
| second-max $-$ min, times max | $21 - 17 = 4$ | 23 | 92 |

Output `126`, and the margin is $a_1(a_n - a_{n-1}) = 17 \cdot 2 = 34$.

---

Same problem in rating order (#213 of 486): [../../by-rating/213-MXMTRIO.md](../../by-rating/213-MXMTRIO.md)
