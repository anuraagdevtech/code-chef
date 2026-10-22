[&larr; 9. Sale Season](SALESEASON.md) &middot; [Index](../../README.md) &middot; [17. Car or Bike &rarr;](TRAVELFAST.md)

# 11. Chefland Games

> CodeChef problem code [`CHEFGAMES`](https://www.codechef.com/problems/CHEFGAMES) &middot; difficulty **550** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Conditionals & Case Work |
| **Technique** | Reducing an AND over flags to a sum |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

In Chefland, a tennis game involves $4$ referees.
Each referee has to point out whether he considers the ball to be inside limits or outside limits. The ball is considered to be `IN` if and only if **all** the referees agree that it was inside limits.

Given the decision of the $4$ referees, help Chef determine whether the ball is considered inside limits or not.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input containing $4$ integers $R_1, R_2, R_3, R_4$ denoting the decision of the respective referees.

Here $R$ can be either $0$ or $1$ where $0$ would denote that the referee considered the ball to be inside limits whereas $1$ denotes that they consider it to be outside limits.

**Output**

For each test case, output `IN` if the ball is considered to be inside limits by all referees and `OUT` otherwise.

The checker is case-insensitive so answers like `in`, `In`, and `IN` would be considered the same.

## Constraints

- $1 \leq T \leq 20$
- $0 \leq R_1, R_2, R_3, R_4 \leq 1$

## Sample

**Sample input**

```
4
1 1 0 0
0 0 0 0
0 0 0 1
1 1 1 1
```

**Sample output**

```
OUT
IN
OUT
OUT
```

<details><summary>Explanation</summary>

**Test case $1$:** Referees $1$ and $2$ do not consider the ball to be `IN`. Thus, the ball is `OUT`.

**Test case $2$:** All referees consider the ball to be `IN`. Thus, the ball is `IN`.

**Test case $3$:** Referee $4$ does not consider the ball to be `IN`. Thus, the ball is `OUT`.

**Test case $4$:** No referee considers the ball to be `IN`. Thus, the ball is `OUT`.

</details>

## Approach

The ball is `IN` only when **every** referee calls it inside. Read the encoding carefully, because it is inverted from the intuitive one: $R_i = 0$ means *inside* limits and $R_i = 1$ means *outside*. Skimming this is the main way to lose the problem.

So the condition is $R_1 = R_2 = R_3 = R_4 = 0$. Rather than writing a four-way `and`, note that each $R_i$ is non-negative, so their sum is zero exactly when all of them are zero:

$$R_1 + R_2 + R_3 + R_4 = 0$$

Equivalently, a single `1` anywhere makes the sum positive and the ball is `OUT`. This "sum of non-negative flags is zero iff all are zero" reduction scales to any number of referees without changing the code, and it is the same idea used in the water-bottle problem, just with the threshold at zero instead of one.

Python's built-in `any` over the raw values would read just as well; the sum is used here because the values arrive as integers already.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        # 0 means "inside limits", so IN requires every value to be 0.
        calls = sum(map(int, data[1 + 4 * i:5 + 4 * i]))
        out.append("IN" if calls == 0 else "OUT")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **All four zero**: the only way to answer `IN`, since every rating must be inside its limit.
- **A single one anywhere**: `OUT`. The sample puts it in the last position ($0\,0\,0\,1$) precisely because a check that only inspects the first value or two would pass it.
- **All four one**: `OUT`.
- **The polarity is inverted** from the obvious reading: a $1$ marks a *violation*, not a pass, so `IN` is the all-zero case. Reading it the other way flips every answer.
- Summing the flags turns a four-way AND into one comparison against zero, which is harder to get subtly wrong than four chained conditions.

## Dry run

| $R_1$ | $R_2$ | $R_3$ | $R_4$ | sum | sum $= 0$? | output |
|---:|---:|---:|---:|---:|:---:|---|
| 1 | 1 | 0 | 0 | 2 | no | `OUT` |
| 0 | 0 | 0 | 0 | 0 | yes | `IN` |
| 0 | 0 | 0 | 1 | 1 | no | `OUT` |
| 1 | 1 | 1 | 1 | 4 | no | `OUT` |

Only row 2 clears every limit.

---

Same problem in rating order (#18 of 486): [../../by-rating/018-CHEFGAMES.md](../../by-rating/018-CHEFGAMES.md)
