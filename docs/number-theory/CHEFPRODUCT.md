[&larr; 419. Number Hunt](NUMHUNT.md) &middot; [Index](../../README.md) &middot; [434. The Optimal Pairs &rarr;](OPTPAIRS.md)

# 424. Chef Product

> CodeChef problem code [`CHEFPRODUCT`](https://www.codechef.com/problems/CHEFPRODUCT) &middot; difficulty **1658** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Size feasibility from a square bound and a parity |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

Chef has a special interest in studying sets of integers.

Given an integer $N$, he defines a *good-set* as a set of **distinct non-negative** integers, such that:
- The sum of the integers in the set is equal to $N$.
- The product of each non-empty subset of the set is **odd**.

Determine the number of **distinct sizes** of *good-set* that can be formed.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of one integer $N$.

**Output**

For each test case, output on a new line, the number of **distinct sizes** of *good-set* that can be formed.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^{18}$

## Sample

**Sample input**

```
2
4
18
```

**Sample output**

```
1
2
```

<details><summary>Explanation</summary>

**Test case $1$**: The only **good-set** is $\{1, 3\}$.

**Test case $2$**: The **good-sets** are $\{1,17\}$, $\{3,15\}$, $\{5,13\}$, $\{7,11\}$ and $\{1, 3, 5, 9\}$. Thus, there are four sets of size $2$ and one set of size $4$, giving $2$ distinct sizes.

</details>

## Approach

"Every non-empty subset has an odd product" is a strong condition in disguise: the singletons are subsets, so **every element must be odd**. In particular $0$ is excluded, so the set consists of distinct positive odd integers — and then every subset product is automatically odd.

Now ask which sizes $k$ are possible for a set of $k$ distinct positive odds summing to $N$. Two constraints:

- **Minimum sum.** The smallest such set is $1 + 3 + \cdots + (2k-1) = k^2$, so $k^2 \leq N$.
- **Parity.** A sum of $k$ odd numbers is congruent to $k$ mod $2$, so $k \equiv N \pmod 2$.

Both are also sufficient: starting from $\{1, 3, \ldots, 2k-1\}$, raising the largest element by $2$ at a time reaches every value of the right parity above $k^2$, keeping the elements distinct and odd. So the count of valid sizes is

$$\#\{\,k \geq 1 : k^2 \leq N,\ k \equiv N \!\!\pmod 2\,\}$$

which with $m = \lfloor \sqrt{N} \rfloor$ is $\lfloor m/2 \rfloor$ for even $N$ and $\lceil m/2 \rceil$ for odd $N$.

Use `isqrt` rather than a floating-point square root: at $N = 10^{18}$ a `double` cannot distinguish $m^2$ from $m^2 - 1$, and the bound $k^2 \leq N$ is exactly where that matters.

The samples show the parity filter doing the work. For $N = 4$ we have $m = 2$, and only $k = 2$ survives ($\{1,3\}$); $k = 1$ fails because a single odd number cannot be even. For $N = 18$, $m = 4$ gives $k \in \{2, 4\}$ — for instance $\{1,17\}$ and $\{1,3,5,9\}$ — so the answer is $2$.

## Solution (Python)

```python
import sys
from math import isqrt


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for tok in data[1:1 + t]:
        n = int(tok)
        # k distinct odds need sum >= k^2 and have sum congruent to k mod 2.
        m = isqrt(n)
        out.append(str(m // 2 if n % 2 == 0 else (m + 1) // 2))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Every subset product odd means every element is odd**, since one even factor makes that singleton's product even — and $0$ is even, so $0$ is excluded despite non-negatives being allowed.
- **So a good-set of size $k$ is $k$ distinct positive odd numbers**, whose minimum sum is $1 + 3 + \dots + (2k-1) = k^2$ — giving the bound $k \leq \lfloor \sqrt{N} \rfloor$.
- **Parity is the second constraint.** A sum of $k$ odd numbers is congruent to $k$ modulo $2$, so only sizes matching $N$'s parity are possible.
- **Both conditions together are sufficient**, since any sum of the right parity at least $k^2$ is reachable by inflating the largest element in steps of two.
- **So the count is the number of $k \leq \lfloor \sqrt{N} \rfloor$ with $k \equiv N \pmod 2$** — $\lfloor m/2 \rfloor$ for even $N$ and $\lceil m/2 \rceil$ for odd.
- **The empty set never counts**, since its sum is $0 \neq N$ for $N \geq 1$.
- **`isqrt` must be exact**: at $N = 10^{18}$ a float square root can land one off and change the count.

## Dry run

| $N$ | $\lfloor \sqrt{N} \rfloor$ | parity of $N$ | valid sizes | count |
|---:|---:|---|---|---:|
| 4 | 2 | even | $k = 2$: $\{1,3\}$ | `1` |
| 18 | 4 | even | $k = 2$: $\{5,13\}$; $k = 4$: $\{1,3,5,9\}$ | `2` |
| 9 | 3 | odd | $k=1$: $\{9\}$; $k=3$: $\{1,3,5\}$ | 2 |

Size $3$ is impossible for $N = 4$ because $3^2 = 9 > 4$; size $1$ is impossible because $4$ is not odd.

> CodeChef tags: `Algorithms`, `Searching`

---

Same problem in rating order (#387 of 486): [../../by-rating/387-CHEFPRODUCT.md](../../by-rating/387-CHEFPRODUCT.md)
