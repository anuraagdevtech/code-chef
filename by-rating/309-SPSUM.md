# 309. Split Sums

> [`SPSUM`](https://www.codechef.com/problems/SPSUM) &middot; difficulty **1524** &middot; time limit **1s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Splitting a fixed total under a gcd condition |
| **CodeChef tags** | `ad-hoc`, `maths` |
| **Complexity class** | Logarithmic $O(\log n)$ |
| **Time** | $O(\log S)$ per test case |
| **Space** | $O(1)$ |

## Question

A and B are brothers and like playing with marbles.Their mother buys them **N** marbles to play with.The preciousness of each marble is a natural number from 1 to **N** and no two marbles have same preciousness.

Since A and B are good at maths they want to divide all those **N** marbles among them in such a way that sum of the preciousness of all marbles that A receives and sum of the preciousness of all marbles that B receives after distribution are co-primes i.e the gcd(greatest common divisor) of their sum is 1.

Also the absolute value of difference between the sum of the preciousness of marbles of A and B should be exactly **M**.

Help A and B in finding whether such a distribution of **N** marbles between them is possible or not.

Formally, you have to tell whether you can distribute first **N** natural numbers in two sets such that the absolute difference of the sum of numbers in the two sets is equal to **M** and the gcd of their sum is 1.

Note that one of the set can be empty and greatest common divisor of **0** and **k** is **k**

**Input**

- The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The first line of each test case contains two integers **N**  and **M** denoting the number of marbles and the absolute difference of sum respectively.

**Output**

- For each test case, output a single line.

Print “Yes” if there exist a valid distribution of marbles between A and B else print “No”.

**Constraints**

- **1** ≤ **T** ≤ **20**

- **1** ≤ **N** ≤ **1,000,000,000**

- **0** ≤ **M** ≤ **10^18**

## Constraints

- 1 ≤ T ≤ 20
- 1 ≤ N ≤ 1,000,000,000
- 0 ≤ M ≤ 10^18

## Sample

**Sample input**

```
2
5 7
1 2
```

**Sample output**

```
Yes
No
```

## Approach

The two sums are completely determined. With $S = \frac{N(N+1)}{2}$ the total of $1 \ldots N$, requiring $a + b = S$ and $|a - b| = M$ gives

$$a = \frac{S + M}{2}, \qquad b = \frac{S - M}{2}$$

So three conditions must hold:

1. $M \leq S$, or $b$ would be negative;
2. $S + M$ must be **even**, or the halves are not integers;
3. $\gcd(a, b) = 1$.

Nothing else is needed — in particular, **any** target $a$ in $[0, S]$ is achievable as a subset sum of $1, 2, \ldots, N$, since the values $1 \ldots N$ hit every total in that range. So feasibility of the split never has to be checked separately, and no search is required.

The gcd condition has a neat reading: any common divisor of $a$ and $b$ divides both their sum $S$ and their difference $M$, so the test is closely tied to $\gcd(S, M)$ — but computing $\gcd(a,b)$ directly is simplest and avoids edge cases around $M = 0$.

The problem's note that $\gcd(0, k) = k$ matters when $M = S$: then $b = 0$ and the gcd is $a = S$, which is coprime to nothing unless $S = 1$. The formula handles it without a special case.

Sample case 1: $N = 5$ gives $S = 15$, and $M = 7$ makes $S + M = 22$ even, so $a = 11$ and $b = 4$ with $\gcd = 1$ — `Yes`. Sample case 2 has $S = 1$ against $M = 2$, failing the first condition.

With $N$ up to $10^9$, $S$ reaches about $5 \times 10^{17}$ and $M$ up to $10^{18}$, so this is **64-bit** arithmetic outside Python.

## Solution

```python
import sys
from math import gcd


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, m = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        s = n * (n + 1) // 2
        # The two sums are forced; any target in [0, s] is a reachable subset sum.
        if m > s or (s + m) % 2:
            out.append("No")
            continue
        a, b = (s + m) // 2, (s - m) // 2
        out.append("Yes" if gcd(a, b) == 1 else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The two sums are forced by $S$ and $M$.** Their total is $S = N(N+1)/2$ and their difference is $M$, so they must be $(S+M)/2$ and $(S-M)/2$ — there is nothing to search.
- **Parity must match**: if $S + M$ is odd no integer split exists, so the answer is `No` before any gcd is computed.
- **$M$ cannot exceed $S$** (the second row, $N = 1$ with $M = 2$), since the larger share is at most everything.
- **Any target in $[0, S]$ is a reachable subset sum** of $1 \dots N$, which is why only the parity and the gcd need checking and no feasibility search over subsets is needed.
- **The gcd condition is the real test**, and it can fail even when the arithmetic works out — for instance $N = 4$ with $M = 0$ gives $5$ and $5$, whose gcd is $5$.
- **$M$ up to $10^{18}$ and $N$ up to $10^9$** put $S$ near $5 \times 10^{17}$, so exact integers are required throughout.

## Dry run

First sample: $N = 5$, so $S = 15$, and $M = 7$.

| step | value |
|---|---|
| $S + M = 22$ | even ✓ |
| A's share $(S+M)/2$ | 11 |
| B's share $(S-M)/2$ | 4 |
| $\gcd(11, 4)$ | 1 ✓ |

Output `Yes` — for instance A takes $\{5, 4, 2\}$ and B takes $\{1, 3\}$.

---

Same problem grouped by topic: [../docs/number-theory/SPSUM.md](../docs/number-theory/SPSUM.md)
