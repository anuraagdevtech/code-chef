# 175. Make them equal

> CodeChef problem code [`MAKEEQUAL`](https://www.codechef.com/problems/MAKEEQUAL) &middot; difficulty **1267** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Bounded by the widest gap |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | Level up from 1* to 2* (Level 2) |

## Question

Chef has an array $A$ having $N$ elements. Chef wants to make all the elements of the array equal by repeating the following move.

- Choose any integer $K$ between $1$ and $N$ (inclusive). Then choose $K$ distinct indices $i_1 , i_2, \dots, i_K$, and increase the values of $A_{i_1} , A_{i_2} , \dots , A_{i_K}$ by $1$.

Find the minimum number of moves required to make all the elements of the array equal.

**Input**

- The first line contains $T$ denoting the number of test cases. Then the test cases follow.
- The first line of each test case contains a single integer $N$ denoting the number of elements in $A$.
- The second line of each test case contains $N$ space separated integers $A_1, A_2, \dots, A_N$.

**Output**

For each test case, print a single line containing one integer denoting the minimum number of moves required to make all the elements of the array equal.

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^5$
- The sum of $N$ over all test cases does not exceed $10^5$.

## Sample

**Sample input**

```
2
3
1 3 1
3
2 2 2
```

**Sample output**

```
2
0
```

<details><summary>Explanation</summary>

- **Test Case $1$**: In the first move, Chef can choose $K = 2$, and choose the indices $\{1 , 3\}$. After increasing $A_1$ and $A_3$ by $1$, the array will become $[2 , 3 , 2]$.
In the second move, Chef can choose $K = 2$, and choose the indices $\{1 , 3\}$. After increasing $A_1$ and $A_3$ by $1$, the array will become $[3 , 3 , 3]$, and hence all the elements become equal.

- **Test Case $2$**: All the elements of the array are equal, hence no move is required.

</details>

## Approach

A move raises any chosen subset of elements by $1$ — so in a single move, **every** element that still needs raising can be raised at once. There is no cost to touching more indices.

That makes the answer easy. Since values only increase, the common target must be at least $\max(A)$, and choosing exactly $\max(A)$ is optimal. The element needing the most work is the smallest one, requiring $\max(A) - \min(A)$ increments. Every other element needs fewer, so it can simply sit out the final moves. Hence

$$\text{moves} = \max(A) - \min(A)$$

The lower bound is clear — the minimum element gains at most $1$ per move — and the construction matches it, so the bound is tight.

The trap is treating this as a sum. Totalling $\sum (\max - A_i)$ counts individual increments, not moves, and would answer $4$ on sample case 1 instead of $2$. The freedom to choose $K$ and update many indices simultaneously is precisely what collapses the sum into a maximum.

Sample case 1 has $\max = 3$ and $\min = 1$, so $2$ moves: raise both $1$s together, twice. Sample case 2 is already uniform and needs none.

Aiming above $\max(A)$ would only add moves, so there is no reason to consider a higher target.

One pass computes both extremes, giving $O(N)$ time and $O(1)$ space — appropriate given the sum of $N$ reaches $10^5$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = [int(v) for v in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        # One move can raise every lagging element at once, so only the
        # widest gap matters - not the total shortfall.
        out.append(str(max(a) - min(a)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$

## Edge cases

- **One move raises every lagging element at once**, so the cost is the single widest gap, not the total shortfall. The first row needs $2$; summing the per-element deficits ($2 + 0 + 2$) gives $4$.
- **Already equal** (the second row) → $0$, which $\max - \min$ gives with no special case.
- **$N = 1$**: maximum and minimum coincide, so the answer is $0$.
- **The target is forced to be $\max(A)$** — raising elements only, so nothing below the maximum can be the common value, and every element must climb to it.
- **Sum of $N$ bounded by $10^5$** across up to $10^4$ cases, so one pass per case with no sorting.

## Dry run

| input | max | min | gap | output |
|---|---:|---:|---:|---|
| $1, 3, 1$ | 3 | 1 | 2 | `2` |
| $2, 2, 2$ | 2 | 2 | 0 | `0` |

In the first row both $1$s rise together on each of the two moves.

---

Same problem in rating order (#195 of 486): [../../by-rating/195-MAKEEQUAL.md](../../by-rating/195-MAKEEQUAL.md)
