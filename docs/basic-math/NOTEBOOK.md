# 15. Count the Notebooks

> CodeChef problem code [`NOTEBOOK`](https://www.codechef.com/problems/NOTEBOOK) &middot; difficulty **563** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Chaining unit conversions |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

You know that $1$ kg of pulp can be used to make $1000$ pages and $1$ notebook consists of $100$ pages.

Suppose a notebook factory receives $N$ kg of pulp, how many notebooks can be made from that?

**Input**

- First line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single integer $N$ - the weight of the pulp the factory has (in kgs).

**Output**

For each test case, output the number of notebooks that can be made using $N$ kgs of pulp.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$

## Sample

**Sample input**

```
3
1
100
50
```

**Sample output**

```
10
1000
500
```

<details><summary>Explanation</summary>

**Test case-1:** $1$ kg of pulp can be used to make $1000$ pages which can be used to make $10$ notebooks.

**Test case-2:** $100$ kg of pulp can be used to make $100000$ pages which can be used to make $1000$ notebooks.

**Test case-3:** $50$ kg of pulp can be used to make $50000$ pages which can be used to make $500$ notebooks.

</details>

## Approach

This is a two-step unit conversion. One kilogram of pulp yields $1000$ pages, and one notebook consumes $100$ pages, so

$$N \text{ kg} \;\longrightarrow\; 1000N \text{ pages} \;\longrightarrow\; \frac{1000N}{100} = 10N \text{ notebooks}$$

The two constants cancel to a single factor of $10$, so the answer is simply `10 * n`.

It is worth noticing *why* no rounding appears. Because $1000$ is an exact multiple of $100$, every kilogram produces a whole number of notebooks and no pages are ever left stranded. Had a notebook taken, say, $300$ pages, the answer would have needed a floor — $\lfloor 1000N / 300 \rfloor$ — since a partial notebook cannot be sold. Spotting that the division is clean is what licenses the simplification.

Chaining the conversion in one expression, rather than computing pages into a variable and dividing afterwards, keeps the arithmetic in integers throughout.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # 1000 pages per kg / 100 pages per notebook = 10 notebooks per kg.
        out.append(str(10 * n))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **$N = 1$**: one kilogram gives $10$ notebooks, which is the conversion factor itself.
- **Largest input** ($N = 100$): $1000$ notebooks.
- **The two conversions compose exactly.** $1000$ pages per kilogram divided by $100$ pages per notebook is exactly $10$, so no rounding enters anywhere. Had the numbers not divided evenly, the chain would need a floor at the end and *only* at the end — flooring each step separately loses paper.
- Nothing here can be fractional, so there is no ceiling-versus-floor decision to make.

## Dry run

| $N$ (kg) | pages $1000N$ | notebooks $/100$ | output |
|---:|---:|---:|---:|
| 1 | 1000 | 10 | `10` |
| 100 | 100000 | 1000 | `1000` |
| 50 | 50000 | 500 | `500` |

The code folds both steps into the single multiplier $10$.

> CodeChef tags: `Mathematics`

---

Same problem in rating order (#21 of 486): [../../by-rating/021-NOTEBOOK.md](../../by-rating/021-NOTEBOOK.md)
