# 10. Minimum Pizzas

> CodeChef problem code [`MINPIZZA`](https://www.codechef.com/problems/MINPIZZA) &middot; difficulty **546** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Ceiling division |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Each pizza consists of $4$ slices. There are $N$ friends and each friend needs exactly $X$ slices.

Find the **minimum** number of pizzas they should order to satisfy their appetite.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two integers $N$ and $X$, the number of friends and the number of slices each friend wants respectively.

**Output**

For each test case, output the **minimum** number of pizzas required.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N, X \leq 10$

## Sample

**Sample input**

```
4
1 5
2 6
4 3
3 5
```

**Sample output**

```
2
3
3
4
```

<details><summary>Explanation</summary>

**Test case $1$:** There is only $1$ friend who requires $5$ slices. If he orders $1$ pizza, he will get only $4$ slices. Thus, at least $2$ pizzas should be ordered to have required number of slices.

**Test case $2$:** There are $2$ friends who require $6$ slices each. Thus, total $12$ slices are required. To get $12$ slices, they should order $3$ pizzas.

**Test case $3$:** There are $4$ friends who require $3$ slices each. Thus, total $12$ slices are required. To get $12$ slices, they should order $3$ pizzas.

**Test case $4$:** There are $3$ friends who require $5$ slices each. Thus, total $15$ slices are required. To get $15$ slices, they should order at least $4$ pizzas.

</details>

## Approach

$N$ friends each want $X$ slices, so the group needs $N \cdot X$ slices in total. A pizza yields $4$ slices and pizzas are only sold whole, so the number to order is

$$\left\lceil \frac{N \cdot X}{4} \right\rceil$$

Leftover slices are fine; being short by even one is not. That asymmetry is what forces a **ceiling** here, in contrast to the floor used when spending a fixed budget.

As with the subscriptions problem, compute the ceiling in integers using

$$\left\lceil \frac{n}{k} \right\rceil = \left\lfloor \frac{n + k - 1}{k} \right\rfloor$$

so the expression is `(n * x + 3) // 4`. A useful sanity check is that the formula must return the exact quotient when the division is clean and never overshoot: with $N \cdot X = 12$ it gives $(12 + 3) // 4 = 3$, not $4$.

Sample case 3 is the clean-division case ($4 \times 3 = 12$ slices, exactly $3$ pizzas) and case 1 is the ragged one ($1 \times 5 = 5$ slices, needing $2$ pizzas and wasting $3$ slices).

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # ceil(n * x / 4) in integer arithmetic.
        out.append(str((n * x + 3) // 4))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Slices an exact multiple of $4$** ($N = 2$, $X = 6$ gives $12$): the $+3$ must not buy a spare pizza — $(12+3)//4 = 3$, not $4$.
- **A single slice** ($N = X = 1$): $\lceil 1/4 \rceil = 1$, because a lone slice still needs a whole pizza.
- **Largest input** ($N = X = 10$): $100$ slices, so $25$ pizzas with nothing wasted.
- **Multiply before dividing.** The need is $N \cdot X$ slices in total; computing $\lceil X/4 \rceil$ per person and multiplying by $N$ over-orders whenever $X$ is not a multiple of four — for $N = 4$, $X = 3$ that would give $4$ pizzas instead of $3$.

## Dry run

| $N$ | $X$ | slices $NX$ | $NX + 3$ | $//\,4$ | output |
|---:|---:|---:|---:|---:|---|
| 1 | 5 | 5 | 8 | 2 | `2` |
| 2 | 6 | 12 | 15 | 3 | `3` |
| 4 | 3 | 12 | 15 | 3 | `3` |
| 3 | 5 | 15 | 18 | 4 | `4` |

Rows 2 and 3 need the same $12$ slices by different routes, and both round to $3$ rather than $4$.

> CodeChef tags: `Mathematics`

---

Same problem in rating order (#17 of 486): [../../by-rating/017-MINPIZZA.md](../../by-rating/017-MINPIZZA.md)
