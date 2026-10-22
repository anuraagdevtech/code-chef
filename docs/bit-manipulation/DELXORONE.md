[&larr; 273. Equal by XORing](EQBYXOR.md) &middot; [Index](../../README.md) &middot; [281. Positive or Negative Subarrays &rarr;](POSITNEG.md)

# 276. One-XOR Deletions

> CodeChef problem code [`DELXORONE`](https://www.codechef.com/problems/DELXORONE) &middot; difficulty **1516** &middot; time limit **2.5s**

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | Grouping by the value with its low bit dropped |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

Chef has with him an array $A$ of length $N$. In one move, he can delete any element from $A$.

Find the minimum number of deletions Chef must make so that the following condition holds:
- Let $B$ denote the resulting array, and $M$ be the length of $B$.
- Then, $B_i \oplus B_j \leq 1$ for every $1 \leq i, j \leq M$.

Here, $\oplus$ denotes the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) operation.

For example, $[3, 3, 3]$ and $[6, 7, 6, 7]$ are valid final arrays, while $[1, 2]$ and $[6, 7, 8]$ are not (because $1 \oplus 2 = 3$ and $7\oplus 8 = 15$, respectively).

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$, denoting the length of array $A$.
    - The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — the elements of array $A$.

**Output**

For each test case, output on a new line the answer: the minimum number of deletions required so that the given condition is satisfied.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 3\cdot 10^5$
- $0 \leq A_i \leq N$
- The sum of $N$ over all test cases won't exceed $3\cdot 10^5$.

## Sample

**Sample input**

```
4
4
2 2 2 2
5
3 4 3 4 4
5
1 2 3 4 0
6
5 5 5 6 6 6
```

**Sample output**

```
0
2
3
3
```

<details><summary>Explanation</summary>

**Test case $1$:** The given array already satisfies the condition, no deletions need to be done.

**Test case $2$:** Chef can delete both the $3$'s to make the array $[4, 4, 4]$, which satisfies the condition.

**Test case $3$:** Chef can use three moves as follows:
- Delete the $1$, the array is now $[2, 3, 4, 0]$.
- Delete the $4$, the array is now $[2, 3, 0]$.
- Delete the $0$, the array is now $[2, 3]$ which satisfies the condition.

It can be verified that using two or less deletions cannot give an array that satisfies the condition.

**Test case $4$:** Chef must either delete all the $5$'s or all the $6$'s.

</details>

## Approach

The condition $B_i \oplus B_j \leq 1$ for **every** pair means any two kept values differ in at most the lowest bit — their XOR is $0$ or $1$. Equivalently, all kept values share the same quotient when the low bit is removed:

$$\left\lfloor \frac{B_i}{2} \right\rfloor \text{ is the same for all } i \quad\Longleftrightarrow\quad B_i \gg 1 \text{ is constant}$$

So the surviving array is drawn from a single group $\{2g, 2g+1\}$, and the best we can do is keep the **largest** such group. The answer is

$$N - \max_g \#\{i : A_i \gg 1 = g\}$$

Framing the pairwise condition as a shared key is what turns this from an $O(N^2)$ compatibility check into one pass with a counter.

It is worth noting that the condition is on *all* pairs, not just adjacent ones, which is what forces a single group — a chain of pairwise-compatible values would otherwise allow drift.

Sample case 4 is the clearest: $[5,5,5,6,6,6]$ splits into $5 \gg 1 = 2$ and $6 \gg 1 = 3$, two groups of three. Keeping either costs three deletions. Note that $5 \oplus 6 = 3 > 1$, so the two groups genuinely cannot mix even though the values are adjacent integers — $5$ and $6$ straddle the group boundary.

Sample case 3, $[1,2,3,4,0]$, has groups $\{0,1\}$, $\{2,3\}$ and $\{4\}$ of sizes $2, 2, 1$, so three deletions.

Since $A_i \leq N$, a plain list indexed by $A_i \gg 1$ works as the counter and is faster than a dictionary.

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
        # Values are bounded by n, so a plain list beats a dictionary here.
        groups = [0] * (n // 2 + 2)
        for v in data[pos + 1:pos + 1 + n]:
            groups[int(v) >> 1] += 1
        pos += 1 + n
        # Every kept pair must XOR to 0 or 1, so they share v >> 1.
        out.append(str(n - max(groups)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$

## Edge cases

- **$B_i \oplus B_j \leq 1$ means the survivors agree on every bit but the lowest**, so they all share the same value of $v \gg 1$ — which turns the problem into "keep the largest such group".
- **The condition is required for *every* pair**, including $i = j$ (trivially $0$), so there is no chaining: a set of values that pairwise differ only in the low bit must all come from one group.
- **Already valid** (the first row, four copies of $2$) → $0$ deletions.
- **Two different values can coexist** when they are a $2k, 2k+1$ couple — the second row keeps the three $4$s, and a $4$ with a $5$ would have been equally fine.
- **$0$ is an ordinary value** and groups with $1$: the third row's $0$ and $1$ form a group of two.
- **$A_i \leq N$ is given**, so a plain list of $N/2 + 2$ counters beats a dictionary — and the bound is on $N$, not on a separate value limit.
- **Sum of $N \leq 3 \cdot 10^5$**, and the counter list is reallocated per case.

## Dry run

Fourth sample: $5, 5, 5, 6, 6, 6$.

| value | $v \gg 1$ | group |
|---:|---:|---|
| 5 | 2 | $\{4, 5\}$ |
| 6 | 3 | $\{6, 7\}$ |

| group key | count |
|---:|---:|
| 2 | 3 |
| 3 | 3 |

Largest group is $3$, so $6 - 3 = $ `3` deletions. Note $5 \oplus 6 = 3 > 1$, so the two groups cannot mix.

> CodeChef tags: `Data Structures`, `Arrays`

---

Same problem in rating order (#304 of 486): [../../by-rating/304-DELXORONE.md](../../by-rating/304-DELXORONE.md)
