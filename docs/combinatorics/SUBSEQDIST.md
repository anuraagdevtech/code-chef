# 466. Add to Subsequence

> CodeChef problem code [`SUBSEQDIST`](https://www.codechef.com/problems/SUBSEQDIST) &middot; difficulty **1737** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Operations as bits of a distinguishing code |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

Chef has an array $A$ of length $N$.

In one operation, Chef can choose any [subsequence](https://en.wikipedia.org/wiki/Subsequence) of the array and any integer $X$ and then add $X$ to **all** the elements of the chosen subsequence.

Determine the **minimum** number of operations required to make all the elements of the array **distinct**.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains a single integer $N$ — the length of Array $A$.
    - Next line contains $N$ space-separated integers $A_1, A_2, A_3, \dots, A_N$ - denoting the array $A$.

**Output**

For each test case, output the **minimum** number of operations required to make all the elements distinct.

## Constraints

- $1 \leq T \leq 4000$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- Sum of $N$ over all test cases do not exceed $3 \cdot 10^5$

## Sample

**Sample input**

```
4
3
3 3 3
6
1 3 2 1 2 2
4
1 2 1 2
5
1 3 2 4 6
```

**Sample output**

```
2
2
1
0
```

<details><summary>Explanation</summary>

**Test case $1$:**
- Operation $1$: Choose the subsequence $\{A_1\}$ and add $X = 1$ to the elements. The array becomes $A = [4, 3, 3]$.
- Operation $2$: Choose the subsequence $\{A_2\}$ and add $X = 2$ to the elements. The array becomes $A = [4, 5, 3]$.

Thus, we require, minimum $2$ operations to make all the elements distinct.

**Test case $2$:**
- Operation $1$: Choose the subsequence $\{A_1, A_6\}$ and add $X = 4$ to the elements. The array becomes $A = [5, 3, 2, 1, 2, 6]$.
- Operation $2$: Choose the subsequence $\{A_3\}$ and add $X = 5$ to the elements. The array becomes $A = [5, 3, 7, 1, 2, 6]$.

Thus, we require, minimum $2$ operations to make all the elements distinct.

**Test case $3$:**
- Operation $1$: Choose the subsequence $\{A_3, A_4\}$ and add $X = 2$ to the elements. The array becomes $A = [1, 2, 3, 4]$.

Thus, we require, minimum $1$ operation to make all the elements distinct.

**Test case $4$:** All the elements are distinct. We need zero operations.

</details>

## Approach

After $k$ operations with increments $X_1, \ldots, X_k$, element $i$ has become

$$A_i + \sum_{j \in S_i} X_j$$

where $S_i \subseteq \{1, \ldots, k\}$ records which operations included it. So the operations act as **$k$ bits of a code** assigned to each element.

Two elements that started equal can only be separated if their codes differ, so a value occurring $m$ times needs $m$ distinct codes:

$$2^k \geq m \quad\Longleftrightarrow\quad k \geq \lceil \log_2 m \rceil$$

and the binding case is the largest multiplicity. That bound is achievable: pick the $X_j$ wildly separated (say $X_j = 10^{18} \cdot 4^{\,j}$), so distinct codes give distinct sums and elements from different original values never collide. Hence

$$\text{answer} = \lceil \log_2 (\max_v \mathrm{cnt}_v) \rceil$$

computed as `(m - 1).bit_length()`.

The key realisation is that one operation can fix *many* duplicate groups at once, since the chosen subsequence is arbitrary — so the answer depends only on the worst group, not on how many groups there are. The second sample shows this: $[1,3,2,1,2,2]$ has a pair of $1$s and a triple of $2$s, and the same two operations resolve both, giving $2$ rather than $1 + 2$.

The other samples: three equal elements need $2$ operations since $2^1 < 3$; two pairs need only $1$; and an already-distinct array needs none.

## Solution (Python)

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
        most = max(Counter(data[pos + 1:pos + 1 + n]).values())
        pos += 1 + n
        # k operations give 2^k distinct codes, and the worst group decides.
        out.append(str((most - 1).bit_length()))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$

## Edge cases

- **Each operation assigns every element one bit** — in the chosen subsequence or not — so after $k$ operations each element carries a $k$-bit code, and two equal elements are separated exactly when their codes differ.
- **So $k$ operations can split a group of equal values into at most $2^k$ classes**, making the answer $\lceil \log_2 m \rceil$ for the largest multiplicity $m$.
- **Only the worst group matters**, since the same $k$ operations serve every group at once — different groups need no separating from each other, as generic increments keep them apart.
- **Already distinct** (the fourth row) → $0$ operations, which `(1-1).bit_length()` gives as $0$.
- **A group of two needs one operation** (the third row), and a group of three needs two — the ceiling, not the floor.
- **`(m-1).bit_length()` is exactly $\lceil \log_2 m \rceil$** for $m \geq 1$, avoiding any floating-point logarithm.
- **The integer $X$ is chosen per operation and is unbounded**, which is what lets the codes translate into genuinely distinct values.

## Dry run

| array | multiplicities | largest | $\lceil \log_2 m \rceil$ |
|---|---|---:|---:|
| $3,3,3$ | $3$ | 3 | `2` |
| $1,3,2,1,2,2$ | $2, 1, 3$ | 3 | `2` |
| $1,2,1,2$ | $2, 2$ | 2 | `1` |
| $1,3,2,4,6$ | all $1$ | 1 | `0` |

For the first row, two operations give the three $3$s the codes $00$, $01$, $10$ — enough to separate them.

> CodeChef tags: `Algorithms`, `Constructive`

---

Same problem in rating order (#438 of 486): [../../by-rating/438-SUBSEQDIST.md](../../by-rating/438-SUBSEQDIST.md)
