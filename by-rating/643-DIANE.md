[&larr; 642. String Operations](642-STROPERS.md) &middot; [Index](README.md) &middot; [644. Chef and Two String &rarr;](644-CHEFTWOS.md)

# 643. Yet Another Crossover Episode

> [`DIANE`](https://www.codechef.com/problems/DIANE) &middot; difficulty **2221** &middot; time limit **2s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Blocks with a computable contribution, separated by ones |
| **CodeChef tags** | `Algorithms`, `Constructive`, `ad-hoc` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(D / 99998 + 1)$ per test case |
| **Space** | $O(D / 99998 + 1)$ for the output |

## Question

You are given an integer $D$. Find an integer sequence $A_1, A_2, \ldots, A_N$ such that the following conditions are satisfied:
- $1 \le N \le 10^5$
- $1 \le A_i \le 10^5$ for each valid $i$
- $\sum_{i=1}^N \sum_{j=i}^N \left( \mathrm{min}(A_i, A_{i+1}, \ldots, A_j) - \mathrm{GCD}(A_i, A_{i+1}, \ldots, A_j) \right) = D$

It can be proved that a solution always exists under the given constraints.

Note: $\mathrm{GCD}(B_1, B_2, \ldots, B_M)$ is the greatest integer which divides all the integers $B_1, B_2, \ldots, B_M$.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer $D$.

**Output**
For each test case, print two lines. The first of these lines should contain a single integer $N$. The second line should contain $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

If there are multiple solutions, you may find any one of them.

**Constraints**
- $1 \le T \le 10$
- $0 \le D \le 10^9$

**Example Input**
```
4
2
5
200
13
```

**Example Output**
```
3
3 3 2
5
2 8 5 1 10
7
12 10 15 11 19 13 15
4
5 4 4 10
```

## Constraints

- $1 \le T \le 10$
- $0 \le D \le 10^9$

## Approach

Three observations make the sum easy to control.

- A subarray of equal values has min = gcd and contributes 0.
- A subarray containing a 1 has min = gcd = 1 and contributes 0. So a 1 between two blocks makes them independent.
- Take $k$ copies of $a$ followed by a single $a + 1$. Subarrays inside the copies contribute 0, the single $a + 1$ contributes 0, and each of the $k$ subarrays that end at the last element and include at least one $a$ has minimum $a$ and gcd 1 (consecutive integers are coprime), contributing $a - 1$. The block is worth $k (a - 1)$.

Write $D = 99998 \cdot q + r$ with $0 \le r < 99998$. A block of $q$ copies of 99999 followed by 100000 is worth $99998 \cdot q$, and the two-element block $r + 1, r + 2$ is worth $r$. Put a 1 between them when both are present; for $D = 0$ print the single element 1. The length is about $D / 99998 + 4$, far below the limit.

## Solution

```python
import sys


def solve(tokens):
    target = next(tokens)
    quotient, remainder = divmod(target, 99998)
    result = []
    if quotient:
        result = [99999] * quotient + [100000]
    if remainder:
        if result:
            result.append(1)
        result.extend([remainder + 1, remainder + 2])
    if not result:
        result = [1]
    return str(len(result)) + '\n' + ' '.join(map(str, result))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Edge cases

- $D = 0$: the array `1`.
- $r = 0$ or $q = 0$: only one of the two blocks is printed, without a separator.
- All values stay within $[1, 10^5]$: the largest are 99999 and 100000.
- Many arrays are valid, so the output is validated by a checker.

## Dry run

`D = 200`: $q = 0$, $r = 200$. Output the block `201 202`: its only non-trivial subarray has min 201 and gcd 1, contributing 200.

`D = 199996 + 5 = 200001`: $q = 2$, $r = 5$. Output `99999 99999 100000 1 6 7`: the first block gives $2 \cdot 99998$, the last gives 5, and everything touching the 1 gives 0.

---

Same problem grouped by topic: [../docs/constructive/DIANE.md](../docs/constructive/DIANE.md)
