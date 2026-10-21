# 1729 &middot; Set Difference 

> CodeChef problem code [`SETDIFF`](https://www.codechef.com/problems/SETDIFF) &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Counting how often each element is the extreme |
| **CodeChef tags** | `Mathematics`, `Modular Arithmetic`, `Modular Exponentiation`, `Combinatorics` |
| **CodeChef category** | easy |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |

Same write-up grouped by topic: [../docs/combinatorics/SETDIFF.md](../docs/combinatorics/SETDIFF.md)

## Question

Churu is working as a data scientist in Coderpur. He works on a lot of data on the daily basis. One day, he found an interesting problem, which was very easy to solve for small data but was getting more complex with increasing number of data points. So, Churu needs your help in solving this problem.

 Given a set **S** of **N** non-negative integers (Some integers might occur more than once in the set), find out the value of **SETDIFF(S)**.

<img src="https://codechef_shared.s3.amazonaws.com/upfiles/SETDIFF.png" alt="Mountain View" style="width:304px;height:51px">

Where **max(s)** represents the maximum value in set **s** whereas **min(s)** represents the minimum value in the set **s**.
As value of ** SETDIFF(S)** can be very large, print it modulo ** (10^9 + 7) **.

There might be repeated values in the set. For set **S** = **{1,2,2}**, consider that first 2 is not same as the second 2 and there will be two different subsets **{1,2}**. See last sample case for the more clarifications.

**Input**

- First line of input contains an integer **T** denoting number of test cases.

- For each test case, first line will contain an integer **N** denoting number of elements in set **S**.

-  Next line contains **N** space separated integers denoting the set **S**.

**Output**

For each test case, print a single integer representing the answer of that test case.

**Note**

Two subsets will be called different if there exists an index **i** such that **S[i]** occurs in one of the subset and not in another.

**Constraints**

**Subtask #1: 20 points**

	- **1 ≤ T  ≤ 5, 1 ≤ N  ≤ 1000,  0 ≤ value in set ≤ 10^9**

**Subtask #2: 25 points**

	- **1 ≤ T  ≤ 5, 1 ≤ N  ≤ 10^5,  0 ≤ value in set ≤ 1000**

**Subtask #3: 55 points**

	- **1 ≤ T  ≤ 5, 1 ≤ N  ≤ 10^5,  0 ≤ value in set ≤ 10^9**

## Constraints

- $1 \leq T \leq 5$
- $1 \leq N \leq 10^5$
- $0 \leq$ each value in the set $\leq 10^9$
- the answer is printed modulo $10^9 + 7$

## Sample

**Sample input**

```
4
2
1 2
3
1 2 3
4
1 2 3 4
3
1 2 2
```

**Sample output**

```
1
6 
23
3
```

<details><summary>Explanation</summary>

For first case answer will be 2-1 = 1.

For the second case:

Subset = {1}, max(s)-min(s) = 0.
Subset = {2}, max(s)-min(s) = 0.
Subset = {3}, max(s)-min(s) = 0.
Subset = {1,2}, max(s)-min(s) = 1.
Subset = {2,3}, max(s)-min(s) = 1.
Subset = {1,3}, max(s)-min(s) = 2.
Subset = {1,2,3}, max(s)-min(s) = 2.
So the output will be 1+1+2+2 = 6.

In the last case, there are three subsets, {1,2}, {1,2} and {1,2,2} having max(s) - min(s) = 1 for each.

</details>

## Approach

Summing $\max(s) - \min(s)$ over all $2^N$ subsets is hopeless directly, but the sum **splits**:

$$\mathrm{SETDIFF}(S) = \sum_{s} \max(s) \;-\; \sum_{s} \min(s)$$

and each half counts how often an element plays its role. Sort ascending as $a_0 \leq \cdots \leq a_{N-1}$ and fix the tie-break by index. Then $a_i$ is the maximum of a subset exactly when the subset contains $a_i$ and nothing after it — any combination of the $i$ earlier elements, so $2^i$ subsets. Symmetrically it is the minimum of $2^{N-1-i}$ subsets. Hence

$$\mathrm{SETDIFF}(S) = \sum_{i=0}^{N-1} a_i\,2^{i} \;-\; \sum_{i=0}^{N-1} a_i\,2^{N-1-i} \pmod{10^9+7}$$

Singletons contribute $0$ to each half and cancel, which is why they can be left in without a special case.

Fixing the tie-break by index is what makes repeated values correct: the problem counts subsets by *position*, so the two copies of $2$ in $\{1,2,2\}$ give two distinct subsets $\{1,2\}$, and ordering them by index assigns each its own exponent without double counting. That sample gives $13 - 10 = 3$.

The modular subtraction can go negative, so add the modulus before reducing.

The other samples check the formula: $\{1,2\}$ gives $(1 + 4) - (2 + 2) = 1$; $\{1,2,3\}$ gives $(1 + 4 + 12) - (4 + 4 + 3) = 6$; and $\{1,2,3,4\}$ gives $49 - 26 = 23$.

## Solution (Python)

```python
import sys

MOD = 1_000_000_007


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        vals = sorted(int(x) for x in data[pos + 1:pos + 1 + n])
        pos += 1 + n
        # a_i tops 2^i subsets and bottoms 2^(n-1-i) of them.
        total = 0
        low, high = 1, pow(2, n - 1, MOD)
        inv2 = (MOD + 1) // 2
        for v in vals:
            total = (total + v * (low - high)) % MOD
            low = low * 2 % MOD
            high = high * inv2 % MOD
        out.append(str(total % MOD))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N \log N)$ per test case
- **Space:** $O(N)$
