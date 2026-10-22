[&larr; 393. Different String](DIFSTR.md) &middot; [Index](../../README.md) &middot; [400. Construct Array &rarr;](CONSTRRAY.md)

# 397. GCD of Prefixes

> CodeChef problem code [`GCDPRF`](https://www.codechef.com/problems/GCDPRF) &middot; difficulty **1617** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Divisibility chain, realised by the array itself |
| **Time** | $O(N \log A)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

Sasuke and Itachi are playing a game. Sasuke first creates an array $A$ containing $N$ positive integers $A_1, A_2, \dots, A_N$. He then creates a new array $B$ of length $N$ such that $B_i = \gcd(A_1, A_2, ..., A_i)$ for each $1 \leq i \leq N$. Now, Sasuke gives array $B$ to Itachi and asks him to find any array $A$ (with $1\leq A_i\leq 10^9$) such that the given process applied to $A$ will produce $B$. Can you help Itachi solve this problem?

Here, $\gcd$ stands for [greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor).

**Input**

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $B_1, B_2, \dots, B_N$

**Output**

For each test case, print a single line containing $N$ space-separated integers denoting the array $A$ you constructed. If no such array $A$ exists, print $-1$ instead.

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq N \leq 10^5$
- $1 \leq A_i, B_i \leq 10^9$
- It is guaranteed that sum of $N$ over all test cases doesn't exceed $5 \times 10^5$.

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
2
2
4 2
2
1 3
```

**Sample output**

```
4 26
-1
```

<details><summary>Explanation</summary>

**Test Case 1:** One possible answer is $[4, 26]$ because $B$ can be generated as follows: $B = [\gcd(4), \gcd(4, 26)] = [4, 2]$.

**Test Case 2:** It can be shown that no array $A$ exists which can produce the given $B$.

</details>

## Approach

Prefix GCDs only ever shrink, and they shrink by division: $B_{i} = \gcd(B_{i-1}, A_i)$, so

$$B_i \mid B_{i-1}$$

is necessary. If that chain ever breaks — as in the sample's $B = [1, 3]$, where $3 \nmid 1$ — no array exists and the answer is $-1$.

When the chain holds, the construction is as short as it gets: take $A = B$. The divisibility chain means $B_i$ divides every earlier $B_j$, so

$$\gcd(B_1, B_2, \ldots, B_i) = B_i$$

and the prefix GCDs of $A$ reproduce $B$ exactly. The range condition is free as well, since $B_i \leq 10^9$ is given.

It is worth seeing why nothing cleverer is needed. One might try to make $A_i$ a multiple of $B_i$ that avoids extra common factors — the sample's `4 26` does this, with $26 = 2 \cdot 13$ — but the earlier prefix already caps the GCD at $B_{i-1}$, so any extra factors in $A_i$ beyond $B_i$ are harmless *and* unnecessary. Echoing $B$ is both valid and simplest.

Note the chain condition is only about consecutive terms: $B_i \mid B_{i-1}$ for every $i$ implies $B_i \mid B_j$ for all $j < i$ by transitivity, so one pass suffices.

Our output for the first sample is `4 2` where the sample prints `4 26`; both have prefix GCDs $4, 2$, and the problem accepts any valid array.

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
        b = [int(x) for x in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        # Each prefix GCD must divide the previous one; then B realises itself.
        if all(b[i - 1] % b[i] == 0 for i in range(1, n)):
            out.append(" ".join(map(str, b)))
        else:
            out.append("-1")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N \log A)$ per test case
- **Space:** $O(N)$

## Edge cases

- **Prefix GCDs form a divisibility chain.** $B_i = \gcd(B_{i-1}, A_i)$, so $B_i$ always divides $B_{i-1}$ — making that the one necessary condition, and the second row fails it ($1$ is not divisible by $3$).
- **The condition is also sufficient, and $B$ realises itself.** Taking $A = B$ gives $\gcd(B_1, \dots, B_i) = B_i$, because every earlier $B_j$ is a multiple of $B_i$ — so no construction is needed beyond echoing the input.
- **$B_i \leq 10^9$ is given**, so echoing $B$ automatically respects the bound on $A_i$.
- **The chain must be checked in the right direction**: $B_{i-1} \bmod B_i$, not the reverse. The reverse test would accept the second row.
- **$N = 1$** has no constraint at all, and $A = B$ works trivially.
- **A constant $B$** is a valid chain (every value divides itself), as is any strictly decreasing chain of divisors.
- **This answer differs from the sample's** (`4 2` against `4 26`), and both produce the same $B$; the statement asks for any such $A$, so a special judge recomputes the prefix GCDs.

## Dry run

First sample: $B = 4, 2$.

| check | value |
|---|---|
| $4 \bmod 2$ | $0$ ✓ |

So output $A = 4, 2$ and verify:

| $i$ | $\gcd(A_1 \dots A_i)$ | required $B_i$ |
|---:|---:|---:|
| 1 | $\gcd(4) = 4$ | 4 ✓ |
| 2 | $\gcd(4, 2) = 2$ | 2 ✓ |

> CodeChef tags: `Mathematics`

---

Same problem in rating order (#358 of 486): [../../by-rating/358-GCDPRF.md](../../by-rating/358-GCDPRF.md)
