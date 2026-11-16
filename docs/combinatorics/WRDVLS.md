[&larr; 708. Potato to Gold](SIMPLEARRAY.md) &middot; [Index](../../README.md)

# 719. Weird Values

> CodeChef problem code [`WRDVLS`](https://www.codechef.com/problems/WRDVLS) &middot; difficulty **2393** &middot; time limit **2s**

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | For each value, count subarrays containing exactly that many occurrences |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

You are given an array $A = [A_1, A_2, \ldots, A_N]$ containing $N$ integers.

Consider any subarray $[A_L, A_{L+1}, \ldots, A_R]$ of this subarray (where $1\leq L \leq R \leq N$). Ther `weirdness` of this subarray, denoted $w(L, R)$, is defined to be the number of indices $L \leq i \leq R$ such that $A_i$ equals the number of occurrences of $A_i$ in this subarray.

Formally, we define $w(L, R)$ for $1 \leq L \leq R \leq N$ as follows:
- For every integer $x$, let $f_{L, R}(x)$ denote the number of indices $L \leq j \leq R$ such that $A_j = x$.
- $w(L, R)$ then equals the number of $L \leq i \leq R$ such that $A_i = f_{L, R}(A_i)$

For example, let $A = [1, 3, 5, 2, 1, 2, 9, 5]$. Then,
- $w(1, 8) = 2$, which can be computed as follows.
We have
    - $f_{1, 8}(1) = 2$
    - $f_{1, 8}(2) = 2$
    - $f_{1, 8}(3) = 1$
    - $f_{1, 8}(5) = 2$
    - $f_{1, 8}(9) = 1$

The only indices which satisfy $f_{1, 8}(A_i) = A_i$ are $i = 4$ and $i = 6$, and hence $w(1, 8) = 2$.
- $w(3, 5) = 1$ — the subarray is $[5, 2, 1]$, and each of $1, 2, 5$ occur exactly once in this subarray. Of these, only $1$ equals the number of its occurrences in this subarray.

Given $A$, your task is to compute the sum of the `weirdness` of all subarrays of $A$, i.e, the value
$$\sum_{L = 1}^{N} \sum_{R = L}^N w(L, R)$$

**Input**

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains an integer $N$, the size of the given array.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — the elements of $A$.

**Output**

For each test case, output a single line containing a single integer — the sum of the `weirdness` of all subarrays of the given array.

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq N \leq 10^6$
- $1 \leq A_i \leq 10^6$
- The sum of $N$ across all test cases does not exceed $10^6$.

## Sample

**Sample input**

```
4
3
3 3 3
4
1 2 1 2
5
1 2 3 2 1
8
1 2 2 3 2 3 3 1
```

**Sample output**

```
3
10
16
54
```

<details><summary>Explanation</summary>

**Test Case 1:** The only subarray with non-zero `weirdness` is the whole array, which has $w(1, 3) = 3$ because every value is $3$ and it appears thrice.

**Test Case 2:** There are $10$ subarrays. Their `weirdness` values are as follows:
- $w(1, 1) = 1$, because $A_1 = 1$ and $f_{1, 1}(1) = 1$.
- $w(1, 2) = 1$, because $A_1 = 1$ and $f_{1, 2}(1) = 1$; but $A_2 = 2$ and $f_{1, 2}(2) = 1 \neq 2$.
- $w(1, 3) = 0$, here $f_{1, 3}(1) = 2 \neq 1$ and $f_{1, 3}(2) = 1 \neq 2$ so no index satisfies the condition.
- $w(1, 4) = 2$, here indices $2$ and $4$ satisfy the condition.
- $w(2, 2) = 0$
- $w(2, 3) = 1$, index $3$ satisfies the condition.
- $w(2, 4) = 3$, all indices satisfy the condition.
- $w(3, 3) = 1$
- $w(3, 4) = 1$, index $3$ satisfies the condition.
- $w(4, 4) = 0$

</details>

## Approach

Group the contributions by value. The indices holding a value $x$ are counted in $w(L, R)$ exactly when the subarray contains exactly $x$ occurrences of $x$, and then all $x$ of them are counted. So the answer is

$$\sum_x x \cdot \#\{\text{subarrays with exactly } x \text{ occurrences of } x\}.$$

For a value $x$ with occurrence positions $p_1 < p_2 < \dots < p_m$ (and sentinels $p_0 = 0$, $p_{m+1} = N + 1$), a subarray contains exactly the occurrences $p_j, \dots, p_{j+x-1}$ when its left end lies in $(p_{j-1}, p_j]$ and its right end in $[p_{j+x-1}, p_{j+x})$. The two choices are independent, giving $(p_j - p_{j-1}) \cdot (p_{j+x} - p_{j+x-1})$ subarrays.

Slide this window of $x$ consecutive occurrences over the list. Values with fewer than $x$ occurrences are skipped, and the total work is the total number of occurrences.

## Solution (Python)

```python
import sys


def solve(tokens):
    n = next(tokens)
    positions = {}
    for i in range(n):
        positions.setdefault(next(tokens), []).append(i)
    total = 0
    for value, occ in positions.items():
        if len(occ) < value:
            continue
        occ = [-1] + occ + [n]
        for j in range(1, len(occ) - value):
            total += value * (occ[j] - occ[j - 1]) * (occ[j + value] - occ[j + value - 1])
    return str(total)


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

- A value larger than its number of occurrences never contributes.
- The value 1 contributes for every subarray that contains it exactly once.
- The total is far larger than 32 bits for big inputs.
- Sentinels at both ends make the boundary windows uniform.

## Dry run

`A = [1, 2, 1, 2]` (positions 1-4).

- $x = 1$ at positions 1, 3: window `{1}`: $(1 - 0)(3 - 1) = 2$; window `{3}`: $(3 - 1)(5 - 3) = 4$. Contribution $1 \cdot 6 = 6$.
- $x = 2$ at positions 2, 4: one window `{2, 4}`: $(2 - 0)(5 - 4) = 2$. Contribution $2 \cdot 2 = 4$.

Answer 10.

> CodeChef tags: `Data Structures`, `Arrays`, `Mathematics`, `Algorithms`, `Greedy`

---

Same problem in rating order (#683 of 735): [../../by-rating/683-WRDVLS.md](../../by-rating/683-WRDVLS.md)
