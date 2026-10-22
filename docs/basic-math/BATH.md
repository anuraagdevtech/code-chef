# 38. Bath in Winters

> CodeChef problem code [`BATH`](https://www.codechef.com/problems/BATH) &middot; difficulty **643** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Floor division by a composite unit |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

A geyser has a capacity of $X$ litres of water and a bucket has a capacity of $Y$ litres of water.

One person requires **exactly** $2$ buckets of water to take a bath. Find the **maximum** number of people that can take bath using water from **one completely filled** geyser..

**Input**

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains a single line of input, two integers $X, Y$.

**Output**

For each test case, output the **maximum** number of people that can take bath.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X, Y \leq 100$

## Sample

**Sample input**

```
4
10 6
25 1
100 10
30 40
```

**Sample output**

```
0
12
5
0
```

<details><summary>Explanation</summary>

**Test Case $1$:** One bucket has a capacity of $6$ litres. This means that one person requires $2\cdot 6 = 12$ litres of water to take a bath. Since this is less than the total water present in geyser, $0$ people can take bath.

**Test Case $2$:** One bucket has a capacity of $1$ litre. This means that one person requires $2\cdot 1 = 2$ litres of water to take a bath. The total amount of water present in geyser is $25$ litres. Thus, $12$ people can take bath. Note that $1$ litre water would remain unused in the geyser.

**Test Case $3$:** One bucket has a capacity of $10$ litres. This means that one person requires $2\cdot 10 = 20$ litres of water to take a bath. The total amount of water present in geyser is $100$ litres. Thus, $5$ people can take bath. Note that $0$ litres of water would remain unused in the geyser after this.

</details>

## Approach

A bucket holds $Y$ litres and one bath takes exactly $2$ buckets, so a single person consumes $2Y$ litres. The geyser holds $X$ litres, so the number of complete baths is

$$\left\lfloor \frac{X}{2Y} \right\rfloor$$

The rounding direction is the crux. A bath needs *exactly* two buckets — a person cannot bathe with one and a half — so any remaining water is simply unused and the division **floors**. This is the opposite of the cars and pizzas problems, where every person had to be served and partial units rounded up. The phrase to look for is "maximum number that can be served from a fixed supply", which always floors.

The other half of the trick is forming the right unit. The divisor is $2Y$, not $Y$: it is tempting to compute the number of buckets `x // y` and then halve it, which happens to give the same answer here but is an extra step and reads less directly. Dividing by the per-person cost in one go is both clearer and immune to a stray rounding between the two divisions.

Sample cases 1 and 4 are the ones that punish a wrong direction: $10$ litres against a $12$-litre bath, and $30$ against $80$, both yield $0$ people rather than $1$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # One bath costs exactly 2 * y litres; leftover water is wasted.
        out.append(str(x // (2 * y)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Not enough for a single bath** ($X = 10$, $Y = 6$ needs $12$ litres): the answer is $0$, and two of the four sample rows are this case.
- **Leftover water is wasted** — this is a floor, not a ceiling. $X = 25$, $Y = 1$ gives $12$ baths using $24$ litres and strands the last one.
- **An exact fit** ($X = 100$, $Y = 10$): $5$ baths with nothing left.
- **The unit is $2Y$, not $Y$.** A bath needs $Y$ hot *and* $Y$ cold, so dividing by $Y$ doubles every answer — the composite unit is the only real content here.

## Dry run

| $X$ (litres) | $Y$ | cost per bath $2Y$ | $X // 2Y$ | output |
|---:|---:|---:|---:|---|
| 10 | 6 | 12 | 0 | `0` |
| 25 | 1 | 2 | 12 | `12` |
| 100 | 10 | 20 | 5 | `5` |
| 30 | 40 | 80 | 0 | `0` |

Row 2 wastes one litre; rows 1 and 4 cannot afford even one bath.

> CodeChef tags: `Mathematics`, `Basic Math`

---

Same problem in rating order (#45 of 486): [../../by-rating/045-BATH.md](../../by-rating/045-BATH.md)
