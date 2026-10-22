[&larr; 275. Chef Drinks Coke](COKE.md) &middot; [Index](../../README.md) &middot; [389. Odd Sum &rarr;](ODDSUM.md)

# 371. Guessing Game

> CodeChef problem code [`GUESS`](https://www.codechef.com/problems/GUESS) &middot; difficulty **1410** &middot; time limit **3.5s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Counting by parity, reduced to lowest terms |
| **Time** | $O(\log \min(N,M))$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

## Question

Alice and Bob, both have to drink water. But they both don't want to go, so they will play a game to decide who will fetch water for both of them. Alice will choose a number randomly between **1** and **N** (both inclusive) and Bob will choose a number randomly between **1** and **M** (both inclusive). Both will write their numbers on a slip of paper. If sum of numbers choosen by both is **odd**, then Alice will go, else Bob will go.

What is probability that Alice will go?

**Input**

First line contains, **T**, the number of testcases. Each testcase consists of **N** and **M** in one line, separated by a space.

**Output**

For each test case, output a single line containing probability as an [irreducible fraction](http://en.wikipedia.org/wiki/Irreducible_fraction).

**Constraints**

- **1** ≤ **T** ≤ **10^5**

- **1** ≤ **N,M** ≤ **10^9**

## Constraints

- 1 ≤ T ≤ 10^5
- 1 ≤ N,M ≤ 10^9

## Sample

**Sample input**

```
3
1 1
1 2
2 3
```

**Sample output**

```
0/1
1/2
1/2
```

<details><summary>Explanation</summary>

**test1: The only way is when Alice and Bob both choose 1. So, Alice won't have to go because sum is even.**
**test2: The different ways are (1,1) and (1,2), where first term denotes the number choosen by Alice. So of all possible cases (ie. 2) in only 1 case Alice has to go. Therefore, probability is 1/2.**
**test3: The different ways are (1,1), (1,2), (1,3), (2,1), (2,2), (2,3) where first term denotes the number choosen by Alice. So of all possible cases (ie. 6) in only 3 cases Alice has to go. Therefore, probability is 1/2.**

</details>

## Approach

Both choices are uniform and independent, so the probability is a ratio of counts over the $N \cdot M$ equally likely pairs. A sum is odd exactly when the two parts have **different parity**, so with

$$N_{\text{odd}} = \left\lceil \frac{N}{2} \right\rceil = \left\lfloor \frac{N+1}{2} \right\rfloor, \qquad N_{\text{even}} = \left\lfloor \frac{N}{2} \right\rfloor$$

and likewise for $M$, the favourable count is

$$N_{\text{odd}} M_{\text{even}} + N_{\text{even}} M_{\text{odd}}$$

Since $N, M \leq 10^9$ the numerator reaches about $5 \times 10^{17}$ — inside 64-bit range but only just, so C++ needs `long long` here.

The output must be an **irreducible fraction**, so divide both parts by their GCD. The degenerate case is a numerator of $0$: $\gcd(0, d) = d$, so the reduction yields $0/1$ automatically rather than $0/d$ — exactly the expected `0/1` when $N = M = 1$, where the only sum is $2$.

A useful sanity check: whenever either $N$ or $M$ is even the answer is exactly $1/2$, because that side contributes equal numbers of odd and even values and so balances the parities whatever the other side does. Both sample answers of $1/2$ are instances — $N=1, M=2$ and $N=2, M=3$. The probability can differ from $1/2$ only when $N$ and $M$ are both odd, which is when each side has one more odd value than even.

## Solution (Python)

```python
import sys
from math import gcd


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, m = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # An odd sum needs one odd and one even pick.
        top = (n + 1) // 2 * (m // 2) + n // 2 * ((m + 1) // 2)
        bottom = n * m
        g = gcd(top, bottom)          # gcd(0, d) == d, so 0 reduces to 0/1
        out.append(f"{top // g}/{bottom // g}")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(\log \min(N,M))$ per test case
- **Space:** $O(1)$

## Edge cases

- **A zero numerator must print `0/1`, not `0/<denominator>`.** Python's `gcd(0, d)` returns `d`, so dividing both parts by the gcd reduces $0/1$ correctly without a special case — and the first row is exactly this, since $1 + 1$ is always even.
- **Counting odds as $\lceil n/2 \rceil$ and evens as $\lfloor n/2 \rfloor$** is what makes $n = 1$ work: one odd, zero evens.
- **An odd sum needs exactly one odd and one even pick**, so the two cross terms are the entire numerator and no other combination contributes.
- **The fraction must be in lowest terms** — the third row reduces $3/6$ to $1/2$.
- **$n$ and $m$ up to $10^9$** put the denominator at $10^{18}$, native in Python but past 32-bit.
- **The two ranges are independent**, so the counts multiply rather than needing any joint enumeration.

## Dry run

Third sample: $n = 2$, $m = 3$.

| | odds | evens |
|---|---:|---:|
| $1 \dots 2$ | 1 | 1 |
| $1 \dots 3$ | 2 | 1 |

Favourable pairs: $1 \times 1$ (odd, even) $+\ 1 \times 2$ (even, odd) $= 3$, out of $2 \times 3 = 6$. Reducing by $\gcd(3,6) = 3$ gives `1/2`.

---

Same problem in rating order (#231 of 486): [../../by-rating/231-GUESS.md](../../by-rating/231-GUESS.md)
