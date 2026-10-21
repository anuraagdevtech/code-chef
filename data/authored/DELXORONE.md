---
topic: Bit Manipulation
subtopic: Grouping by the value with its low bit dropped
time: $O(N)$ per test case
space: $O(N)$
---
The condition $B_i \oplus B_j \leq 1$ for **every** pair means any two kept values differ in at most the lowest bit — their XOR is $0$ or $1$. Equivalently, all kept values share the same quotient when the low bit is removed:

$$\left\lfloor \frac{B_i}{2} \right\rfloor \text{ is the same for all } i \quad\Longleftrightarrow\quad B_i \gg 1 \text{ is constant}$$

So the surviving array is drawn from a single group $\{2g, 2g+1\}$, and the best we can do is keep the **largest** such group. The answer is

$$N - \max_g \#\{i : A_i \gg 1 = g\}$$

Framing the pairwise condition as a shared key is what turns this from an $O(N^2)$ compatibility check into one pass with a counter.

It is worth noting that the condition is on *all* pairs, not just adjacent ones, which is what forces a single group — a chain of pairwise-compatible values would otherwise allow drift.

Sample case 4 is the clearest: $[5,5,5,6,6,6]$ splits into $5 \gg 1 = 2$ and $6 \gg 1 = 3$, two groups of three. Keeping either costs three deletions. Note that $5 \oplus 6 = 3 > 1$, so the two groups genuinely cannot mix even though the values are adjacent integers — $5$ and $6$ straddle the group boundary.

Sample case 3, $[1,2,3,4,0]$, has groups $\{0,1\}$, $\{2,3\}$ and $\{4\}$ of sizes $2, 2, 1$, so three deletions.

Since $A_i \leq N$, a plain list indexed by $A_i \gg 1$ works as the counter and is faster than a dictionary.

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
