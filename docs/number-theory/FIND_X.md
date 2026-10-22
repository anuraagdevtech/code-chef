[&larr; 395. Chef And The Hiring Event](CHEARMY.md) &middot; [Index](../../README.md) &middot; [419. Number Hunt &rarr;](NUMHUNT.md)

# 410. Find eX

> CodeChef problem code [`FIND_X`](https://www.codechef.com/problems/FIND_X) &middot; difficulty **1651** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Shared remainder forces a multiple of the LCM |
| **Time** | $O(\log \min(B,D))$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

Chef has $4$ positive integers $A$, $B$, $C$, and $D$ such that $A$ $\%$ $B=C$ $\%$ $D$.

Find the **smallest positive** integer $X$ such that $(A+X)$ $\%$ $B=(C+X)$ $\%$ $D$ holds.

It is guaranteed that such $X$ always exists.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains four space-separated integers $A$, $B$, $C$, and $D$.

**Output**

For each test case, print a single line containing one integer — $X$, the smallest integer satisfying the conditions.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq A, B, C, D \leq 10^9$
- $A$ $\%$ $B = C$ $\%$ $D$

## Sample

**Sample input**

```
3
4 7 4 8
5 1 8 2
3 2 4 3
```

**Sample output**

```
1
2
5
```

<details><summary>Explanation</summary>

**Test case $1$:** The smallest $X$ satisfying the equation is $1$, as $(4+1)$ $\%$ $7=(4+1)$ $\%$ $8 = 5$.

**Test case $2$:** The smallest $X$ satisfying the equation is $2$, as $(5+2)$ $\%$ $1=(8+2)$ $\%$ $2 = 0$.

</details>

## Approach

Let $r = A \bmod B = C \bmod D$. Since $(A + X) \bmod B = (r + X) \bmod B$ and likewise for $D$, substituting $Y = r + X$ reduces the whole problem to

$$Y \bmod B = Y \bmod D$$

Call that common remainder $m$. Then $m < B$ and $m < D$, so $m < \min(B, D)$, and $Y - m$ is divisible by both $B$ and $D$, hence by $L = \mathrm{lcm}(B, D)$. Since $m < \min(B,D) \leq L$, this says exactly

$$Y \bmod L < \min(B, D)$$

So the valid $Y$ form a short window at the start of each multiple of $L$. Note $r$ itself is valid (it is below both moduli), which is the given $X = 0$ — and we need $X > 0$, i.e. the *next* valid $Y$ above $r$:

- if $r + 1 < \min(B, D)$, then $Y = r+1$ is still inside the window, so $X = 1$;
- otherwise $r$ is the last value in the window, and the next window starts at $Y = L$, giving $X = L - r$.

Those are the only two possibilities, which is why no search is needed. Note $L$ can reach $10^{18}$, so computing it as $B / \gcd(B,D) \cdot D$ matters in C++; Python is unbounded.

The samples hit both branches. $A{=}4, B{=}7, C{=}4, D{=}8$ has $r = 4 < 6 = \min - 1$, so $X = 1$. $A{=}5, B{=}1, C{=}8, D{=}2$ has $\min(B,D) = 1$ and $r = 0$, so the window is only $\{0\}$ and $X = \mathrm{lcm}(1,2) - 0 = 2$. And $A{=}3, B{=}2, C{=}4, D{=}3$ has $r = 1 = \min(B,D) - 1$, giving $X = 6 - 1 = 5$.

## Solution (Python)

```python
import sys
from math import gcd


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, c, d = (int(data[1 + 4 * i]), int(data[2 + 4 * i]),
                      int(data[3 + 4 * i]), int(data[4 + 4 * i]))
        r = a % b
        small = b if b < d else d
        if r + 1 < small:
            out.append("1")              # still inside the current window
        else:
            # The window ends here, so jump to the start of the next one.
            out.append(str(b // gcd(b, d) * d - r))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(\log \min(B,D))$ per test case
- **Space:** $O(1)$

## Edge cases

- **The two remainders start equal and advance in step until one of them wraps.** The first wrap happens at $X = \min(B, D) - r$, so any smaller $X$ keeps them equal — and $X = 1$ works whenever $r + 1 < \min(B, D)$.
- **Once the window ends, they realign only when both wrap together**, which is at the next multiple of $\operatorname{lcm}(B, D)$ — giving $X = \operatorname{lcm}(B,D) - r$.
- **The lcm must be computed as `b // gcd(b, d) * d`**, dividing first; with $B, D$ up to $10^9$ the naive product reaches $10^{18}$, native in Python but an overflow in a 64-bit language.
- **$B = 1$ (or $D = 1$) forces the second branch**, since $r = 0$ and $\min$ is $1$, so $r + 1 < 1$ is false — the second sample row.
- **$X$ must be strictly positive**, which is why the window test is $r + 1 < \min$ rather than $r \leq \min$.
- **$A \% B = C \% D$ is guaranteed**, so the remainders really do start equal and the reasoning applies from step zero.
- **A solution always exists**, as the statement promises — the lcm point is always reachable.

## Dry run

Third sample: $A = 3$, $B = 2$, $C = 4$, $D = 3$, so $r = 1$ and $\min(B,D) = 2$.

Since $r + 1 = 2$ is not less than $2$, the window has already ended. $\operatorname{lcm}(2,3) = 6$, so $X = 6 - 1 = 5$.

| $X$ | $(3+X) \bmod 2$ | $(4+X) \bmod 3$ | equal? |
|---:|---:|---:|:---:|
| 1 | 0 | 2 | no |
| 2 | 1 | 0 | no |
| 3 | 0 | 1 | no |
| 4 | 1 | 2 | no |
| 5 | 0 | 0 | **yes** |

> CodeChef tags: `Number Theory`

---

Same problem in rating order (#383 of 486): [../../by-rating/383-FIND_X.md](../../by-rating/383-FIND_X.md)
