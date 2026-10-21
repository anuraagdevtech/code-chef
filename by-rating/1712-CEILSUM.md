# 1712 &middot; Ceiling Sum

> CodeChef problem code [`CEILSUM`](https://www.codechef.com/problems/CEILSUM) &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Parity bonus on a fixed total |
| **CodeChef tags** | `Algorithms`, `Constructive`, `ad-hoc` |
| **CodeChef top tag** | `Ad Hoc` |
| **CodeChef category** | easy |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/basic-math/CEILSUM.md](../docs/basic-math/CEILSUM.md)

## Question

You are given two integers $A, B$. You have to choose an integer $X$ in the range [minimum($A, B$), maximum($A, B$)] such that:

$$\Big \lceil \frac{B - X}{2} \Big \rceil + \Big \lceil \frac{X - A}{2} \Big \rceil$$ is maximum.

What is the maximum sum you can obtain if you choose $X$ optimally?

**Note:** $\lceil x \rceil$ : Returns the smallest integer that is greater than or equal to $x$ (i.e  rounds up to the nearest integer). For example, $\lceil 1.4 \rceil = 2$, $\lceil 5 \rceil = 5$, $\lceil -1.5 \rceil = -1$, $\lceil -3 \rceil = -3$ , $\lceil 0 \rceil = 0$.

**Input**

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, two integers $A, B$.

**Output**

For each testcase, output the maximum sum of $\lceil \frac{B - X}{2} \rceil + \lceil \frac{X - A}{2} \rceil$.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq A, B \leq 10^9$

## Sample

**Sample input**

```
3
2 2
1 11
13 6
```

**Sample output**

```
0
6
-3
```

<details><summary>Explanation</summary>

- In the first test case, there is only one possible value of $X$ which is equal to $2$. So the sum is equal to $\lceil \frac{2 - 2}{2} \rceil + \lceil \frac{2 - 2}{2} \rceil$ = $\lceil \ 0 \rceil + \lceil \ 0 \rceil$  = $0 + 0 = 0$.

- In the second test case, we can choose $X$ to be $2$. So sum is equal to $\lceil \frac{11 - 2}{2} \rceil + \lceil \frac{2 - 1}{2} \rceil$ = $\lceil \ 4.5 \rceil + \lceil \ 0.5 \rceil$ = $5 + 1 = 6$. There is no possible way to choose an integer $X$ in the range $[1, 11]$ such that sum is greater than $6$.

</details>

## Approach

Write $p = B - X$ and $q = X - A$, so $p + q = B - A$ is **fixed** whatever $X$ is. Using $\lceil z/2 \rceil = \frac{z + (z \bmod 2)}{2}$,

$$\left\lceil \frac{p}{2} \right\rceil + \left\lceil \frac{q}{2} \right\rceil = \frac{(B-A) + [\,p \text{ odd}\,] + [\,q \text{ odd}\,]}{2}$$

So the sum is a constant plus a bonus of $0$, $1$ or $2$ from the roundings, and the only question is how many of $p, q$ can be made odd.

- $B - A$ **odd**: $p$ and $q$ have opposite parities, so exactly one is odd no matter what. The bonus is always $1$ and the answer is $\frac{B-A+1}{2}$.
- $B - A$ **even and non-zero**: $p$ and $q$ share a parity, so they are both odd or both even. The range $[\min(A,B), \max(A,B)]$ contains at least two integers, so an $X$ of either parity is available — pick one making $B-X$ odd and collect the full bonus of $2$, giving $\frac{B-A}{2} + 1$.
- $A = B$: the only legal $X$ is $A$, so $p = q = 0$ and the answer is $0$.

Note the result can be negative, since $B < A$ is allowed and then $B - A < 0$; the formula handles it, as does the ceiling of a negative number ($\lceil -1.5 \rceil = -1$).

The samples cover all three. $A = B = 2$ gives $0$. $A{=}1, B{=}11$ has an even gap of $10$, so $5 + 1 = 6$ — for instance $X = 2$ makes both $9$ and $1$ odd. And $A{=}13, B{=}6$ has the odd gap $-7$, giving $-3$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        gap = b - a
        if gap == 0:
            out.append("0")               # X is forced, so both halves vanish
        elif gap % 2:
            out.append(str((gap + 1) // 2))   # one half is always odd
        else:
            out.append(str(gap // 2 + 1))     # both halves can be made odd
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
