[&larr; 16. Chef and Candies](CHEFCAND.md) &middot; [Index](../../README.md) &middot; [23. Nearest Exit &rarr;](NEARESTEXIT.md)

# 20. Monopoly

> CodeChef problem code [`MONOPOLY2`](https://www.codechef.com/problems/MONOPOLY2) &middot; difficulty **578** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Maximum against the sum of the rest |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

There are $4$ companies in the markets of Chefland, $A$, $B$, $C$, and $D$. $\\$
This year,
- Company $A$ made a profit of $P$ lakh rupees,
- Company $B$ made a profit of $Q$ lakh rupees,
- Company $C$ made a profit of $R$ lakh rupees,
- Company $D$ made a profit of $S$ lakh rupees.

There is said to be a **monopoly** in the market if the profit made by one company is **strictly greater than** the sum of profits made by all other companies. $\\$ Determine if there is a monopoly in the market or not.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first line and only line of each test case contains four space-separated integers $P$, $Q$, $R$ and $S$ — the profits made by companies $A$, $B$, $C$ and $D$ respectively.

**Output**

For each test case, output `YES` if there is a monopoly in the market. Otherwise, output `NO`.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical).

## Constraints

- $1 \leq T \leq 5000$
- $1 \leq P, Q, R, S \leq 100$

## Sample

**Sample input**

```
4
1 1 1 10
30 20 6 4
100 90 3 4
14 15 16 17
```

**Sample output**

```
YES
NO
YES
NO
```

<details><summary>Explanation</summary>

**Test Case 1:** Here, company $D$'s profit ($10$) is greater than the sum of profits of all other companies ($1 + 1 + 1 = 3$).

**Test Case 2:** Here, no company's profit is **strictly** greater than the sum of profits of all other companies.

**Test Case 3:** Here, company $A$'s profit ($100$) is greater than the sum of profits of all other companies ($90 + 3 + 4 = 97$).

</details>

## Approach

A monopoly exists when some company's profit strictly exceeds the combined profit of the other three. The naive reading suggests four separate checks — $P > Q+R+S$, then $Q > P+R+S$, and so on — which works but repeats itself.

A cleaner formulation: only the **largest** company can possibly dominate, since if any company beats the sum of the rest then the largest certainly does. So let $M = \max(P, Q, R, S)$ and $S_{\text{total}} = P + Q + R + S$. The rest sum to $S_{\text{total}} - M$, and the condition becomes

$$M > S_{\text{total}} - M \quad\Longleftrightarrow\quad 2M > S_{\text{total}}$$

This is the same "strict majority" shape that appeared in the Mahasena problem — one element outweighing everything else is always $2 \times \text{part} > \text{whole}$. Recognising the pattern means the code is two built-in calls and a comparison, and it generalises to any number of companies without a longer chain of `or`s.

Strictness matters at the boundary: if the largest exactly equals the sum of the others, $2M = S_{\text{total}}$ and the answer is `NO`. All profits are at least $1$, so no company can dominate by default.

Sample case 2 ($30, 20, 6, 4$) has $M = 30$ against a total of $60$, exactly the tie, and correctly answers `NO`.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        profits = list(map(int, data[1 + 4 * i:5 + 4 * i]))
        # Only the largest can dominate: max > sum - max  <=>  2 * max > sum.
        out.append("YES" if 2 * max(profits) > sum(profits) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Exact tie**, $2\max = \text{sum}$: the sample's $30\,20\,6\,4$ has max $30$ and sum $60$, so $60 > 60$ fails and the answer is `NO`. The comparison must be **strict**, and this row is there to catch `>=`.
- **Two values tied for largest** ($5\,5\,1\,1$): max $5$, sum $12$, so `NO` — neither copy can dominate, and taking "the maximum" rather than "a maximum" causes no trouble because the test only uses its value.
- **All four equal** ($1\,1\,1\,1$): $2 > 4$ fails, `NO`.
- **One value dominating** ($1\,1\,1\,10$): $20 > 13$, `YES`.
- **Only the largest can possibly dominate**, so checking the maximum alone is sufficient — there is no need to test all four.

## Dry run

| $P$ | $Q$ | $R$ | $S$ | max | sum | $2\max > \text{sum}$ | output |
|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 1 | 1 | 10 | 10 | 13 | $20 > 13$ yes | `YES` |
| 30 | 20 | 6 | 4 | 30 | 60 | $60 > 60$ no | `NO` |
| 100 | 90 | 3 | 4 | 100 | 197 | $200 > 197$ yes | `YES` |
| 14 | 15 | 16 | 17 | 17 | 62 | $34 > 62$ no | `NO` |

Row 2 is the exact tie; row 3 is a narrow win by three.

> CodeChef tags: `Basic Programming Concepts`, `Mathematics`

---

Same problem in rating order (#27 of 486): [../../by-rating/027-MONOPOLY2.md](../../by-rating/027-MONOPOLY2.md)
