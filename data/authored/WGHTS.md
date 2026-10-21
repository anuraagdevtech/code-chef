---
topic: Brute Force
subtopic: Enumerating every non-empty subset
time: $O(2^k)$ per test case with $k = 3$, so $O(1)$
space: $O(1)$
---
Chef may use **one or more** of the three weights, so the reachable totals are the sums of the non-empty subsets of $\{X, Y, Z\}$. With three weights there are $2^3 - 1 = 7$ of them:

$$X,\quad Y,\quad Z,\quad X+Y,\quad X+Z,\quad Y+Z,\quad X+Y+Z$$

Seven candidates is small enough to list outright, and because the set is fixed the cost is constant per test case.

The phrase "one or more" is what excludes the empty subset — a weight of $0$ is not measurable, and since $W \geq 1$ it could never match anyway. It also means every single weight counts on its own, which sample case 2 relies on: $W = 7$ matches the weight $7$ directly, with the others unused.

Rather than hard-coding seven expressions, the code uses `itertools.combinations` over sizes $1$ to $3$. That is the same seven sums, written in a form that would extend unchanged to more weights — and it is the honest way to express "any subset" so the reader sees the structure rather than a list of special cases.

It is worth noting what the problem does *not* ask. In classic balance-scale puzzles, weights may be placed on either pan, which allows **differences** such as $Y - X$ and turns this into a different question. Here weights only add. Sample case 4 confirms it: $20$ is unreachable from $\{10, 11, 12\}$ by addition, even though $10 + 12 - 11 = 11$ and other signed combinations exist.

For a larger weight set this approach would become $O(2^k)$ and a subset-sum DP would take over; at $k = 3$ enumeration is exactly right.

## Edge cases

- **A single weight equals $W$** ($W = 7$ with weights $9, 7, 2$): reachable by a one-element subset, so subsets of size $1$ must be included and not just pairs and triples.
- **Only all three together work**: the size-$3$ subset must be considered too.
- **Nothing works** ($W = 20$ from $10, 11, 12$: the reachable sums are $10, 11, 12, 21, 22, 23, 33$): `NO`.
- **Weights only add.** They all go on one pan, so differences are unavailable — this is why $W = 5$ is unreachable from $2, 1, 6$ even though $6 - 1 = 5$. The sample's first row is that trap.
- With three weights there are only $7$ non-empty subsets, so brute force is exact and trivially fast.

## Dry run

Row 1: $W = 5$ with weights $2, 1, 6$. All seven subset sums:

| subset | $\{2\}$ | $\{1\}$ | $\{6\}$ | $\{2,1\}$ | $\{2,6\}$ | $\{1,6\}$ | $\{2,1,6\}$ |
|---|---:|---:|---:|---:|---:|---:|---:|
| sum | 2 | 1 | 6 | 3 | 8 | 7 | 9 |

$5$ appears nowhere, so `NO`. Row 2 ($W = 7$ from $9, 7, 2$) matches the singleton $\{7\}$, and row 3 ($W = 20$ from $8, 10, 12$) matches $\{8, 12\}$.
