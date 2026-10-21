# 348. Maximum Damage

> CodeChef problem code [`MAXDMGE`](https://www.codechef.com/problems/MAXDMGE) &middot; difficulty **1636** &middot; time limit **0.5 - 1s**

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | AND is monotone, so only adjacent pairs matter |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

## Question

Nasir and two of his henchmen are planning to attack $N$ shops of the Qureshi clan. The shops are conveniently lined up, and numbered from $1$ to $N$. The $i$-th shop contains $A_i$ kg of coal.

For a given subarray of shops $[A_L, A_{L+1}, \dots, A_R]$, the *bitwise and* of this subarray is defined to be the [bitwise AND](https://en.wikipedia.org/wiki/Bitwise_operation#AND) of the coal contained in each of the shops, i.e, $A_L \& A_{L+1} \& \dots \& A_R$.

The damage caused when bombing the $i$-th shop is computed to be the maximum *bitwise and* over all subarrays containing shop $i$, and whose size is **strictly larger than 1**.

For each shop ($1\leq i\leq N$), find the damage caused when Nasir bombs it.

**Input**

- The first line of input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$, denoting the number of shops.
- The second line of each test case contains $N$ space-separated integers, the $i$-th of which is $A_i$, representing the amount of coal in the $i$-th shop.

**Output**

For each test case, print a single line containing $N$ integers $d_1,d_2,\ldots,d_n$ where $d_i$ represents the maximum damage that can be caused if the $i$-th shop is to be bombed.

## Constraints

- $1 \leq T \leq 10000$
- $2 \leq N \leq 2 \cdot 10^5$
- $0 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
2
5
29 412 671 255 912
6
166 94 184 114 1124 298
```

**Sample output**

```
28 156 159 159 144 
6 24 48 96 96 32
```

<details><summary>Explanation</summary>

**Test case 1:** There are several choices of subarray which give the maximum for each index. One such choice is given below:

For shop $1$, choose subarray $[29, 412, 671, 255]$

For shop $2$, choose subarray $[412, 671, 255]$

For shop $3$, choose subarray $[671, 255]$

For shop $4$. choose subarray $[671, 255]$

For shop $5$, choose subarray $[412, 671, 255, 912]$

</details>

## Approach

The search space looks large — every subarray of size $\geq 2$ through each index — but **bitwise AND only ever loses bits**. Extending a subarray can clear bits and never set them, so for any subarray $S$ and any $S' \subseteq S$,

$$\mathrm{AND}(S) \leq \mathrm{AND}(S')$$

Every subarray of size $\geq 2$ containing index $i$ contains one of the two adjacent pairs $(i-1, i)$ or $(i, i+1)$, and by monotonicity its AND is no larger than that pair's. So the maximum is attained at size exactly $2$:

$$d_i = \max\bigl(A_{i-1} \,\&\, A_i,\; A_i \,\&\, A_{i+1}\bigr)$$

with the missing term dropped at the two ends — and since $N \geq 2$, each index always has at least one neighbour, so $d_i$ is always defined.

The implementation is then one pass computing the $N - 1$ adjacent ANDs and a second taking the max of each index's one or two incident pairs. There is no need for a sparse table or a two-pointer sweep over bit counts; the monotonicity collapses the whole problem.

Sample 1, $[29, 412, 671, 255, 912]$, has adjacent ANDs $28, 156, 159, 144$, so the answers are $28$, $\max(28,156)$, $\max(156,159)$, $\max(159,144)$, $144$ — i.e. `28 156 159 159 144`. Note $d_4 = 159$ comes from the pair to its *left*, which is the point of taking the max over both neighbours rather than always looking one way.

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
        pos += 1 + n
        # AND never gains bits, so the best subarray through i is a pair.
        pairs = [a[i] & a[i + 1] for i in range(n - 1)]
        best = [0] * n
        best[0] = pairs[0]
        best[n - 1] = pairs[n - 2]
        for i in range(1, n - 1):
            best[i] = pairs[i - 1] if pairs[i - 1] > pairs[i] else pairs[i]
        out.append(" ".join(map(str, best)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
