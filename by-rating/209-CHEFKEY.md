# 209. Chef and Keyboard

> [`CHEFKEY`](https://www.codechef.com/problems/CHEFKEY) &middot; difficulty **1323** &middot; time limit **1s** &middot; Jump from 2* to 3* (Level 3)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Divisor pairs under a box constraint |
| **Complexity class** | Square root $O(\sqrt{n})$ |
| **Time** | $O(\sqrt{c})$ per test case |
| **Space** | $O(1)$ |

## Question

Chef is a well known programmer. He owns a brand new Android phone of screen size of dimension **n × m** (**n** denotes the height of the phone and **m** denotes the width). Chef wants to design a program for painting the screen. He figured out **c** colors, which he will use to paint the screen. He wants to paint some rectangular section of pixels of the screen each with different color. Also Chef would like to use all of his **c** colors in painting.

Can you help Chef in finding number of different dimensions of rectangular section he can paint? In other words, find number of pairs **x, y** such that Chef can paint a rectangular section of dimension **x × y** (**x** denotes height, **y** denotes width) on the screen. Please note that Chef uses a fix orientation of his phone and is not allowed to rotate it, i.e. height always stays **n** and width always stays **m** and not the other way around.

**Input**

First line of the input contains an integer **T** denoting the number of test cases. **T** test cases follow.

Only line of each test case contains three space separated integers **n, m, c**.

**Output**

For each test case, output a single line containing the answer for the test case.

**Constraints**

- **1** ≤ **T** ≤ **100**

- **1** ≤ **n, m** ≤ **10^6**

- **1** ≤ **c** ≤ **10^6**

**Subtasks**

- Subtask #1: (40 points) **1** ≤ **n, m** ≤ **100**, **1** ≤ **c** ≤ **10^4**

- Subtask #2: (60 points) **original constraints**

## Constraints

- 1 ≤ T ≤ 100
- 1 ≤ n, m ≤ 10^6
- 1 ≤ c ≤ 10^6

## Sample

**Sample input**

```
2
4 6 12
3 3 10
```

**Sample output**

```
3
0
```

<details><summary>Explanation</summary>

**Test case 1.** Possible pairs of dimensions are **(2, 6)**, **(3, 4)** and **(4, 3)**. Note that the rectangular section of dimension **(1, 12)** can't be painted as it can't fit into the screen, because 12 > 6.

**Test case 2.** There does not exist any rectangle of desired dimensions which can have 10 different pixels painted.

</details>

## Approach

Every pixel of the painted rectangle gets a different colour and all $c$ colours are used, so an $x \times y$ section is paintable exactly when it has $c$ pixels and fits on the screen:

$$x \cdot y = c, \qquad x \leq n, \qquad y \leq m$$

So the question is how many **divisor pairs** of $c$ fit inside the $n \times m$ box. Orientation is fixed, so $(x,y)$ and $(y,x)$ are counted separately whenever both fit — the asymmetry of the box is the whole point.

Enumerate divisors up to $\sqrt{c}$. Each divisor $d \leq \sqrt{c}$ yields the pair $(d, c/d)$, and its partner $(c/d, d)$ unless $d^2 = c$, in which case the two coincide and must be counted once. Both are tested against the box independently.

$$\text{answer} = \#\{d \mid c : d \leq n \text{ and } c/d \leq m\}$$

At $\sqrt{10^6} = 1000$ iterations per test and $T \leq 100$, this is trivial — far better than scanning all $x \leq n$ with $n$ up to $10^6$.

The samples show both outcomes. With $n = 4, m = 6, c = 12$ the fitting pairs are $(2,6)$, $(3,4)$ and $(4,3)$, giving $3$; $(1,12)$ is too wide and $(6,2)$, $(12,1)$ too tall. With $n = m = 3$ and $c = 10$, the divisors of $10$ are $1, 2, 5, 10$ and every pair needs a side of at least $5$, so nothing fits and the answer is $0$ — note that a screen having $9 \geq c$ is not enough on its own.

## Solution

```python
import sys
from math import isqrt


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, m, c = (int(data[1 + 3 * i]), int(data[2 + 3 * i]), int(data[3 + 3 * i]))
        found = 0
        for d in range(1, isqrt(c) + 1):
            if c % d:
                continue
            other = c // d
            if d <= n and other <= m:
                found += 1
            # The mirrored orientation is a separate section unless d == c/d.
            if other != d and other <= n and d <= m:
                found += 1
        out.append(str(found))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/number-theory/CHEFKEY.md](../docs/number-theory/CHEFKEY.md)
