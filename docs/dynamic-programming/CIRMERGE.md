[&larr; 642. Tetris](SPCP6.md) &middot; [Index](../../README.md) &middot; [686. Little Elephant and T-Shirts &rarr;](TSHIRTS.md)

# 679. Circular Merging

> CodeChef problem code [`CIRMERGE`](https://www.codechef.com/problems/CIRMERGE) &middot; difficulty **2208** &middot; time limit **5s**

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Interval merging on the doubled circle with Knuth optimisation |
| **Time** | $O(N^2)$ per test case |
| **Space** | $O(N^2)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

$N$ integers $A_1, A_2, \ldots, A_N$ are placed in a circle in such a way that for each valid $i$, $A_i$ and $A_{i+1}$ are adjacent, and $A_1$ and $A_N$ are also adjacent.

We want to repeat the following operation exactly $N-1$ times (until only one number remains):
- Select two adjacent numbers. Let's denote them by $a$ and $b$.
- Score $a+b$ penalty points.
- Erase both $a$ and $b$ from the circle and insert $a+b$ in the space between them.

What is the minimum number of penalty points we can score?

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $a_1, a_2, \ldots, a_N$.

**Output**
For each test case, print a single line containing one integer — the minimum number of penalty points.

**Constraints**
- $1 \le T \le 10$
- $2 \le N \le 400$
- $1 \le a_i \le 10^9$ for each valid $i$

**Subtasks**
**Subtask #1 (10 points):**
- $2 \le N \le 10$
- $a_i \le 10$ for each valid $i$

**Subtask #2 (10 points):**
- $2 \le N \le 25$
- $a_1, a_2, \ldots, a_N$ are distinct powers of $2$ (including $1$)

**Subtask #3 (10 points):** $2 \le N \le 100$

**Subtask #4 (70 points):** original constraints

## Constraints

- $1 \le T \le 10$
- $2 \le N \le 400$
- $1 \le a_i \le 10^9$ for each valid $i$

## Sample

**Sample input**

```
1
3
10 10 1
```

**Sample output**

```
32
```

<details><summary>Explanation</summary>

- $[10,10,1] \rightarrow [10, 11]$, penalty:  $11$
- $[10,11] \rightarrow [21]$, penalty:  $21$
- Total penalty: $11+21=32$

</details>

## Approach

On a line this is the classic stone-merging DP: the last merge joins a left block and a right block, so

$$\text{cost}(i, j) = \min_{i \le k < j} \bigl(\text{cost}(i, k) + \text{cost}(k+1, j)\bigr) + \text{sum}(i, j).$$

On a circle, the $N - 1$ merges use $N - 1$ of the $N$ adjacencies, so some adjacency is never merged across; cutting the circle there gives a line. Write the array twice and solve the linear problem for every interval of length up to $N$ in the doubled array; the answer is the best interval of length exactly $N$.

The plain DP is cubic. The weights are positive, so the cost function satisfies the quadrangle inequality and the optimal split point is monotone: $\text{opt}(i, j-1) \le \text{opt}(i, j) \le \text{opt}(i+1, j)$. Restricting the search for $k$ to that range (Knuth's optimisation) makes the total work quadratic.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        ring = [next(tokens) for _ in range(n)] * 2
        size = 2 * n
        prefix = [0]
        for value in ring:
            prefix.append(prefix[-1] + value)
        cost = [[0] * size for _ in range(size)]
        opt = [[0] * size for _ in range(size)]
        for i in range(size):
            opt[i][i] = i
        for length in range(2, n + 1):
            for i in range(size - length + 1):
                j = i + length - 1
                low = opt[i][j - 1]
                high = min(j - 1, opt[i + 1][j])
                best = 10 ** 30
                split = low
                for k in range(low, high + 1):
                    value = cost[i][k] + cost[k + 1][j]
                    if value < best:
                        best = value
                        split = k
                cost[i][j] = best + prefix[j + 1] - prefix[i]
                opt[i][j] = split
        out.append(str(min((cost[i][i + n - 1] for i in range(n)))))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N^2)$ per test case
- **Space:** $O(N^2)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- $N = 1$: no merge, penalty 0.
- $N = 2$: a single merge costing the total.
- Only intervals up to length $N$ are needed in the doubled array.
- Penalties can exceed 32 bits.

## Dry run

`A = [10, 10, 1]`, doubled `10 10 1 10 10 1`.

Length-2 costs: `20, 11, 11, 20, 11`. Length 3:

- `[10, 10, 1]`: $\min(0 + 11,\; 20 + 0) + 21 = 32$
- `[10, 1, 10]`: $\min(0 + 11,\; 11 + 0) + 21 = 32$
- `[1, 10, 10]`: $\min(0 + 20,\; 11 + 0) + 21 = 32$

Answer 32.

---

Same problem in rating order (#639 of 735): [../../by-rating/639-CIRMERGE.md](../../by-rating/639-CIRMERGE.md)
