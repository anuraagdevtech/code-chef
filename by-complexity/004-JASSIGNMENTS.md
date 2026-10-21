# 004. Janmansh and Assignments

> [`JASSIGNMENTS`](https://www.codechef.com/problems/JASSIGNMENTS) &middot; difficulty **513** &middot; complexity class **Constant time** $O(1)$

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Conditional arithmetic |
| **CodeChef tags** | `Mathematics`, `Basic Math`, `Arithmetic` |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Problem

Janmansh has to submit $3$ assignments for Chingari before $10$ pm and he starts to do the assignments at $X$ pm. Each assignment takes him $1$ hour to complete. Can you tell whether he'll be able to complete all assignments on time or not?

## Problem constraints

- $1 \le T \le 10$
- $1 \le X \le 9$

## Approach

Janmansh starts at $X$ pm and each of the $3$ assignments costs exactly one hour, so he finishes at hour $X + 3$. He is on time when that finishing moment is no later than the $10$ pm deadline:

$$X + 3 \leq 10 \quad\Longleftrightarrow\quad X \leq 7$$

So the whole problem collapses to a single comparison. The constraint $1 \le X \le 9$ keeps everything inside one afternoon, so there is no wrap-around past midnight to worry about and no need to convert to a 24-hour clock.

The boundary is the only place to slip. At $X = 7$ he finishes exactly at $10$ pm, and "before 10 pm" in the sense used here is satisfied — the sample confirms it, since $X = 7$ answers `Yes` while $X = 9$ (finishing at midnight) answers `No`. That makes the comparison `<=`, not `<`.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x = int(data[1 + i])
        # Starts at x, needs 3 hours, must land no later than 10.
        out.append("Yes" if x + 3 <= 10 else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **$X = 7$**, the boundary: he finishes exactly at $10$ pm, which counts as on time, so `Yes`. An off-by-one here (`<` instead of `<=`) fails precisely this case, and the sample tests it.
- **$X = 8$**: finishes at $11$ pm, so `No`.
- **$X = 1$** (smallest) finishes at $4$ pm, comfortably `Yes`; **$X = 9$** (largest) finishes at midnight, `No`.
- The bound $X \leq 9$ keeps everything inside one afternoon, so there is no wrap past midnight and no 12-hour-clock conversion to get wrong.

## Dry run

| $X$ | finishes at | $X + 3 \leq 10$ | output |
|---:|---:|:---:|---|
| 7 | $10$ pm | yes (equality) | `Yes` |
| 9 | $12$ am | no | `No` |

The first row is the tight case: equality is still on time.

---

Same problem grouped by topic: [../docs/basic-math/JASSIGNMENTS.md](../docs/basic-math/JASSIGNMENTS.md)
