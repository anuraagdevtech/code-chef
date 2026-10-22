# 320. Pair Sort Version 3

> CodeChef problem code [`PSORT3`](https://www.codechef.com/problems/PSORT3) &middot; difficulty **unrated** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | Mixed-direction composite key |
| **Time** | $O(N \log N)$ |
| **Space** | $O(N)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

## Question

You are given two arrays $A$ and $B$ of size $N$. We define a pair as $(A_i$, $B_i)$ where $0 \le i \le N - 1$.

The task is to sort these pairs in **decreasing** order of the second elements of the pairs i.e $B_i$. If both the second elements are equal sort according to **increasing** order of the first elements of the pairs.

Output the sorted pairs in a single line with a space separating the pairs. Each pair is printed with first element followed by a space and second element. See Explanation Section for better understanding.

**Input:**
- First line will contain a single integer $N$.
- Second line contains $N$ space separated integers $A_0$, $A_1$, $...$ $A_{N - 1}$ denoting the elements of array $A$.
- Third line contains $N$ space separated integers $B_0$, $B_1$, $...$ $B_{N - 1}$ denoting the elements of array $B$.

**Output:**
Output in a single line $2 * N$ space separated integers. Output the pairs in sorted order, where the first element of a pair is from $A_j$ and second element is from $B_j$ with a space in between.

**Constraints**
- $1 \leq N \leq 10^5$
- $1 \leq A_i, B_i \leq 10^{18}$

**Subtasks**
- 30 points : $1 \leq N \leq 1000$
- 70 points : Original constraints

## Constraints

- $1 \leq N \leq 10^5$
- $1 \leq A_i, B_i \leq 10^{18}$

## Sample

**Sample input**

```
3
2 2 3
6 3 3
```

**Sample output**

```
2 6 2 3 3 3
```

<details><summary>Explanation</summary>

The pairs are:
- $(2, 6)$
- $(2, 3)$
- $(3, 3)$

We are required to sort these pairs in decreasing order of second elements and then increasing order of first elements. Therefore, pairs sorted:
- $(2, 6)$
- $(2, 3)$
- $(3, 3)$

You can clearly see that the **second elements are in decreasing order from top to bottom** and when second elements of two pairs are equal they are **sorted in increasing order of first elements from top to bottom**. We print the pairs as follows:

$2\ 6\ 2\ 3\ 3\ 3$

The first two elements correspond to pair 1 in sorted list. The next two elements correspond to pair 2 in sorted list. The last two elements correspond to pair 3 from sorted list.

</details>

## Approach

Two sort levels pointing in **opposite directions**: the second element descending, and ties broken by the first element ascending.

Python sorts tuples ascending throughout, so the descending field is handled by negating it:

$$\text{key} = (-B_i,\ A_i)$$

Negation is clean here because the values are integers; for a non-numeric field the alternative is `sorted(..., reverse=True)` on one pass followed by a stable sort on the other, which is more error-prone.

The sample is built to expose a wrong tie-break. Pairs $(2,6), (2,3), (3,3)$ sort to $(2,6)$ first on the descending $B$, then the two with $B = 3$ are ordered by **ascending** $A$, giving $(2,3)$ before $(3,3)$. A uniform `reverse=True` would wrongly place $(3,3)$ first.

Output is a single flat line of $2N$ integers — each pair printed as its first element then its second, with no separators beyond spaces. Flattening with a generator and one `" ".join` avoids building the string incrementally.

Values reach $10^{18}$, which is inside unsigned 64-bit but at the edge of signed — worth noting that negating such a value for the sort key is safe in Python but would need care in a fixed-width language, where a comparator function is the better route.

With $N$ up to $10^5$ the sort dominates; bulk I/O matters more than the comparison itself.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])                 # no test-case count
    a = [int(v) for v in data[1:1 + n]]
    b = [int(v) for v in data[1 + n:1 + 2 * n]]
    # Second element descending, first ascending on ties.
    pairs = sorted(zip(a, b), key=lambda p: (-p[1], p[0]))
    out = []
    for first, second in pairs:
        out.append(str(first))
        out.append(str(second))
    sys.stdout.write(" ".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N \log N)$
- **Space:** $O(N)$

## Edge cases

- **The two keys pull in opposite directions**, so the sort key negates the second component and leaves the first positive: descending by $B_i$, ascending by $A_i$ on ties.
- **Negation is safe here** because the values are positive integers — on an unbounded or floating type a reverse comparator would be the sturdier choice.
- **The tie-break is genuinely exercised** by the sample: two pairs share $B_i = 3$ and are ordered by their first components, $2$ before $3$.
- **The pairs come from two separate arrays**, zipped by index — not read as interleaved pairs.
- **The output is one flat line** of $2N$ numbers, each pair's components adjacent.
- **$A_i, B_i$ up to $10^{18}$**, so the keys stay exact in Python where a float key would lose precision.
- **There is no test-case count**: the input is $N$, then array $A$, then array $B$.

## Dry run

Sample: $A = 2, 2, 3$ and $B = 6, 3, 3$.

| pair | sort key $(-B_i,\, A_i)$ |
|---|---|
| $(2, 6)$ | $(-6, 2)$ |
| $(2, 3)$ | $(-3, 2)$ |
| $(3, 3)$ | $(-3, 3)$ |

Sorted: $(2,6)$, then $(2,3)$ before $(3,3)$ on the tie. Output `2 6 2 3 3 3`.

---

Same problem in rating order (#480 of 486): [../../by-rating/480-PSORT3.md](../../by-rating/480-PSORT3.md)
