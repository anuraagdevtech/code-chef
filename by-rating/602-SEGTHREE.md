[&larr; 601. Chef and Rectangle Array](601-CHSQARR.md) &middot; [Index](README.md) &middot; [603. Full Path Eraser &rarr;](603-FPE.md)

# 602. Segment Three

> [`SEGTHREE`](https://www.codechef.com/problems/SEGTHREE) &middot; difficulty **2089** &middot; time limit **1s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Brute Force |
| **Technique** | Residues repeat with period three - try all nine patterns |
| **CodeChef tags** | `Algorithms`, `Constructive`, `ad-hoc`, `Observation` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

Today is an important day for Chef Hammoda as a lot of customers will be visiting his restaurant.
The restaurant contains $N$ tables, and each customer will sit at one table.

Initially, Chef Hammoda plans for the dish served to the $i$-th table to contain $A_i$ ingredients.
However, he thinks that a group of three dishes is *delicious* if the sum of the number of ingredients of the three dishes is divisible by $3$.

Hammoda wants every consecutive group of $3$ tables to have delicious dishes. To achieve this, he can add as many ingredients as he wants to each dish.
Help him determine the **minimum** number of additional ingredients needed to make every group of three consecutive tables *delicious*.

More formally, solve the following problem:
You are given an array $A = [A_1, A_2, \ldots, A_N]$ of length $N$. You're allowed to increment each element however much you like.
Find the **minimum** number of increments needed so that in the resulting array, the sum of every three consecutive elements is divisible by $3$

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains one integer $N$ — the number of tables.
    - The next line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — number of ingredients initially present in the $i^{th}$ dish.

**Output**

For each test case, print on a new line a single integer: the minimum number of increments needed to make every length-$3$ subarray of $A$ have a sum that's divisible by $3$.

## Constraints

- $1 \leq T \leq 10^5$
- $3 \leq N \leq 10^5$
- $1 \leq a_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $10^5$.

**Subtasks**

- **Subtask 1 (10 points):** $1 \leq M \leq 10$
- **Subtask 2 (20 points):** The sum of $N$ across all test cases won't exceed $20$.
- **Subtask 3 (70 points):** No further constraints.

## Sample

**Sample input**

```
3
3
1 2 3 
10
2 3 10 25 12 7 10 12 1 46
7
10 12 15 16 17 200 132
```

**Sample output**

```
0
3
4
```

<details><summary>Explanation</summary>

**Test case $1$:** There is only one subarray of length $3$, and its sum already divisible by $3$.

**Test case $2$:** The array after increments can be:
$[2, 3, 10, \underline{26}, 12, 7, \underline{11}, 12, 1, \underline{47}]$
for a total of $3$ increments (the elements underlined were all incremented by $1$ each). Every subarray of length $3$ now has a sum that's divisible by $3$.
It can be proved that it's not possible to achieve this using two or fewer increments.

**Test case $3$:** The array after increments can be:
$[10, 12, \underline{17}, 16, \underline{18}, 200, \underline{133}]$
for a total of $4$ increments.
Here, $15$ was incremented twice to reach $17$, and the other two elements were incremented once each.

</details>

## Approach

If windows $[i, i+2]$ and $[i+1, i+3]$ both have sums divisible by 3, subtracting them gives $A_{i+3} \equiv A_i \pmod 3$. So in a valid array the residues are periodic with period 3, and the three residues $r_0, r_1, r_2$ of one period must satisfy $r_0 + r_1 + r_2 \equiv 0$. Conversely any such periodic pattern is valid.

Only increments are allowed, so bringing an element with residue $a$ to residue $v$ costs $(v - a) \bmod 3$. For each position class $i \bmod 3$ and each target residue accumulate the total cost in a $3 \times 3$ table. Then try all nine choices of $(r_0, r_1)$, with $r_2 = (-r_0 - r_1) \bmod 3$ forced, and take the cheapest.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        cost = [[0] * 3 for _ in range(3)]
        for i in range(n):
            residue = next(tokens) % 3
            for v in range(3):
                cost[i % 3][v] += (v - residue) % 3
        best = min((cost[0][residue] + cost[1][b] + cost[2][(-residue - b) % 3] for residue in range(3) for b in range(3)))
        out.append(str(best))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- Only additions are allowed; lowering a residue by 1 costs 2.
- $N = 3$ has a single window but the same formula applies.
- The values themselves are irrelevant beyond their residues.
- The cost can be as large as $2N$.

## Dry run

`A = [1, 2, 3]`: residues `1 2 0`.

Choosing the pattern $(1, 2, 0)$ costs nothing and $1 + 2 + 0 \equiv 0$, so the answer is 0.

For `A = [1, 1, 1, 2]` (residues `1 1 1 2`): the pattern $(1, 1, 1)$ is valid and only the last element, in class 0, has to move from 2 to 1, costing 2; the pattern $(2, 0, 1)$ costs $1 + 2 + 0 + 0 = 3$. The answer is 2.

---

Same problem grouped by topic: [../docs/brute-force/SEGTHREE.md](../docs/brute-force/SEGTHREE.md)
