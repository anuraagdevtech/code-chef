[&larr; 616. Interesting Array](616-INTARR.md) &middot; [Index](README.md) &middot; [618. Maximising Vacations &rarr;](618-MAXVAC.md)

# 617. Chefs in Queue

> [`CHFQUEUE`](https://www.codechef.com/problems/CHFQUEUE) &middot; difficulty **2146** &middot; time limit **2s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Stacks |
| **Technique** | Nearest strictly smaller element to the right with a monotonic stack |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ |
| **Space** | $O(N)$ |

## Question

** Read problems statements in Russian [here](https://www.codechef.com/download/translated/LTIME05/russian/CHFQUEUE.pdf)**

All the chefs (except the Head Chef) are standing in queue to submit their bills. The chefs have different seniority. In all there are **N** chefs of **K** different seniority levels. These are given to you in an array, where **A_1**, **A_2**, ..., **A_N** denote the seniority of chefs in the queue. **A_N** denotes front of the queue and **A_1** denotes end of the queue.

Head Chef gets an interesting thought past his head. He begins to think what if every chef starting from the end of the queue begins to delegate his job of submitting bills to a chef least ahead of him in the queue but junior to him. The Head Chef's fearfulness of this scenario is **f = i2 - i1 + 1**, where **i1** is the index of chef in queue and **i2** is the index of the junior chef. Head Chef's total fearfulness of chaos is the product of all the fearfulness in Head Chef's mind. Note if a chef has no junior ahead of him/her in the queue then Head Chef's fearfulness for this Chef is **1**.

You are required to find the Head Chef's total fearfulness given an arrangement of Chef's in a queue. Since this number can be quite large output it modulo **1000000007**.

**Input**

Input description.

- The first line contains two integers **N** and ** K ** denoting the number of chefs and the number of seniority levels. The second line contains **N** space-separated integers **A_1**, **A_2**, ..., **A_N** denoting the seniority of chefs in the queue. **A_N** denotes front of the queue and **A_1** denotes end of the queue.

**Output**

Output description.

- Output a single integer denoting the total fearfulness of the Head Chef.

**Constraints**

- **1** ≤ **N** ≤ **1000000**

- **1** ≤ **a_i** ≤ **1000000**

- **2** ≤ **K** ≤ **100000**

**Scoring**

**Subtask 1 : N <= 5000 ( 10 points)**
** Subtask 2 : K = 2 ( 10 points) **
** Subtask 3 : K <= 10 ( 20 points ) **
** Subtask 4 : See Constraints ( 60 points ) **

## Constraints

- 1 ≤ N ≤ 1000000
- 1 ≤ a_i ≤ 1000000
- 2 ≤ K ≤ 100000

## Sample

**Sample input**

```
4 2
1 2 1 2
```

**Sample output**

```
2
```

<details><summary>Explanation</summary>

**Example case 1.** Only the second chef has a junior in front of him and the fearfulness he causes to the head chef is 3 - 2 + 1 = 2. Every other chef causes a fearfulness of 1 for the Head Chef.

</details>

## Approach

Each chef delegates to the nearest chef ahead of him (larger index) with strictly smaller seniority; if that chef is at index $i_2$ the contribution is $i_2 - i_1 + 1$, and a chef with no junior ahead contributes 1. The answer is the product of all contributions modulo $10^9 + 7$.

"Nearest strictly smaller to the right" is the textbook monotonic-stack query. Scan from the front of the queue (index $N$) to the back, keeping a stack of indices whose values are strictly increasing from bottom to top. For the current chef pop everything that is not smaller than him; the top of the stack, if any, is his junior.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(tokens)
    next(tokens)
    seniority = [next(tokens) for _ in range(n)]
    stack = []
    product = 1
    for i in range(n - 1, -1, -1):
        while stack and seniority[stack[-1]] >= seniority[i]:
            stack.pop()
        if stack:
            product = product * (stack[-1] - i + 1) % 1000000007
        stack.append(i)
    print(product)


if __name__ == "__main__":
    main()
```

## Edge cases

- Equal seniority is not junior, so equal values are popped (`>=`).
- Chefs with no junior ahead multiply the product by 1.
- The value $K$ in the input is not needed.
- Take the product modulo $10^9 + 7$ as it grows.

## Dry run

`A = [1, 2, 1, 2]`, scanning from the right.

| index | value | stack before (values) | junior | factor |
|---:|---:|---|---|---:|
| 4 | 2 | - | none | 1 |
| 3 | 1 | 2 | none (2 is popped) | 1 |
| 2 | 2 | 1 | index 3 | $3 - 2 + 1 = 2$ |
| 1 | 1 | 1, 2 | none (both popped) | 1 |

Answer 2.

---

Same problem grouped by topic: [../docs/stacks/CHFQUEUE.md](../docs/stacks/CHFQUEUE.md)
