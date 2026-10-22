[&larr; 441. OR Tuples](ORTUPLES.md) &middot; [Index](../../README.md) &middot; [466. Add to Subsequence &rarr;](SUBSEQDIST.md)

# 459. Set Difference 

> CodeChef problem code [`SETDIFF`](https://www.codechef.com/problems/SETDIFF) &middot; difficulty **1729** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Counting how often each element is the extreme |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

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

## Edge cases

- **Each element's contribution is counted by how often it is the extreme.** In sorted order, $a_i$ is the maximum of the $2^i$ subsets drawn from the smaller elements plus itself, and the minimum of $2^{n-1-i}$ — so the total is $\sum a_i (2^i - 2^{n-1-i})$ with no subset enumeration.
- **The two powers are maintained incrementally**, one doubling and one halving — the halving by multiplying by the modular inverse of $2$, since there is no integer division under a modulus.
- **The inverse of $2$ is $(p+1)/2$** for an odd prime modulus, which is exact and needs no `pow` call.
- **Duplicates are handled by position, not value.** Sorting breaks ties arbitrarily but consistently, so every subset is still counted exactly once — the fourth sample row has two $2$s and answers $3$.
- **Singleton subsets contribute $0$**, since the maximum and minimum coincide — which the formula gets right because the two counts cancel for them.
- **The subtraction can go negative before reduction**, so the final `% MOD` is needed to bring it back into range.
- **$N$ up to $10^5$** with values to $10^9$, so the sum must be taken modulo throughout rather than at the end.

## Dry run

Third sample: $S = \{1, 2, 3, 4\}$, so $n = 4$.

| $i$ | $a_i$ | times it is the max ($2^i$) | times it is the min ($2^{n-1-i}$) | contribution |
|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 8 | $-7$ |
| 1 | 2 | 2 | 4 | $-4$ |
| 2 | 3 | 4 | 2 | $+6$ |
| 3 | 4 | 8 | 1 | $+28$ |

Total `23`.

> CodeChef tags: `Mathematics`, `Modular Arithmetic`

---

Same problem in rating order (#431 of 486): [../../by-rating/431-SETDIFF.md](../../by-rating/431-SETDIFF.md)
