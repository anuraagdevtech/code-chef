[&larr; 165. Chef in Vaccination Queue](165-VACCINQ.md) &middot; [Index](README.md) &middot; [167. Devu and friendship testing &rarr;](167-CFRTEST.md)

# 166. Weight Balance

> [`WEIGHTBL`](https://www.codechef.com/problems/WEIGHTBL) &middot; difficulty **1045** &middot; time limit **0.5s** &middot; Level up from 1* to 2* (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Reachable range over repeated choices |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

No play and eating all day makes your belly fat. This happened to Chef during the lockdown. His weight before the lockdown was $w_1$ kg (measured on the most accurate hospital machine) and after $M$ months of lockdown, when he measured his weight at home (on a regular scale, which can be inaccurate), he got the result that his weight was $w_2$ kg ($w_2 \gt w_1$).

Scientific research in all growing kids shows that their weights increase by a value between $x_1$ and $x_2$ kg (inclusive) per month, but not necessarily the same value each month. Chef assumes that he is a growing kid. Tell him whether his home scale could be giving correct results.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains five space-separated integers $w_1$, $w_2$, $x_1$, $x_2$ and $M$.

**Output**
For each test case, print a single line containing the integer $1$ if the result shown by the scale can be correct or $0$ if it cannot.

**Constraints**
- $1 \leq T \leq 10^5$
- $1 \leq w_1 \lt w_2 \leq 100$
- $0 \leq x_1 \leq x_2 \leq 10$
- $1 \leq M \leq 10$

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq w_1 \lt w_2 \leq 100$
- $0 \leq x_1 \leq x_2 \leq 10$
- $1 \leq M \leq 10$

## Sample

**Sample input**

```
5
1 2 1 2 2
2 4 1 2 2
4 8 1 2 2
5 8 1 2 2
1 100 1 2 2
```

**Sample output**

```
0
1
1
1
0
```

<details><summary>Explanation</summary>

**Example case 1:** Since the increase in Chef's weight is $2 - 1 = 1$ kg and that is less than the minimum possible increase $1 \cdot 2 = 2$ kg, the scale must be faulty.

**Example case 2:** Since the increase in Chef's weight is $4 - 2 = 2$ kg, which is equal to the minimum possible increase $1 \cdot 2 = 2$ kg, the scale is showing correct results.

**Example case 3:** Since the increase in Chef's weight is $8 - 4 = 4$ kg, which is equal to the maximum possible increase $2 \cdot 2 = 4$ kg, the scale is showing correct results.

**Example case 4:** Since the increase in Chef's weight $8 - 5 = 3$ kg lies in the interval $[1 \cdot 2, 2 \cdot 2]$ kg, the scale is showing correct results.

**Example case 5:** Since the increase in Chef's weight is $100 - 1 = 99$ kg and that is more than the maximum possible increase $2 \cdot 2 = 4$ kg, the weight balance must be faulty.

</details>

## Approach

Over $M$ months Chef gains between $x_1$ and $x_2$ kilograms each month, and the monthly gains need not be equal. So the **total** gain can be anything from $M \cdot x_1$ to $M \cdot x_2$ — and, since the per-month values vary freely, every value in that range is attainable.

The scale is consistent with the science exactly when the observed gain lands inside:

$$M \cdot x_1 \leq w_2 - w_1 \leq M \cdot x_2$$

The step worth justifying is that the range has no gaps. With each month free to take any value in $[x_1, x_2]$, the achievable totals form a continuous interval rather than a scattered set — so a single two-sided comparison suffices and there is nothing to search over.

Both bounds are needed, and the samples prove it. Case 1 fails the **lower** bound: a gain of $1$ kg over two months is less than the minimum $2$, so the scale is reading too low. Case 5 fails the **upper** bound with a gain of $99$ against a maximum of $4$. Dropping either comparison passes one of these wrongly.

Cases 2 through 4 land on and inside the range — case 2 exactly on the minimum and case 3 exactly on the maximum — confirming both ends are inclusive.

Note that $x_1$ may be $0$, so a gain of zero can be legitimate; but $w_1 < w_2$ is guaranteed, so the observed gain is always at least $1$.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        w1, w2, x1, x2, m = map(int, data[1 + 5 * i:6 + 5 * i])
        gain = w2 - w1
        # Monthly gains vary freely, so every total in the range is reachable.
        out.append("1" if m * x1 <= gain <= m * x2 else "0")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Below the minimum** (the first row: a gain of $1$ against a required $2 \times 1 = 2$): `0`.
- **Above the maximum** (the last row: a gain of $99$ against a ceiling of $2 \times 2 = 4$): `0`.
- **Exactly on either bound**: the second row sits on the lower bound and the third on the upper, and both answer `1` — so both comparisons are non-strict, and the sample covers each.
- **$x_1 = x_2$**: the range collapses to a single value and the gain must match it exactly.
- **$x_1$ may be $0$**, which makes the lower bound $0$ and admits any gain up to $m x_2$.
- Monthly gains vary freely within $[x_1, x_2]$, so **every** integer total in $[m x_1, m x_2]$ is reachable — that is why a plain range test suffices and no divisibility condition is needed.

## Dry run

| $w_1$ | $w_2$ | gain | $x_1$ | $x_2$ | $M$ | range $[Mx_1, Mx_2]$ | inside? | output |
|---:|---:|---:|---:|---:|---:|---|:---:|---|
| 1 | 2 | 1 | 1 | 2 | 2 | $[2,4]$ | no | `0` |
| 2 | 4 | 2 | 1 | 2 | 2 | $[2,4]$ | yes (lower) | `1` |
| 4 | 8 | 4 | 1 | 2 | 2 | $[2,4]$ | yes (upper) | `1` |
| 5 | 8 | 3 | 1 | 2 | 2 | $[2,4]$ | yes | `1` |
| 1 | 100 | 99 | 1 | 2 | 2 | $[2,4]$ | no | `0` |

---

Same problem grouped by topic: [../docs/basic-math/WEIGHTBL.md](../docs/basic-math/WEIGHTBL.md)
