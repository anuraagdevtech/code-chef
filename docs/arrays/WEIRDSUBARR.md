[&larr; 460. Box of Chocolates](CHCBOX.md) &middot; [Index](../../README.md)

# 470. Weird Subarrays

> CodeChef problem code [`WEIRDSUBARR`](https://www.codechef.com/problems/WEIRDSUBARR) &middot; difficulty **1739** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Counting valley subarrays from run lengths |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

An array $A$ is called *weird* if it can be sorted in non-decreasing order by applying the given operation any number of times:
- Select any index $i$ $(1 \le i \le |A|)$ and set $A_i := -A_i$.

For example: $A = [2, 1, 3]$ is *weird* since after applying the operation at $i = 1$, $A$ becomes $[-2, 1, 3]$ which is sorted.

JJ has a permutation $P$ of length $N$. He wants to find the number of subarrays of $P$ which are *weird*. Can you help him?

**Input**

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the size of the permutation $P$.
- The second line of each test case contains $N$ space-separated integers $P_1, P_2, \dots, P_N$ denoting the permutation $P$.

**Output**

For each test case, output on a new line the number of *weird* subarrays of $P$.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $P$ is a permutation.
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

## Sample

**Sample input**

```
3
3
2 3 1
3
2 1 3
4
1 2 3 4
```

**Sample output**

```
5
6
10
```

<details><summary>Explanation</summary>

**Test Case 1:** Weird subarrays of $P$ are: $[2], [3], [1], [2, 3], [3, 1]$.

**Test Case 2:** Weird subarrays of $P$ are: $[2], [1], [3], [2, 1], [1, 3], [2, 1, 3]$.

</details>

## Approach

Negating an element makes it negative, and every value here is a positive distinct integer, so in a sorted result all the negated elements come first. Their negatives must be non-decreasing, i.e. their **magnitudes decreasing**, and the untouched suffix must be increasing. So a subarray is weird exactly when it is a **valley**: strictly decreasing, then strictly increasing.

Count valleys by right endpoint. Let $\mathrm{inc}[R]$ be the length of the maximal strictly increasing run ending at $R$, and $m = R - \mathrm{inc}[R] + 1$ its start — the valley's turning point is forced to be $m$, since the increasing arm cannot reach further left. The decreasing arm then extends from $m$ back as far as $\mathrm{dec}[m]$, the maximal strictly decreasing run ending at $m$. So the valid left endpoints are $[\,m - \mathrm{dec}[m] + 1,\ R\,]$ and

$$\#\{\text{valleys ending at } R\} = R - m + \mathrm{dec}[m]$$

Both run-length arrays build in one pass each, so the whole count is linear — no $O(N^2)$ scan over pairs.

Note the turning point is shared by both arms, which is why a single element counts (both arms have length $1$) and why the formula needs no special case for a purely increasing or purely decreasing subarray.

The samples: $[2,3,1]$ gives $1 + 2 + 2 = 5$, excluding only the whole array — $2, 3, 1$ rises then falls, the one shape that cannot be fixed. $[2,1,3]$ is itself a valley, so all $6$ subarrays qualify. And $[1,2,3,4]$ is wholly increasing, giving all $10$.

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
        p = [int(x) for x in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        inc = [1] * n
        dec = [1] * n
        for i in range(1, n):
            if p[i] > p[i - 1]:
                inc[i] = inc[i - 1] + 1
            if p[i] < p[i - 1]:
                dec[i] = dec[i - 1] + 1
        total = 0
        for r in range(n):
            # The turning point is forced to the start of r's increasing run.
            m = r - inc[r] + 1
            total += r - m + dec[m]
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$

## Edge cases

- **Negating turns a value negative, so a weird subarray is a valley.** The negated elements must form a non-decreasing run after negation — meaning a strictly decreasing prefix in the original — followed by a strictly increasing suffix, and every negative sits below every positive automatically.
- **The turning point is forced to the start of $r$'s increasing run.** For the suffix ending at $r$ to be increasing, the turn must be at or after that start; and for turns strictly inside the run, the decreasing part has length $1$.
- **So the count of valid left ends is $(r - m) + \mathrm{dec}[m]$** — one left end per turning point inside the run, plus the whole decreasing run that ends at its start.
- **Single elements always count**, which both run arrays encode by starting at $1$.
- **A fully increasing permutation** (the third row) gives $\binom{N+1}{2}$: every subarray is already sorted and needs no negation.
- **$P$ is a permutation**, so all values are distinct and positive — no ties to worry about in either run, and no zero to straddle the sign boundary.
- **Sum of $N \leq 2 \cdot 10^5$**: three linear passes.

## Dry run

First sample: $P = 2, 3, 1$.

| index | $P$ | increasing run length | decreasing run length |
|---:|---:|---:|---:|
| 1 | 2 | 1 | 1 |
| 2 | 3 | 2 | 1 |
| 3 | 1 | 1 | 2 |

| $r$ | run start $m$ | $(r-m) + \mathrm{dec}[m]$ | running total |
|---:|---:|---:|---:|
| 1 | 1 | $0 + 1 = 1$ | 1 |
| 2 | 1 | $1 + 1 = 2$ | 3 |
| 3 | 3 | $0 + 2 = 2$ | **5** |

Output `5` — every subarray except $[2,3,1]$ itself.

> CodeChef tags: `Algorithms`

---

Same problem in rating order (#441 of 486): [../../by-rating/441-WEIRDSUBARR.md](../../by-rating/441-WEIRDSUBARR.md)
