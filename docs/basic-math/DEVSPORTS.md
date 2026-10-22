# 109. Devendra and Water Sports

> CodeChef problem code [`DEVSPORTS`](https://www.codechef.com/problems/DEVSPORTS) &middot; difficulty **859** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Remaining budget against a total cost |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Recently, Devendra went to Goa with his friends. Devendra is well known for not following a budget.

He had Rs. $Z$ at the start of the trip and has already spent Rs. $Y$ on the trip. There are three kinds of water sports one can enjoy, with prices Rs. $A$, $B$, and $C$. He wants to try each sport at least once.

If he can try all of them at least once output `YES`, otherwise output `NO`.

**Input**

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- Each test case consists of a single line of input containing five space-separated integers $Z, Y, A, B, C$.

**Output**

For each test case, print a single line containing the answer to that test case — `YES` if Devendra can try each ride at least once, and `NO` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

## Constraints

- $1\leq T\leq 10$
- $10^4 \leq Z \leq 10^5$
- $0 \leq Y \leq Z$
- $100 \leq A,B,C \leq 5000$

## Sample

**Sample input**

```
3
25000 22000 1000 1500 700
10000 7000 100 300 500
15000 5000 2000 5000 3000
```

**Sample output**

```
NO
YES
YES
```

<details><summary>Explanation</summary>

**Test Case 1:** After spending Rs. $22000$ on the trip already, Devendra is left with Rs. $3000$. The water sports cost a total of $1000+1500+700 = 3200$. So, he does not have enough money left to try all the watersports.

**Test Case 2:** After spending Rs. $10000$ on the trip, he is left with Rs. $3000$. The water sports cost a total of $100+300+500 = 900$. So, he has enough money to try all the watersports.

**Test Case 3:** After spending Rs. $5000$ on the trip, he is left with Rs. $10000$. The water sports cost a total of $2000+5000+3000 = 10000$. So, he still has enough money left to try all the watersports.

</details>

## Approach

Devendra started with $Z$ and has already spent $Y$, so he has $Z - Y$ left. He wants each of the three sports at least once, costing $A + B + C$ in total. He can manage when

$$Z - Y \geq A + B + C$$

The phrase "at least once" might suggest something more involved, but since prices are fixed and there is no discount for repeats, trying each exactly once is the cheapest way to try each at least once. So the minimum spend is simply the sum, and no optimisation is needed.

The comparison is inclusive: spending his remaining money down to exactly zero still counts. Sample case 3 is precisely this, with $10000$ remaining against a total of $10000$, giving `YES`. A strict `>` would fail it.

Sample case 1 is the near miss — $3000$ left against $3200$ of sports — and shows that the already-spent $Y$ must be subtracted first. Comparing $Z$ against the total instead would wrongly pass every case here, since $Z \geq 10^4$ while the three sports cost at most $15000$ but usually far less.

All quantities are small integers, so there is nothing to watch for numerically; the whole problem is reading the five values in the right order, $Z, Y, A, B, C$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        z, y, a, b, c = map(int, data[1 + 5 * i:6 + 5 * i])
        # Spending down to exactly zero still counts.
        out.append("YES" if z - y >= a + b + c else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Spending down to exactly zero** (the third row leaves $10000$ against a cost of $10000$): still affordable, so the comparison is non-strict.
- **Nothing spent yet** ($Y = 0$): the whole budget is available.
- **Everything already spent** ($Y = Z$): nothing remains, and since each activity costs at least $100$ the answer is `NO`.
- **All three activities are required**, so their costs *add*. Comparing the remaining budget against the largest single cost would pass the first sample row wrongly.

## Dry run

| $Z$ | $Y$ | left $Z-Y$ | $A+B+C$ | affordable? | output |
|---:|---:|---:|---:|:---:|---|
| 25000 | 22000 | 3000 | 3200 | no | `NO` |
| 10000 | 7000 | 3000 | 900 | yes | `YES` |
| 15000 | 5000 | 10000 | 10000 | yes (equal) | `YES` |

Row 3 spends the remainder exactly.

> CodeChef tags: `Basic Programming Concepts`, `Mathematics`

---

Same problem in rating order (#108 of 486): [../../by-rating/108-DEVSPORTS.md](../../by-rating/108-DEVSPORTS.md)
