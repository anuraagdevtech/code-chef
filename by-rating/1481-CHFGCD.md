# 1481 &middot; Chef and GCD

> CodeChef problem code [`CHFGCD`](https://www.codechef.com/problems/CHFGCD) &middot; time limit **0.5s** &middot; Jump from 2* to 3* (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Case analysis on parity |
| **CodeChef category** | main |
| **Time** | $O(\log \min(X,Y))$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/number-theory/CHFGCD.md](../docs/number-theory/CHFGCD.md)

## Question

Chef has two positive integers $X$ and $Y$. Now Chef wants to perform some number of operations (possibly zero) on them. In each operation, Chef can choose either $X$ or $Y$ and increment it by $1$. Find the minimum number of operations Chef needs to perform so that there is a positive integer strictly greater than $1$ which divides both $X$ and $Y$ (In other words, the greatest common divisor of $X$ and $Y$ should be greater than $1$).

**Input**

- The first line contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two integers $X$ and $Y$.

**Output**

For each test case, print a single line containing one integer — the minimum number of operations Chef needs to perform.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq X, Y \leq 10^9$

## Sample

**Sample input**

```
2
4 16
4 55
```

**Sample output**

```
0
1
```

<details><summary>Explanation</summary>

**Test Case 1:** The greatest common divisor of $4$ and $16$ is $4$ which is already greater than $1$, so Chef will not perform any operations.

**Test Case 2:** Chef will perform one operation and add $1$ to $55$. Now the greatest common divisor of $4$ and $56$ is $4$ which is greater than $1$.

</details>

## Approach

The answer is always $0$, $1$ or $2$, and the reason is that **$2$ is a divisor we can always reach**: incrementing each odd value once makes both even, so

$$\text{answer} \leq [X \text{ odd}] + [Y \text{ odd}] \leq 2$$

That bound drives the whole case analysis.

- $\gcd(X,Y) > 1$ already: **$0$**.
- Otherwise the pair is coprime, so they are never both even. If exactly one is odd, adding $1$ to that one makes both even: **$1$**, and $0$ is impossible since they are coprime.
- If both are odd, two moves always suffice. One move can also work, but only if a single increment lands on a common factor — so test $\gcd(X+1, Y) > 1$ and $\gcd(X, Y+1) > 1$. If either holds the answer is **$1$**, else **$2$**.

Only those two one-move candidates need checking, because a single operation can do nothing else.

The both-odd case is where the answer genuinely splits. $X = 3, Y = 5$ needs one move: $Y + 1 = 6$ shares the factor $3$. But $X = Y = 1$ needs two — $\gcd(2,1)$ and $\gcd(1,2)$ are both $1$, and only $(2,2)$ works. More generally two consecutive odd numbers $2m{-}1, 2m{+}1$ often need both increments.

In the sample, $(4,16)$ has $\gcd = 4$, so $0$; $(4,55)$ is coprime with one odd member, so $1$ — and indeed $(4,56)$ shares $4$.

Each test is a couple of GCDs, which keeps $T = 10^5$ comfortable.

## Solution (Python)

```python
import sys
from math import gcd


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        if gcd(x, y) > 1:
            out.append("0")
        elif x % 2 == 0 or y % 2 == 0:
            # Coprime with one even member: bump the odd one and share 2.
            out.append("1")
        elif gcd(x + 1, y) > 1 or gcd(x, y + 1) > 1:
            out.append("1")
        else:
            out.append("2")          # both +1 always shares the factor 2
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(\log \min(X,Y))$ per test case
- **Space:** $O(1)$
