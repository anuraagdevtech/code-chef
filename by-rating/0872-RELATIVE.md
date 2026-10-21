# 872 &middot; Relativity

> CodeChef problem code [`RELATIVE`](https://www.codechef.com/problems/RELATIVE) &middot; time limit **0.5s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Rearranging a given formula |
| **CodeChef tags** | `Special`, `Algorithms`, `Physics`, `Mathematics`, `Brute Force` |
| **CodeChef category** | school |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/basic-math/RELATIVE.md](../docs/basic-math/RELATIVE.md)

## Question

In Chefland, the speed of light is $c\ \mathrm{m}/\mathrm{s}$, and acceleration due to gravity is $g\ \mathrm{m}/\mathrm{s}^2$.

Find the smallest height (in meters) from which Chef should jump such that during his journey down only under the effect of gravity and independent of any air resistance, he achieves the speed of light and verifies Einstein's theory of special relativity.

Assume he jumps at zero velocity and at any time, his velocity ($v$) and depth of descent ($H$) are related as
$$v^2 = 2 \cdot g \cdot H.$$

### Input

- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, two integers $g$, $c$.

### Output
For each test case, output in a single line the answer to the problem. We can show that under the constraints, the answer is an integer.

## Constraints

$1 \leq T \leq 5\cdot 10^3$
- $1 \leq g \leq 10$
- $1000 \leq c \leq 3000$
- $2 \cdot g$ divides $c^2$.

**Subtasks**

**Subtask #1 (100 points):** Original constraints

## Sample

**Sample input**

```
3
7 1400
5 1000
10 1000
```

**Sample output**

```
140000
100000
50000
```

<details><summary>Explanation</summary>

**Test Case $1$:** For Chef to achieve the speed of light, the minimum height required is $\frac{c^2}{2 \cdot g}$ = $\frac{1400 \cdot 1400}{14}$ = $140000$ meters.

**Test Case $3$:** For Chef to achieve the speed of light, the minimum height required is $\frac{c^2}{2 \cdot g}$ = $\frac{1000 \cdot 1000}{20}$ = $50000$ meters.

</details>

## Approach

The problem hands over the relation $v^2 = 2gH$ and asks for the height at which the falling speed reaches $c$. Substituting $v = c$ and solving for $H$:

$$H = \frac{c^2}{2g}$$

That is the entire problem — the physics is supplied, so the work is purely algebraic rearrangement.

The constraint that **$2g$ divides $c^2$** is what makes the answer an exact integer, as the statement promises. That guarantee is why `c * c // (2 * g)` is safe: the division leaves no remainder, so integer division loses nothing. Without it, the answer would need a rounding rule and the problem would have to say which way.

Using floating point here would be the needless risk. With $c$ up to $3000$, $c^2$ reaches $9 \times 10^6$ and the quotient stays small, so a float would in fact be exact — but integer arithmetic makes that reasoning unnecessary, and the habit matters once values grow past $2^{53}$.

Checking sample 1: $c^2 = 1400^2 = 1{,}960{,}000$ and $2g = 14$, giving $140{,}000$ metres.

The relativity framing is a joke, of course — a real object cannot reach the speed of light, and the Newtonian formula would not apply anywhere near it. The tags mark this as a "Special" problem for that reason, but the computation is unaffected.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        g, c = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # v^2 = 2gH with v = c; 2g is guaranteed to divide c^2 exactly.
        out.append(str(c * c // (2 * g)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
