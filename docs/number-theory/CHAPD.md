# 457. Chef and Prime Divisors

> CodeChef problem code [`CHAPD`](https://www.codechef.com/problems/CHAPD) &middot; difficulty **1720** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Stripping shared factors with repeated GCDs |
| **Time** | $O(\log^2 \max(A,B))$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

You are given two positive integers – **A** and **B**. You have to check whether **A** is divisible by all the prime divisors of **B**.

**Input**

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

For each test case, you are given two space separated integers – **A** and **B**.

**Output**

For each test case, output "Yes" (without quotes) if **A** contains all prime divisors of **B**, otherwise print "No".

**Constraints**

- **1** ≤ **T** ≤ **10^4**

- **1** ≤ **A, B** ≤ **10^18**

**Subtasks**

- **Subtask 1 (20 points):****1** ≤ **B** ≤ **10^7**

- **Subtask 2 (30 points):****1** ≤ **A** ≤ **10^7**

- **Subtask 3 (50 points):** Original constraints

## Constraints

- 1 ≤ T ≤ 10^4
- 1 ≤ A, B ≤ 10^18

## Sample

**Sample input**

```
3
120 75
128 16
7 8
```

**Sample output**

```
Yes
Yes
No
```

<details><summary>Explanation</summary>

**Example case 1.** In the first case 120 = 2^3*3*5 and 75 = 3*5^2. 120 is divisible by both 3 and 5. Hence, we will print "Yes"

**Example case 2.** In the second case both 128 and 16 are powers of two. Hence, the answer is "Yes"

**Example case 3.** In the third case 8 is power of two and 7 is not divisible by 2. So, the answer is "No"

</details>

## Approach

At $10^{18}$ there is no factorising $B$ outright, so work with GCDs instead. The idea: repeatedly divide out of $B$ everything it shares with $A$, and see whether anything survives.

$$g \leftarrow \gcd(A, B), \qquad \text{then divide } B \text{ by } g \text{ while it divides}$$

Each round removes from $B$ all the prime powers whose primes also divide $A$, at least partly; repeating until $B$ stops shrinking removes them completely, because every prime of $g$ divides $A$ and is stripped from $B$ to its full multiplicity.

Two terminating conditions:

- $B$ reaches $1$ — every prime of the original $B$ divided $A$, so print `Yes`.
- $g$ becomes $1$ while $B > 1$ — the remaining $B$ is coprime to $A$, so its primes are **not** in $A$, and the answer is `No`.

Note that multiplicity does not matter: the question is about *which* primes divide $B$, not how often. That is why $A = 128 = 2^7$ passes for $B = 16 = 2^4$ and would equally pass for $B = 2^{60}$.

The loop runs $O(\log B)$ times, since each outer round at least halves $B$ when it shrinks at all.

The samples cover the three behaviours. $A = 120, B = 75$: $\gcd = 15$ strips the $3$ and one $5$, leaving $B = 5$; a second round strips that too, so `Yes`. $A = 128, B = 16$: one round clears $B$ entirely. And $A = 7, B = 8$: the first GCD is already $1$ with $B > 1$, so `No`.

## Solution (Python)

```python
import sys
from math import gcd


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        while b > 1:
            g = gcd(a, b)
            if g == 1:
                break                 # what is left shares no prime with A
            while b % g == 0:         # strip those primes to full multiplicity
                b //= g
        out.append("Yes" if b == 1 else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(\log^2 \max(A,B))$ per test case
- **Space:** $O(1)$
