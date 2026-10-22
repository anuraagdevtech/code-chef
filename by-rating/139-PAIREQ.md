[&larr; 138. Shoe Fit](138-SHOEFIT.md) &middot; [Index](README.md) &middot; [140. Chef and Pairing Slippers &rarr;](140-CHEFSLP.md)

# 139. Make all equal using Pairs

> [`PAIREQ`](https://www.codechef.com/problems/PAIREQ) &middot; difficulty **928** &middot; time limit **1s** &middot; Level up from 1* to 2* (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Keep the most frequent value |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

Chef has an array $A$ of length $N$.

In one operation, Chef can choose any two **distinct** indices $i, j$ $(1 \leq i, j \leq N, i \neq j)$ and **either** change $A_i$ to $A_j$ **or** change $A_j$ to $A_i$.

Find the **minimum** number of operations required to make all the elements of the array **equal**.

**Input**

- First line will contain $T$, number of test cases. Then the test cases follow.
- First line of each test case consists of an integer $N$ - denoting the size of array $A$.
- Second line of each test case consists of $N$ space-separated integers $A_1, A_2, \dots, A_N$ - denoting the array $A$.

**Output**

For each test case, output the minimum number of operations required to make all the elements equal.

## Constraints

- $1 \leq T \leq 100$
- $2 \leq N \leq 1000$
- $1 \leq A_i \leq 1000$

## Sample

**Sample input**

```
4
3
1 2 3
4
5 5 5 5
4
2 2 1 1
3
1 1 2
```

**Sample output**

```
2
0
2
1
```

<details><summary>Explanation</summary>

**Test Case $1$:** You can make all the elements equal in $2$ operations. In the first operation, you can choose indices $1, 2$ and convert $A_1$ to $A_2$. So the array becomes $[2, 2, 3]$. Now you can choose indices $1, 3$ and convert $A_3$ to $A_1$, so the final array becomes $[2, 2, 2]$.

**Test Case $2$:** Since all the elements are already equal there is no need to perform any operation.

**Test Case $3$:** You can make all the elements equal in $2$ operations. In the first operation, you can choose indices $1, 3$ and convert $A_1$ to $A_3$. So the array becomes $[1, 2, 1, 1]$. Now you can choose indices $1, 2$ and convert $A_2$ to $A_1$, so the final array becomes $[1, 1, 1, 1]$.

**Test Case $4$:** You can make all the elements equal in $1$ operation. You can pick indices $2, 3$ and convert $A_3$ to $A_2$ after which the array becomes $[1, 1, 1]$.

</details>

## Approach

Each operation overwrites one element with the value of another, so it fixes **exactly one** mismatched element per move. The final common value must be one already present in the array, since the operation only ever copies existing values.

To minimise moves, choose the value that is already most common and overwrite everything else:

$$N - \max_v (\text{count of } v)$$

The lower bound is clear — every element not already equal to the target needs its own operation — and the construction matches it, so the bound is tight. Choosing any less frequent value would only leave more elements to fix.

`collections.Counter(...).most_common(1)` gives the modal frequency in one pass.

Sample case 1, $[1,2,3]$, has every value unique, so the mode count is $1$ and two operations are needed. Sample case 3, $[2,2,1,1]$, has a tie at frequency $2$; either value works and the answer is $2$ — ties need no tie-breaking, since only the count enters the formula.

Sample case 2 is already uniform, needing $0$ operations, which the formula gives without a special case.

The requirement that $i \neq j$ never binds, because $N \geq 2$ guarantees a second index exists to copy from. If the array were a single element it would already be uniform anyway.

## Solution

```python
import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        counts = Counter(data[pos + 1:pos + 1 + n])
        pos += 1 + n
        # Keep whichever value is already most common; fix the rest one by one.
        out.append(str(n - max(counts.values())))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Already all equal** ($5,5,5,5$): zero operations.
- **All distinct** ($1,2,3$): $N-1$ operations, the worst case.
- **A tie for most frequent** ($2,2,1,1$): either value may be kept and the cost is the same, so no tie-break is needed.
- **Keeping the most frequent value is what minimises the work** — keeping any other value costs strictly more, which is why the answer is $N$ minus the maximum count rather than $N$ minus any count.
- $N \geq 2$, so there is always at least one pair to work with.

## Dry run

| array | counts | most frequent | $N - \max$ | output |
|---|---|---:|---:|---|
| $1,2,3$ | $1,1,1$ | 1 | 2 | `2` |
| $5,5,5,5$ | $4$ | 4 | 0 | `0` |
| $2,2,1,1$ | $2,2$ | 2 | 2 | `2` |
| $1,1,2$ | $2,1$ | 2 | 1 | `1` |

Row 3 has two values tied at two apiece, and both choices cost the same.

---

Same problem grouped by topic: [../docs/arrays/PAIREQ.md](../docs/arrays/PAIREQ.md)
