[&larr; 623. Binary Substitution](623-SUBSBIN.md) &middot; [Index](README.md) &middot; [625. Minimize swaps &rarr;](625-DIVBY3.md)

# 624. Chef Goes Shopping

> [`CHEFSHOPPING`](https://www.codechef.com/problems/CHEFSHOPPING) &middot; difficulty **2164** &middot; time limit **1s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Every original boundary is paid once, in its cheaper direction |
| **CodeChef tags** | `Algorithms`, `Observation` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

MoEngage goes shopping with Chef. There are $N$ ingredients placed on a line, numbered $1$ to $N$ from left to right.

At any point in time, MoEngage can choose the ingredient numbered $x$ and do **one** of the following operations:
- If the chosen ingredient is not the leftmost amongst the remaining ingredients, **remove the left neighbor**. This operation costs $L_x$ coins.
- If the chosen ingredient is not the rightmost amongst the remaining ingredients, **remove the right neighbor**. This operation costs $R_x$ coins.

**Note:** MoEngage can perform **at most one** operation of one type on a particular ingredient. For example, you can't remove elements from the left of ingredient $x$ two times. However, you can remove one ingredient each from the left and from the right of ingredient $x$.

MoEngage performs the operations until only one ingredient is left.
Find the **minimum** number of coins he needs to pay so that only one ingredient is left.

**Input**

- The first line contains a positive integer $T$ - the number of test cases. Then $T$ test cases follow.
- The first line of each test case contains a single integer $N$ - the number of ingredients.
- The second line of each test case contains $N$ integers $L_1, L_2, \ldots, L_N$ - the number of coins required to remove the ingredient from the left of an ingredient.
- The third line of each test case contains $N$ integers $R_1, R_2, \ldots, R_N$ - the number of coins required to remove the ingredient from the right of an ingredient.

**Output**

For each test case, output in a new line, one integer - the **minimum** number of coins MoEngage needs to pay so that only one ingredient is left.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 2 \cdot 10^5$
- $1 \le L_i, R_i \le 10^9$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
3
1
3
4
4
2 1 3 2
4 2 4 3
7
3 10 5 2 8 3 9
8 6 11 5 9 13 7
```

**Sample output**

```
0
5
32
```

<details><summary>Explanation</summary>

- **Test case 1:** The number of ingredients is already $1$. Thus, MoEngage has to spend $0$ coins.
- **Test case 2:** Initially, the list of ingredients is $[1, 2, 3, 4]$. MoEngage can apply the operations in the following way:
    - Apply the first operation on ingredient $4$. Coins required for this are $L_4 = 2$. The updated list of ingredients is $[1, 2, 4]$.
    - Apply the second operation on ingredient $2$. Coins required for this are $R_2 = 2$. The updated list of ingredients is $[1, 2]$.
    - Apply the first operation on ingredient $2$. Coins required for this are $L_2 = 1$. The updated list of ingredients is $[2]$.

Thus, the total number of coins required is $2+2+1 = 5$. It can be shown that MoEngage cannot achieve a single ingredient in less than $5$ coins.

</details>

## Approach

Look at the boundary between the original neighbours $i$ and $i+1$. At the end only one ingredient survives, so at some moment the two sides of this boundary must be merged: an ingredient from the left block removes its right neighbour, paying its $R$, or an ingredient from the right block removes its left neighbour, paying its $L$. Each removal settles exactly one original boundary, so there are $N - 1$ payments, one per boundary.

The cheapest payment that can ever be attributed to boundary $i$ is $\min(R_i, L_{i+1})$ when the two original neighbours are still adjacent, and this can be arranged for all boundaries simultaneously by choosing a suitable order of removals. Hence the answer is

$$\sum_{i=1}^{N-1} \min(R_i, L_{i+1}).$$

## Solution

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        left_cost = [next(tokens) for _ in range(n)]
        right_cost = [next(tokens) for _ in range(n)]
        out.append(str(sum((min(right_cost[i], left_cost[i + 1]) for i in range(n - 1)))))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- $N = 1$: nothing to remove, cost 0.
- Costs go up to $10^9$ per removal, so the total needs 64 bits.
- $L_1$ and $R_N$ are never used.
- The order of removals is not asked for - only the total.

## Dry run

`L = [2, 1, 3, 2]`, `R = [4, 2, 4, 3]`.

- boundary 1|2: $\min(R_1, L_2) = \min(4, 1) = 1$
- boundary 2|3: $\min(R_2, L_3) = \min(2, 3) = 2$
- boundary 3|4: $\min(R_3, L_4) = \min(4, 2) = 2$

Answer 5.

---

Same problem grouped by topic: [../docs/greedy/CHEFSHOPPING.md](../docs/greedy/CHEFSHOPPING.md)
