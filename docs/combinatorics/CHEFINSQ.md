# 407. Chef and Interesting Subsequences 

> CodeChef problem code [`CHEFINSQ`](https://www.codechef.com/problems/CHEFINSQ) &middot; difficulty **1646** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Choosing among the tied boundary value |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

Chef has a sequence $A_1, A_2, \ldots, A_N$. This sequence has exactly $2^N$ subsequences. Chef considers a subsequence of $A$ *interesting* if its size is exactly $K$ and the sum of all its elements is minimum possible, i.e. there is no subsequence with size $K$ which has a smaller sum.

Help Chef find the number of interesting subsequences of the sequence $A$.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

### Output
For each test case, print a single line containing one integer ― the number of interesting subsequences.

### Constraints
- $1 \le T \le 10$
- $1 \le K \le N \le 50$
- $1 \le A_i \le 100$ for each valid $i$

### Subtasks
**Subtask #1 (30 points):** $1 \le N \le 20$

**Subtask #2 (70 points):** original constraints

## Constraints

- $1 \le T \le 10$
- $1 \le K \le N \le 50$
- $1 \le A_i \le 100$ for each valid $i$

## Sample

**Sample input**

```
1
4 2
1 2 3 4
```

**Sample output**

```
1
```

<details><summary>Explanation</summary>

**Example case 1:** There are six subsequences with length $2$: $(1, 2)$, $(1, 3)$, $(1, 4)$, $(2, 3)$, $(2, 4)$ and $(3, 4)$. The minimum sum is $3$ and the only subsequence with this sum is $(1, 2)$.

</details>

## Approach

The minimum sum is obtained by taking the $K$ smallest elements, so sort and look at where the cut falls. Let $v = A_{(K)}$ be the $K$-th smallest value. Everything strictly below $v$ is **forced** into the subsequence, and everything strictly above is forced out — swapping either way would change the sum.

The only freedom is among the copies of $v$ itself. If $v$ occurs $c$ times in the whole array and $u$ of them lie in the first $K$ sorted positions, then any $u$ of the $c$ copies may be chosen, and the sum is the same:

$$\text{answer} = \binom{c}{u}$$

Subsequences are indexed by position, so two choices of copies are different subsequences even though they produce the same multiset of values — which is exactly what the problem counts.

The sample has $A = [1,2,3,4]$ with $K = 2$. The cut value is $2$, which occurs once and is used once, giving $\binom{1}{1} = 1$: the subsequence $\{1,2\}$ is the unique minimiser.

The count only becomes interesting with ties. For $A = [1,2,2,2]$ with $K = 2$ the cut value $2$ occurs three times and one is used, giving $\binom{3}{1} = 3$. And for $A = [5,5,5]$ with $K = 2$ it is $\binom{3}{2} = 3$.

With $N \leq 50$ the binomial fits easily in Python's unbounded integers; $\binom{50}{25} \approx 1.3 \times 10^{14}$ needs 64-bit arithmetic in C++.

## Solution (Python)

```python
import sys
from math import comb


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        a = sorted(int(x) for x in data[pos + 2:pos + 2 + n])
        pos += 2 + n
        cut = a[k - 1]
        # Only the copies of the boundary value are interchangeable.
        out.append(str(comb(a.count(cut), a[:k].count(cut))))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N \log N)$ per test case
- **Space:** $O(N)$

> CodeChef tags: `Mathematics`, `Algorithms`
