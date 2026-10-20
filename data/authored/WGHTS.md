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
