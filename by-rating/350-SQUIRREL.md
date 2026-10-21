# 350. Squirrel and chestnut

> [`SQUIRREL`](https://www.codechef.com/problems/SQUIRREL) &middot; difficulty **1611** &middot; time limit **0.5s** &middot; Jump from 2* to 3* (Level 3)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Binary Search |
| **Technique** | Searching time, with a greedy capacity check |
| **Complexity class** | Linear times polylog $O(n \log^2 n)$ |
| **Time** | $O(m \log m \log(\text{time}))$ per test case |
| **Space** | $O(m)$ |

## Question

There are n squirrel(s) waiting below the feet of m chestnut tree(s). The first chestnut of the i-th tree will fall right after T_i second(s), and one more every P_i second(s) after that. The “big mama” of squirrels wants them to bring their nest no less than k chestnuts to avoid the big storm coming, as fast as possible! So they are discussing to wait below which trees to take enough chestnuts in the shortest time. Time to move to the positions is zero, and the squirrels move nowhere after that.

**Request**

Calculate the shortest time (how many seconds more) the squirrels can take enough chestnuts.

**Input**

- The first line contains an integer t, the number of test cases, for each:
- The first line contains the integers m,n,k, respectively.

- The second line contains the integers T_i  (i=1..m), respectively.

- The third line contains the integers P_i  (i=1..m), respectively.

***(Each integer on a same line is separated by at least one space character, there is no added line between test cases)***

**Output**

For each test cases, output in a single line an integer which is the shortest time calculated.

## Constraints

- $0 \lt t \leq 20$
- $0 \lt m, n \leq 10,000$
- $0 \lt k \leq 10^7$
- $0 < T_i, P_i \leq 100$

## Sample

**Sample input**

```
2
3 2 5
5 1 2
1 2 1
3 2 5
5 1 2
1 1 1
```

**Sample output**

```
4
3
```

<details><summary>Explanation</summary>

**Test case $1$:** Two squirrels wait below trees $2$ and $3$.
- After $1$ second, a chestnut from tree $2$ falls. Total chestnuts the squirrels have is $1$.
- After $2$ seconds, a chestnut from tree $3$ falls. Total chestnuts the squirrels have is $2$.
- After $3$ seconds, two chestnuts fall from trees $2$ and $3$. Total chestnuts the squirrels have is $4$.
- After $4$ seconds, a chestnut from tree $3$ falls. Total chestnuts the squirrels have is $5$.

Total time to gather $5$ chestnuts is $4$ seconds.

**Test case $2$:** Two squirrels wait below trees $2$ and $3$.
- After $1$ second, a chestnut from tree $2$ falls. Total chestnuts the squirrels have is $1$.
- After $2$ seconds, two chestnuts fall from trees $2$ and $3$. Total chestnuts the squirrels have is $3$.
- After $3$ seconds, two chestnuts fall from trees $2$ and $3$. Total chestnuts the squirrels have is $5$.

Total time to gather $5$ chestnuts is $3$ seconds.

</details>

## Approach

Tree $i$ has dropped its first chestnut at second $T_i$ and one more every $P_i$ seconds after, so by second $S$ it has produced

$$c_i(S) = \begin{cases} 0 & S < T_i \\ \left\lfloor \dfrac{S - T_i}{P_i} \right\rfloor + 1 & \text{otherwise} \end{cases}$$

The $n$ squirrels station themselves under $n$ different trees, so the harvest at time $S$ is the sum of the **$n$ largest** $c_i(S)$.

Every $c_i$ is non-decreasing in $S$, so the harvest is too — which makes "enough by time $S$" a monotone predicate and **binary search on $S$** the natural tool.

Each probe computes the $m$ counts and sums the top $n$; `heapq.nlargest` does that without a full sort when $n \ll m$.

The search bound deserves a thought. With $k$ up to $10^7$, a single tree, and $P_i$ up to $100$, the answer can reach about $10^9$ — so the upper limit is set there rather than at something comfortable, and roughly $30$ probes cover it.

The two samples differ only in one period, which is enough to move the answer. In the first, the trees have periods $1, 2, 1$ and by second $4$ the best two have produced $3 + 2 = 5$. In the second, speeding the middle tree to period $1$ lets the best two reach $3 + 2 = 5$ a second earlier.

Note the floor-plus-one: a tree that has just dropped its first chestnut at exactly $S = T_i$ counts as one, not zero.

## Solution

```python
import sys
import heapq


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        m, n, k = int(data[pos]), int(data[pos + 1]), int(data[pos + 2])
        times = [int(v) for v in data[pos + 3:pos + 3 + m]]
        periods = [int(v) for v in data[pos + 3 + m:pos + 3 + 2 * m]]
        pos += 3 + 2 * m

        def harvest(s):
            counts = [(s - ti) // pi + 1 for ti, pi in zip(times, periods) if s >= ti]
            # Squirrels occupy n different trees, so take the n best.
            return sum(heapq.nlargest(n, counts)) if counts else 0

        lo, hi = 0, 10 ** 9 + 200
        while lo < hi:
            mid = (lo + hi) // 2
            if harvest(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        out.append(str(lo))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/binary-search/SQUIRREL.md](../docs/binary-search/SQUIRREL.md)
