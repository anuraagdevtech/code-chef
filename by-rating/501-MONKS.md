[&larr; 500. Chef Restaurant ](500-CHEFRES.md) &middot; [Index](README.md) &middot; [502. Palpal Strings &rarr;](502-PALPALS.md)

# 501. Monks

> [`MONKS`](https://www.codechef.com/problems/MONKS) &middot; difficulty **1776** &middot; time limit **2s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Keep the largest feasible prefix after sorting |
| **CodeChef tags** | `Algorithms`, `Greedy`, `Sorting` |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N\log N)$ per test case |
| **Space** | $O(N)$ |

## Question

There is a town with $N$ people and initially, the $i^{th}$ person has $A_i$ coins. However, some people of the town decide to become *monks*. If the $i^{th}$ person becomes a monk, then:
- He leaves the town thereby reducing the number of people in the town by $1$.
- He distributes $X$ $(0 \le X \le A_i)$ coins to the remaining people of the town (not necessarily equally). Note that each monk can freely choose his value of $X$, and different monks may choose different values of $X$.
- He takes the remaining $A_i - X$ coins with him.

For example, initially, if $A = [1, 3, 4, 5]$ and $4^{th}$ person decides to become a monk then he can leave the town and can give $2$ coins to the $1^{st}$ person, $1$ coin to the $2^{nd}$ person, no coins to the $3^{rd}$ person and take $2$ coins along with him while going. Now $A$ becomes $[3, 4, 4]$.

Determine the **minimum** number of people who have to become monks, so that in the end, everyone remaining in the town has an equal number of coins.

**Input**

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the number of people in the town.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ denoting the initial number of coins of everyone in the town.

**Output**

For each test case, output the minimum number of people who have to become monks, so that in the end, everyone remaining in the town has an equal number of coins.

## Constraints

- $1 \le T \le 10^5$
- $1 \le N \le 10^5$
- $1 \le A_i \le 10^9$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

## Sample

**Sample input**

```
3
4
6 6 6 6
3
5 1 4
5
2 1 2 1 1
```

**Sample output**

```
0
1
2
```

<details><summary>Explanation</summary>

**Test case $1$:** All the people already have an equal number of coins.

**Test case $2$:** The $2^{nd}$ person can become a monk and give his $1$ coin to the person with $4$ coins. After this, both the remaining people will have $5$ coins.

**Test case $3$:** One way of two people becoming monks is as follows:
- The $2^{nd}$ person becomes a monk, and takes his $1$ coin with him
- The $3^{rd}$ person becomes a monk, and gives one coin each to the $4^{th}$ and $5^{th}$ people

Everyone remaining in the town now has $2$ coins.

</details>

## Approach

Suppose $k$ people remain. Their final wealth is at least the largest initial wealth among them, so they require at least $k$ times that maximum coins. The entire town has only $S$ coins.

For any fixed $k$, keeping the $k$ poorest people minimises that maximum to sorted $A_{k-1}$. If $kA_{k-1}\le S$, the departing people can donate exactly the deficits and take the excess away. This condition is both necessary and sufficient. Maximise feasible $k$ and return $N-k$.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        a = sorted(int(next(tokens)) for _ in range(n))
        total = sum(a)
        keep = 1
        for k, value in enumerate(a, 1):
            if k*value <= total:
                keep = k
            else:
                break
        out.append(str(n-keep))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Edge cases

- Everyone can remain if all amounts are equal.
- At least one person can always remain.
- Donors may retain excess coins; exact divisibility of the town total is unnecessary.

## Dry run

For `[5,1,4]`, sorted amounts are `[1,4,5]`, total `10`. Keeping all three needs `15`, but keeping two needs `8`, so one monk suffices.

---

Same problem grouped by topic: [../docs/greedy/MONKS.md](../docs/greedy/MONKS.md)
