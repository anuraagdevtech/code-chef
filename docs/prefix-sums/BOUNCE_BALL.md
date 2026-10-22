# 298. Bouncing Ball

> CodeChef problem code [`BOUNCE_BALL`](https://www.codechef.com/problems/BOUNCE_BALL) &middot; difficulty **1607** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Prefix Sums |
| **Technique** | Alternating hits balance two totals |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

You are given an array $A$ of length $N$, where each element represents either empty ground ($A_i = 0$) or a wall (a positive integer indicating the height of the wall).

You can place a ball on any empty ground (that is, choose an index $i$ with $A_i = 0$) and push it either to the right or to the left.
When the ball hits a wall, it decreases the height of the wall it hit by $1$, and then bounces back in the opposite direction. If the wall's height reaches $0$, it becomes empty ground.
The ball continues to move until it goes out of bounds.

Determine the number of ways to place and push the ball so that all walls are destroyed. Two ways are considered different if either the starting index of the ball or the direction of the push is different.

**Input**

- The first line contains a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$, denoting the size of the array $A$.
    - The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
$A_i = 0$ means the $i$-th position is empty ground, and $A_i \gt 0$ denotes a wall of height $A_i$ at position $i$.

**Output**

For each test case, print on a new line a single integer representing the number of ways all walls can be destroyed.

## Constraints

- $1 \leq T \leq 10^4$
- $3 \leq N \leq 10^5$
- $0 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

**Subtasks**

- **Subtask 1 (10 points):** $1 \leq M \leq 10$
- **Subtask 2 (20 points):** The sum of $N$ across all test cases won't exceed $20$.
- **Subtask 3 (70 points):** No further constraints.

## Sample

**Sample input**

```
4
4
1 0 0 2
5
1 1 0 1 1
5
2 4 0 5 0
3
1000 0 999
```

**Sample output**

```
2
2
1
1
```

<details><summary>Explanation</summary>

**Test case $1$:** The ball can be placed at position $2$ or $3$ and pushed to the right.
- The ball hits the wall at position $4$, making its height $1$. It then bounces to the left direction.
- The ball hits the wall at position $1$, making its height $0$. It then bounces in the right direction.
- The ball hits the wall at position $4$, making its height $0$. Now, all the walls have height $0$.

It can be shown that there are no other ways to destroy all the walls.

</details>

## Approach

A ball launched from an empty cell strikes walls **alternately**: one on the side it was pushed toward, then one on the other side, and so on, each strike removing exactly one unit of height. It leaves the array the moment it travels toward a side with nothing left.

So only the **total wall height on each side** matters. Let $L$ and $R$ be the sums to the left and right of the starting index.

Pushed right, the strikes land R, L, R, L, …. For every wall to be destroyed, the alternation must consume both totals exactly:

- $R = L$ — the strikes pair off perfectly, and after the final left strike the ball turns right into an empty array;
- $R = L + 1$ — one extra right strike leads the sequence, and after it the ball turns left into nothing.

Any other relationship strands height on one side. So pushing right succeeds exactly when $R - L \in \{0, 1\}$, and by symmetry pushing left succeeds when $L - R \in \{0, 1\}$.

Counting per empty cell: both directions work when $L = R$ (contributing $2$), exactly one works when the totals differ by one, and nothing works otherwise.

Prefix sums give $L$ and $R$ for every index in one pass.

Sample case 2, $[1,1,0,1,1]$, has the only gap perfectly balanced at $L = R = 2$, so both pushes work — answer $2$. Sample case 3's second gap has $L = 11$ against $R = 0$ and contributes nothing, while the first gap differs by exactly one and contributes a single way.

Heights reach $10^9$ with $N$ up to $10^5$, so the side totals reach $10^{14}$ — **64-bit** territory outside Python.

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
        total = sum(a)
        ways = 0
        left = 0
        for v in a:
            if v == 0:
                right = total - left
                # Strikes alternate, so the two sides must differ by 0 or 1.
                if left == right:
                    ways += 2
                elif abs(left - right) == 1:
                    ways += 1
            left += v
        out.append(str(ways))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$

## Edge cases

- **The hits alternate sides, so the two totals must nearly balance.** Pushed right, the ball spends hits on the right and left alternately, taking $\lceil k/2 \rceil$ from the right of $k$ total — so clearing everything needs $R = L$ or $R = L + 1$.
- **Equal totals give two ways**, since either direction works; a difference of one gives exactly one way, pushing toward the heavier side. That is the whole counting rule.
- **A difference above one gives nothing**, however large the totals: the third row has $6$ against $5$ at one zero (one way) and $11$ against $0$ at the other (none).
- **Every empty cell is a candidate**, and two adjacent zeros can both count — the first row's positions $2$ and $3$ each give one way, for a total of $2$.
- **Walls of height above $1$ take several hits**, which is why the totals are sums of heights rather than counts of walls (the last row balances $1000$ against $999$).
- **The running left total must be updated after the test**, so the zero cell itself contributes nothing to either side.
- **Sum of $N \leq 2 \cdot 10^5$**: one pass with a running prefix and the precomputed grand total.

## Dry run

First sample: $A = 1, 0, 0, 2$, total wall height $3$.

| position | left total | right total | difference | ways |
|---:|---:|---:|---:|---:|
| 2 | 1 | 2 | 1 | 1 (push right) |
| 3 | 1 | 2 | 1 | 1 (push right) |

Output `2`. From position $2$ pushed right: hit the wall at $4$ (height $2 \to 1$), bounce left, hit the wall at $1$ ($1 \to 0$), bounce right, hit $4$ again ($1 \to 0$) — all clear.

> CodeChef tags: `Algorithms`, `Simple Algos`

---

Same problem in rating order (#345 of 486): [../../by-rating/345-BOUNCE_BALL.md](../../by-rating/345-BOUNCE_BALL.md)
