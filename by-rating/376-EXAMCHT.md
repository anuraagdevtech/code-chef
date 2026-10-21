# 376. Exam Cheating

> [`EXAMCHT`](https://www.codechef.com/problems/EXAMCHT) &middot; difficulty **1639** &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Counting divisors of a difference |
| **CodeChef tags** | `Mathematics`, `Number Theory`, `Integer Factorisation`, `Modular Arithmetic`, `Divisors` |
| **Complexity class** | Square root $O(\sqrt{n})$ |
| **Time** | $O(\sqrt{|A-B|})$ per test case |
| **Space** | $O(1)$ |

## Question

Ram and Shyam are sitting next to each other, hoping to cheat on an exam. However, the examination board has prepared $p$ different sets of questions (numbered $0$ through $p-1$), which will be distributed to the students in the following way:
- The students are assigned roll numbers — pairwise distinct positive integers.
- If a student's roll number is $r$, this student gets the $((r-1)\%p)$-th set of questions.

Obviously, Ram and Shyam can cheat only if they get the same set of questions.

You are given the roll numbers of Ram and Shyam: $A$ and $B$ respectively. Find the number of values of $p$ for which they can cheat, or determine that there is an infinite number of such values.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $A$ and $B$.

**Output**
For each test case, print a single line — the number of values of $p$ for which Ram and Shyam can cheat, or $-1$ if there is an infinite number of such values.

**Constraints**
- $1 \le T \le 100$
- $1 \le A, B \le 10^8$

## Constraints

- $1 \le T \le 100$
- $1 \le A, B \le 10^8$

## Sample

**Sample input**

```
1
2 6
```

**Sample output**

```
3
```

<details><summary>Explanation</summary>

**Example case 1:** They can cheat for $p = 1$, $p = 2$ or $p = 4$.

</details>

## Approach

Ram and Shyam share a set exactly when $(A-1) \bmod p = (B-1) \bmod p$, which is

$$p \mid (A - B)$$

So the question is purely how many positive $p$ divide $A-B$.

If $A = B$ the difference is $0$ and every $p$ works, so there are infinitely many — print $-1$. That case cannot arise from distinct roll numbers, but the input permits it.

Otherwise the answer is the **number of divisors** of $|A-B|$, counted by trial division up to $\sqrt{|A-B|}$: each divisor $d \leq \sqrt{D}$ pairs with $D/d$, and the pair is counted once when $d^2 = D$. With $|A-B| < 10^8$ that is at most $10^4$ steps, so $T \leq 100$ is trivial.

The sign does not matter, since $p \mid (A-B)$ and $p \mid (B-A)$ are the same condition — take the absolute value before factoring.

The sample has $A = 2$ and $B = 6$, so $|A-B| = 4$ with divisors $1, 2, 4$, giving $3$. Checking $p = 4$: roll $2$ gets set $1 \bmod 4 = 1$ and roll $6$ gets set $5 \bmod 4 = 1$ — the same. But $p = 3$ fails: sets $1$ and $2$.

Note every difference has $p = 1$ among its divisors, so with $A \neq B$ the answer is at least $1$ — a single question set is always shared.

## Solution

```python
import sys
from math import isqrt


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        gap = abs(a - b)
        if gap == 0:
            out.append("-1")          # every p works
            continue
        # p works iff p divides the difference, so count its divisors.
        count = 0
        for d in range(1, isqrt(gap) + 1):
            if gap % d == 0:
                count += 1 if d * d == gap else 2
        out.append(str(count))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/number-theory/EXAMCHT.md](../docs/number-theory/EXAMCHT.md)
