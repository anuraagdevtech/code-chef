[&larr; 403. Bitwise Tuples](BITTUP.md) &middot; [Index](../../README.md) &middot; [416. The Vowel Matrix &rarr;](VOWMTRX.md)

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

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

**Output**
For each test case, print a single line containing one integer ― the number of interesting subsequences.

**Constraints**
- $1 \le T \le 10$
- $1 \le K \le N \le 50$
- $1 \le A_i \le 100$ for each valid $i$

**Subtasks**
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

## Edge cases

- **The minimum sum is forced** — it takes the $K$ smallest values — so the only freedom is *which* copies of the boundary value are chosen.
- **Only the tied boundary value is interchangeable.** Values strictly below the cut must all be taken, and values strictly above can never be, so the count is $\binom{\text{total copies of the cut}}{\text{copies used}}$.
- **All values distinct** (the sample) → exactly one interesting subsequence, since $\binom{1}{1} = 1$.
- **All values equal** → the answer is $\binom{N}{K}$, with the cut value being the only value there is.
- **$K = N$** → one subsequence, the whole array, which the formula gives as $\binom{c}{c} = 1$.
- **Subsequences are counted by index set, not by value**, which is exactly why identical values at different positions count separately.
- **$N \leq 50$**, so the binomial fits comfortably and `math.comb` needs no modular arithmetic.

## Dry run

Take $A = 1, 2, 2, 2, 5$ with $K = 3$, sorted as shown.

| step | value |
|---|---|
| the $K$ smallest | $1, 2, 2$ |
| boundary value (the $K$-th) | 2 |
| copies of $2$ in the whole array | 3 |
| copies of $2$ among the first $K$ | 2 |
| count | $\binom{3}{2} = 3$ |

The sample's own case, $1,2,3,4$ with $K = 2$, has a unique boundary copy and so answers `1`.

> CodeChef tags: `Mathematics`, `Algorithms`

---

Same problem in rating order (#378 of 486): [../../by-rating/378-CHEFINSQ.md](../../by-rating/378-CHEFINSQ.md)
