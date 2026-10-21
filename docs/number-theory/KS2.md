# 280. Guddu on a Date

> CodeChef problem code [`KS2`](https://www.codechef.com/problems/KS2) &middot; difficulty **1525** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | A bijection between prefixes and solutions |
| **Time** | $O(\log N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

Guddu likes a girl that loves playing with numbers. She agreed to go on a date with Guddu, but only if he can solve the following problem:

An integer is *round* if it is greater than $0$ and the sum of its digits in decimal representation is a multiple of $10$. Find the $N$-th smallest round integer.

However, Guddu does not like playing with numbers at all and he is unable to solve this problem, so he begs you to solve it for him. In return, he will definitely give you a treat.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer $N$.

**Output**
For each test case, print a single line containing the $N$-th round integer. It is guaranteed that this number is smaller than $2^{64}$.

**Constraints**
- $1 \le T \le 10^5$
- $1 \le N \le 10^{18}$

**Subtasks**
**Subtask #1 (30 points):**
- $1 \le T \le 10$
- $1 \le N \le 10^5$

**Subtask #2 (70 points):** original constraints

## Constraints

- $1 \le T \le 10^5$
- $1 \le N \le 10^{18}$

## Sample

**Sample input**

```
1
2
```

**Sample output**

```
28
```

<details><summary>Explanation</summary>

**Example case 1:** The smallest round integer is $19$ and the second smallest is $28$.

</details>

## Approach

Call an integer *round* when its digit sum is a multiple of $10$. The key structural fact:

> For every positive integer $p$, there is **exactly one** digit $d$ making the number $\overline{p\,d}$ round.

Because appending $d$ adds $d$ to the digit sum, and exactly one value of $d \in \{0, \ldots, 9\}$ brings that sum to $0$ modulo $10$ — namely $d = (-S(p)) \bmod 10$.

That gives a bijection between prefixes $p = 1, 2, 3, \ldots$ and round numbers, **order-preserving** because appending a digit is monotonic in the prefix. So the $N$-th round number is simply $N$ with its completing digit attached:

$$\text{answer} = 10N + \bigl((10 - S(N) \bmod 10) \bmod 10\bigr)$$

Checking the sample: $N = 2$ has digit sum $2$, so $d = 8$ and the answer is $28$. For $N = 1$ the digit sum is $1$, giving $19$ — and indeed no smaller positive integer has a digit sum of $10$.

The bijection is what makes this $O(\log N)$ rather than a search. With $N$ up to $10^{18}$, enumerating round numbers is impossible, and even a digit DP with binary search would be far more work than this.

The outer $\bmod 10$ matters for the case $S(N) \equiv 0$, where the completing digit is $0$ rather than $10$ — for example $N = 19$ gives $190$.

The result reaches about $10^{19}$, which **exceeds signed 64-bit range** and needs unsigned or big integers elsewhere; the problem's guarantee that it fits in $2^{64}$ is the hint.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        s = data[1 + i]
        # Exactly one last digit completes any prefix to a round number, so
        # the n-th round number is n with that digit appended.
        digit_sum = sum(ch - 48 for ch in s)
        out.append(s.decode() + str((10 - digit_sum % 10) % 10))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(\log N)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Algorithms`
