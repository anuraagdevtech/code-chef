[&larr; 169. Turn It](NFS.md) &middot; [Index](../../README.md) &middot; [172. Tom And Jerry 1 &rarr;](TANDJ1.md)

# 171. Distinct Pair Sums

> CodeChef problem code [`MANYSUMS`](https://www.codechef.com/problems/MANYSUMS) &middot; difficulty **1480** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Range of achievable sums |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | Level up from 1* to 2* (Level 2) |

## Question

You are given a range of integers $\{L, L+1, \ldots, R\}$. An integer $X$ is said to be *reachable* if it can be represented as a sum of two **not necessarily distinct** integers in this range. Find the number of distinct reachable integers.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $L$ and $R$.

**Output**
For each test case, print a single line containing one integer — the number of reachable integers.

**Constraints**
- $1 \leq T \leq 10^5$
- $1 \leq L \leq R \leq 10^6$

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq L \leq R \leq 10^6$

## Sample

**Sample input**

```
2
2 2
2 3
```

**Sample output**

```
1
3
```

<details><summary>Explanation</summary>

**Example case 1:** The only reachable integer is $2 + 2 = 4$.

**Example case 2:** $4$, $5$ and $6$ are reachable, since $2+2=4$, $2+3=5$ and $3+3=6$.

</details>

## Approach

Adding two values from $\{L, \ldots, R\}$, with repetition allowed, gives a smallest sum of $L + L = 2L$ and a largest of $R + R = 2R$.

The important claim is that **every** integer in between is reachable. Starting from $(L, L)$, raising one of the two chosen values by one increases the sum by exactly one, and either value may be raised until it hits $R$. So the sums sweep the whole interval with no gaps, and the count is

$$2R - 2L + 1$$

Confirming that there are no gaps is the step that matters. The instinct that pair sums might skip values is reasonable in general — it is true for a set like $\{1, 10\}$ — but a **contiguous** range of integers produces a contiguous range of sums, precisely because unit steps are available.

The "not necessarily distinct" clause is what makes $2L$ and $2R$ themselves reachable. Requiring distinct values would shrink the range to $[2L+1, 2R-1]$ and make $L = R$ a degenerate case with no valid pair at all.

Sample case 1 has $L = R = 2$: the only sum is $4$, and the formula gives $4 - 4 + 1 = 1$. Sample case 2 spans $4$ to $6$ for $3$ reachable values.

The usual fencepost applies — the $+1$ is needed because both endpoints are included.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        l, r = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Sums sweep [2L, 2R] with no gaps, since unit steps are available.
        out.append(str(2 * r - 2 * l + 1))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **The two integers need not be distinct**, which the statement says explicitly — that is what makes $2L$ and $2R$ themselves reachable, and why $L = R$ gives one sum rather than none.
- **There are no gaps in $[2L, 2R]$**, because either addend can be nudged by one: starting from $L + L$ and incrementing one side at a time sweeps every integer up to $R + R$.
- **$L = R$** (the first row) → exactly one reachable value, $2L$.
- **The count is of distinct sums, not of pairs** — the second row has nine ordered pairs but only three distinct sums.
- **$L, R$ up to $10^6$** keeps the answer under $2 \times 10^6$, so no large arithmetic is involved.
- **$T$ up to $10^5$** with constant work per case.

## Dry run

| $L$ | $R$ | reachable sums | count |
|---:|---:|---|---:|
| 2 | 2 | $4$ | `1` |
| 2 | 3 | $4$ ($2{+}2$), $5$ ($2{+}3$), $6$ ($3{+}3$) | `3` |

---

Same problem in rating order (#278 of 486): [../../by-rating/278-MANYSUMS.md](../../by-rating/278-MANYSUMS.md)
