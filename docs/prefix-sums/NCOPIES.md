[&larr; 471. Fair Distribution](FAIR_DISTRIB.md) &middot; [Index](../../README.md)

# 476. Copy and Paste

> CodeChef problem code [`NCOPIES`](https://www.codechef.com/problems/NCOPIES) &middot; difficulty **1745** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Prefix Sums |
| **Technique** | Splitting a repeated string's running total |
| **Time** | $O(N + M)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

Chef has binary string $A$ of length $N$. He constructs a new binary string $B$ by concatenating $M$ copies of $A$ together. For example, if $A = \texttt{"10010"}$, $M = 3$, then $B = \texttt{"100101001010010"}$.

Chef calls an index $i$ $(1 \le i \le N \cdot M)$ *good* if:
- $pref_i = suf_{i + 1}$.

Here, $pref_j = B_1 + B_2 + \ldots + B_j$ and
$suf_j = B_{j} + B_{j + 1} + \ldots + B_{N \cdot M}$ (Note that $suf_{N \cdot M + 1} = 0$ by definition)

Chef wants to find the number of good indices in $B$. Can you help him do so?

**Input**

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains two space-separated integers $N$ and $M$ — the length of the binary string $A$ and the number of times $A$ is concatenated to form $B$.
- The second line of each test case contains a binary string $A$ of length $N$ containing $0$s and $1$s only.

**Output**

For each test case, output the number of good indices in $B$.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N, M \leq 10^5$
- $A$ is a binary string, i.e, contains only the characters $0$ and $1$.
- The sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.
- The sum of $M$ over all test cases does not exceed $2 \cdot 10^5$.

## Sample

**Sample input**

```
3
2 2
00
2 4
11
3 3
101
```

**Sample output**

```
4
1
2
```

<details><summary>Explanation</summary>

**Test case $1$:** $B = \texttt{"0000"}$. In this string, all the indices are good.

**Test case $2$:** $B = \texttt{"11111111"}$. In this string, only $i = 4$ is good.

**Test case $3$:** $B = \texttt{"101101101"}$. In this string, $i = 4$ and $i = 5$ are good.

</details>

## Approach

Let $\Sigma$ be the total number of ones in $B$, so $\Sigma = M \cdot S$ with $S$ the count in one copy of $A$. Since $\mathrm{suf}_{i+1} = \Sigma - \mathrm{pref}_i$, the condition $\mathrm{pref}_i = \mathrm{suf}_{i+1}$ is simply

$$2\,\mathrm{pref}_i = \Sigma$$

So if $M S$ is **odd** the answer is $0$ outright, and otherwise the task is to count the indices where the running total equals $H = MS/2$.

Because $B$ is $M$ copies of $A$, an index inside copy $j$ (0-indexed) at offset $k$ has $\mathrm{pref} = jS + \mathrm{pref}^A_k$. Setting that equal to $H$ gives

$$\mathrm{pref}^A_k = H - jS = S\left(\tfrac{M}{2} - j\right)$$

and since $0 \leq \mathrm{pref}^A_k \leq S$, only $j \in \{\lfloor H/S \rfloor - 1,\ \lfloor H/S \rfloor\}$ can contribute. So tally the prefix values of $A$ once and look up at most two targets — no need to build $B$, whose length can reach $10^{10}$.

The all-zero case is separate and striking: with $S = 0$ every prefix is $0 = H$, so **every** index is good. That is the first sample, $N = M = 2$ on `00`, giving $4$.

For `11` with $M = 4$, $H = 4$ is reached only at the very middle of $B$, so the answer is $1$. And for `101` with $M = 3$, $H = 3$ is hit twice — at the `1` ending copy $2$'s first character and again at the `0` after it — giving $2$.

## Solution (Python)

```python
import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, m = int(data[1 + 3 * i]), int(data[2 + 3 * i])
        a = data[3 + 3 * i]
        ones = a.count(0x31)
        if ones == 0:
            out.append(str(n * m))        # every prefix sum is already 0
            continue
        if (m * ones) % 2:
            out.append("0")               # the total cannot be halved
            continue
        seen = Counter()
        run = 0
        for c in a:
            run += c == 0x31
            seen[run] += 1
        half = m * ones // 2
        # Only the copy around H / S can host a matching prefix.
        base = half // ones
        total = 0
        for j in (base - 1, base):
            if 0 <= j < m:
                total += seen.get(half - j * ones, 0)
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N + M)$ per test case
- **Space:** $O(N)$

## Edge cases

- **$pref_i = suf_{i+1}$ means the running sum hits exactly half the total**, since the two partition every character — so the question is how often the prefix sum of $B$ equals $M \cdot (\text{ones in } A) / 2$.
- **An odd total is impossible** → $0$, which must be checked before any division.
- **An all-zero $A$ makes every index good**, since all the sums are $0$ — giving $N M$, the only case where the answer is quadratic in the input size.
- **Only one or two copies can host a match.** Inside copy $j$ the prefix sum is $j \cdot \text{ones} + pref_A(r)$, and $pref_A(r)$ lies in $[0, \text{ones}]$ — so $j$ must be $\lfloor H/\text{ones} \rfloor$ or one less.
- **The positions are counted by prefix value**, so a tally over one copy of $A$ answers both candidates in constant time.
- **The index $i = 0$ is excluded** ($1 \le i$), which the tally respects by only recording positions $1 \dots N$.
- **$N M$ reaches $10^{10}$** in the all-zero case, past 32-bit.

## Dry run

Third sample: $A = $ `101`, $M = 3$, so $B = $ `101101101` with $6$ ones and a half of $3$.

| prefix value within one copy | positions reaching it |
|---:|---|
| 1 | $r = 1, 2$ |
| 2 | $r = 3$ |

With $\text{ones} = 2$, the base copy is $\lfloor 3/2 \rfloor = 1$:

| copy $j$ | needed $pref_A(r)$ | matches |
|---:|---:|---:|
| 0 | $3 - 0 = 3$ | 0 |
| 1 | $3 - 2 = 1$ | 2 |

Output `2` — the good indices are $4$ and $5$.

> CodeChef tags: `Data Structures`, `Mathematics`, `Algorithms`, `Searching`, `Simple Algos`

---

Same problem in rating order (#448 of 486): [../../by-rating/448-NCOPIES.md](../../by-rating/448-NCOPIES.md)
