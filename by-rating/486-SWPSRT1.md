# 486. Sort by swaps

> [`SWPSRT1`](https://www.codechef.com/problems/SWPSRT1) &middot; difficulty **unrated** &middot; time limit **1s** &middot; Jump from 2* to 3* (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | Selection sort meets the swap budget exactly |
| **Complexity class** | Quadratic $O(n^2)$ |
| **Time** | $O(n^2)$ |
| **Space** | $O(n)$ |

## Question

**Swap Sort**
You are given an array $A$ of size $n$ (not exceeding $500$), you are allowed a maximum of $n-1$ swaps where in each swap you can choose **any two** indices $i, j$ such that $0 \leq i, j \leq n-1$ and swap the values of $A_i$ and $A_j$.

Note that you **do not** need to minimise the number of swaps, and you are also **not required** to optimize the time complexity (note that the constraints allow solutions that are $\mathcal{O}(n^2)$ as well), however you **cannot** swap more than $n-1$ times.

There may be many solutions, you can output **any** of them.

**Input**
The first line contains a single integer $n$, the number of elements in the array

The second line contains $n$ space separated integers, the elements of the array

**Output**
In the first line print the number of swaps you need to perform, let this number be $m$.

In the next $m$ lines, print two space separated integers $i, j$ such that $0 \leq i, j \leq n-1$.

After performing the swaps in the order in which your program gives the output, the array should become sorted in increasing order.
(i.e. $A_i \geq A_{i-1}$ for every $i$ in the range $[1, n-1]$).

**Constraints**
$1 \leq n \leq 500$

$-10^9 \leq A_i \leq 10^9$

## Constraints

$1 \leq n \leq 500$
$-10^9 \leq A_i \leq 10^9$

## Sample

**Sample input**

```
3
3 2 1
```

**Sample output**

```
1
0 2
```

<details><summary>Explanation</summary>

After the first swap, the elements $A_0$ and $A_2$ are swapped, and the array becomes sorted, i.e. $\{1, 2, 3\}$

</details>

## Approach

The budget is $n-1$ arbitrary swaps, and **selection sort** fits it precisely.

For each position $i$ from $0$ upward, find the minimum of the unsorted suffix and swap it into place. That is at most one swap per position, and the final position needs none — so at most $n-1$ swaps, matching the limit exactly.

The reason selection sort is the right tool rather than, say, bubble sort is that the swaps are **unrestricted**: any two indices may be exchanged. Bubble sort only swaps neighbours and can need $\binom{n}{2}$ of them, blowing the budget. Selection sort exploits the freedom to move an element directly to its destination.

A swap is skipped when the minimum is already in place, so the reported count can be fewer than $n-1$ — the problem asks only that it not exceed the budget, not that it be minimal.

With $n \leq 500$ the $O(n^2)$ scan is trivially fast, and the statement explicitly permits it.

The output format is the count $m$ followed by $m$ lines of index pairs, applied in order. For the sample $[3,2,1]$ this gives a single swap of positions $0$ and $2$, matching the published answer — though **any valid sequence is accepted**, so this is judged by a checker that replays the swaps and confirms the result is sorted and within budget.

Duplicate values need no special handling: selection sort places equal elements in some order, and the problem asks only for non-decreasing output, not stability.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])                 # no test-case count
    a = [int(v) for v in data[1:1 + n]]
    swaps = []
    # Selection sort: at most one swap per position, so at most n - 1 total.
    for i in range(n - 1):
        lo = min(range(i, n), key=lambda j: a[j])
        if lo != i:
            a[i], a[lo] = a[lo], a[i]
            swaps.append((i, lo))
    out = [str(len(swaps))]
    out.extend(f"{i} {j}" for i, j in swaps)
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Selection sort fits the budget exactly.** Each of the first $n-1$ positions is fixed with at most one swap, so the total never exceeds $n-1$ — which is precisely the allowance.
- **A position already holding its minimum is skipped**, so the count can be well below $n-1$ — the sample uses just one swap for three elements.
- **The swaps may use any two indices**, not only adjacent ones, which is what lets selection sort apply at all.
- **Minimisation is explicitly not required**, so there is no need to count inversions or find the cycle decomposition — any sequence within budget is accepted.
- **The reported pairs must be replayable in order**, which the emission order guarantees.
- **An already-sorted array yields zero swaps**, and the output is the count alone.
- **Equal elements need no swap**, since `min` picks the earliest index among ties and the guard then skips it.
- **$n \leq 500$** makes the quadratic scan trivial, and the statement explicitly permits it.

## Dry run

Sample: $A = 3, 2, 1$.

| position | smallest in the suffix | at index | swap? | array after |
|---:|---:|---:|---|---|
| 0 | 1 | 2 | yes, $(0, 2)$ | $1, 2, 3$ |
| 1 | 2 | 1 | no | $1, 2, 3$ |

One swap, so the output is `1` then `0 2`.

---

Same problem grouped by topic: [../docs/sorting/SWPSRT1.md](../docs/sorting/SWPSRT1.md)
