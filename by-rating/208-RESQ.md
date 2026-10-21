# 208. Arranging Cup-cakes

> [`RESQ`](https://www.codechef.com/problems/RESQ) &middot; difficulty **1322** &middot; time limit **2s** &middot; Jump from 2* to 3* (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Divisor nearest the square root |
| **Complexity class** | Square root $O(\sqrt{n})$ |
| **Time** | $O(\sqrt{N})$ per test case |
| **Space** | $O(1)$ |

## Question

Our Chef is catering for a big corporate office party and is busy preparing different mouth watering dishes. The host has insisted that he serves his delicious cupcakes for dessert.

 On the day of the party, the Chef was over-seeing all the food arrangements as well, ensuring that every item was in its designated position. The host was satisfied with everything except the cupcakes. He noticed they were arranged neatly in the shape of a rectangle. He asks the Chef to make it as square-like as possible.

 The Chef is in no mood to waste his cupcakes by transforming it into a perfect square arrangement. Instead, to fool the host, he asks you to arrange the **N** cupcakes as a rectangle so that the **difference** between the length and the width is minimized.

**Input**

The first line of the input file contains an integer **T**, the number of test cases. Each of the following **T** lines contains a single integer **N** denoting the number of cupcakes.

**Output**

Output **T** lines, each indicating the minimum possible difference between the length and the width in a rectangular arrangement of the cupcakes.

**Constraints**

1 ≤ **T** ≤ 100

1 ≤ **N** ≤ 10^8

## Constraints

1 ≤ T ≤ 100
1 ≤ N ≤ 10^8

## Sample

**Sample input**

```
4
20
13
8
4
```

**Sample output**

```
1
12
2
0
```

<details><summary>Explanation</summary>

**Test case $1$:** $20$ cupcakes can be arranged in a rectange in $6$ possible ways -  $1 \times 20, 2 \times 10, 4 \times 5, 5 \times 4, 10 \times 2$ and $20 \times 1$.
The corresponding differences between the length and the width for each of these rectangles are $ |1-20| = 19, |2-10| = 8, |4-5| = 1, |5-4| = 1, |10-2| = 8$ and $|20-1| = 19$ respectively. Hence, $1$ is the smallest difference between length and width among all possible combinations.

**Test case $2$:** $13$ cupcakes can be arranged in $2$ ways only. These are $13 \times 1$ and $1 \times 13$. In both cases, the difference between width and length is $12$.

**Test case $3$:** $8$ cupcakes can be arranged in $4$ ways. These are: $8\times 1, 4\times 2, 2\times 4$ and $1\times 8$. The minimum difference between length and width is $2$ which is in the cases $4\times 2 $ and $2\times 4$.

**Test case $4$:** $4$ cupcakes can be arranged as $2\times 2$. The difference between the length and the width, in this case, is $0$.

</details>

## Approach

A rectangular arrangement of $N$ cupcakes is a factorisation $N = \ell \times w$, and the difference $|\ell - w|$ shrinks as the factors move toward each other. Writing $\ell = N/d$ and $w = d$ with $d \leq \sqrt{N}$, the gap

$$\frac{N}{d} - d$$

is **strictly decreasing in $d$** on $(0, \sqrt{N}]$, since both terms move the right way. So the best arrangement comes from the **largest divisor of $N$ that is at most $\sqrt{N}$** — no comparison of candidates is needed, just the last one found.

Scanning $d$ from $1$ to $\lfloor \sqrt{N} \rfloor$ and keeping the largest divisor costs $O(\sqrt{N}) = 10^4$ steps, which with $T \leq 100$ is trivial. The divisor $1$ always qualifies, so the scan never comes up empty.

The samples cover the extremes. $N = 4$ is a perfect square, so $d = 2$ gives $0$ — the only way to hit zero. $N = 13$ is prime, so the only option is $1 \times 13$, giving $12$; primes are always the worst case. $N = 20$ gives $d = 4$ and $5 - 4 = 1$, and $N = 8$ gives $d = 2$ and $4 - 2 = 2$ — note $8$'s divisors skip over $\sqrt 8 \approx 2.83$, which is why the answer is not smaller.

Use integer arithmetic for the loop bound: `isqrt(n)` rather than `int(n ** 0.5)`, which can be off by one near a perfect square and would silently miss the $0$ answer.

## Solution

```python
import sys
from math import isqrt


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for tok in data[1:1 + t]:
        n = int(tok)
        # N/d - d falls as d rises, so the largest divisor below sqrt(N) wins.
        best = 1
        for d in range(1, isqrt(n) + 1):
            if n % d == 0:
                best = d
        out.append(str(n // best - best))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **A perfect square** ($N = 4$) gives $0$, and that is the only way to reach $0$ — rows and columns are equal.
- **A prime** ($N = 13$) forces the $1 \times N$ arrangement and the worst possible answer, $N - 1$.
- **$N = 1$**: $\mathrm{isqrt}(1) = 1$, the divisor $1$ is found, and the answer is $1 - 1 = 0$.
- **$N/d - d$ decreases as $d$ rises** over $(0, \sqrt{N}]$, so the *largest* divisor not exceeding $\sqrt{N}$ is optimal; searching from the other side gives the same pair, since each divisor below the root has exactly one partner above it.
- **`isqrt` must be exact.** `int(math.sqrt(n))` can come out one too small on a large perfect square, and at $N = 10^8$ that would miss the divisor $10^4$ and report $10^4 - 1$ instead of $0$.
- **$N$ up to $10^8$** means $10^4$ trial divisions per case and $10^6$ across the file — fine, but a full factorisation would not be.

## Dry run

| $N$ | $\mathrm{isqrt}(N)$ | divisors $\leq$ root | best $d$ | $N/d$ | output |
|---:|---:|---|---:|---:|---:|
| 20 | 4 | $1, 2, 4$ | 4 | 5 | `1` |
| 13 | 3 | $1$ | 1 | 13 | `12` |
| 8 | 2 | $1, 2$ | 2 | 4 | `2` |
| 4 | 2 | $1, 2$ | 2 | 2 | `0` |

---

Same problem grouped by topic: [../docs/number-theory/RESQ.md](../docs/number-theory/RESQ.md)
