# 010. Chef in his Office

> [`OFFICE`](https://www.codechef.com/problems/OFFICE) &middot; difficulty **532** &middot; complexity class **Constant time** $O(1)$

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Direct formula |
| **CodeChef tags** | `Mathematics`, `Basic Programming Concepts`, `Basic Math` |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Problem

Recently Chef joined a new company. In this company, the employees have to work for $X$ hours each day from Monday to Thursday. Also, in this company, Friday is called Chill Day — employees only have to work for $Y$ hours $(Y \lt X)$ on Friday. Saturdays and Sundays are holidays.

Determine the total number of working hours in one week.

## Problem constraints

- $1 \leq T \leq 100$
- $2 \leq X \leq 12$
- $1 \le Y \lt X$

## Approach

The week splits into three kinds of day. Monday through Thursday is four days at $X$ hours each, Friday is a single day at $Y$ hours, and the weekend contributes nothing. Summing them gives the whole answer in one expression:

$$\text{total} = 4X + Y$$

There is no loop to write and no edge case to guard. The constraint $Y < X$ is flavour — it makes Friday genuinely the lighter day — but the formula never depends on it, so no validation is needed.

The thing worth internalising is the counting itself: "Monday to Thursday" is four days, not five. Off-by-one on an inclusive day range is the classic slip, and reading it as $5X + Y$ would pass no sample at all. Checking against the first one: $X=10, Y=5$ gives $4 \cdot 10 + 5 = 45$.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Mon-Thu is four days at x hours, Friday is y, weekend is zero.
        out.append(str(4 * x + y))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **$Y < X$ is guaranteed**, so Friday is always the short day; the formula never needs to decide which day is shorter.
- **Smallest input** ($X = 2$, $Y = 1$): $4 \times 2 + 1 = 9$ hours.
- **Largest input** ($X = 12$, $Y = 11$): $4 \times 12 + 11 = 59$ hours.
- **The weekend contributes nothing** — the count is four full days plus Friday, not five plus two, so a "7 days" reflex overcounts.

## Dry run

| $X$ | $Y$ | $4X$ (Mon&ndash;Thu) | $+Y$ (Fri) | output |
|---:|---:|---:|---:|---|
| 10 | 5 | 40 | 45 | `45` |
| 12 | 2 | 48 | 50 | `50` |
| 8 | 7 | 32 | 39 | `39` |

---

Same problem grouped by topic: [../docs/basic-math/OFFICE.md](../docs/basic-math/OFFICE.md)
