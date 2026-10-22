[&larr; 172. Tom And Jerry 1](TANDJ1.md) &middot; [Index](../../README.md) &middot; [224. Bella ciao &rarr;](CHFHEIST.md)

# 206. Playing with Matches

> CodeChef problem code [`MATCHES`](https://www.codechef.com/problems/MATCHES) &middot; difficulty **986** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Per-digit lookup table |
| **Time** | $O(d)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | Level up from 1* to 2* (Level 2) |

## Question

Chef's son Chefu found some matches in the kitchen and he immediately starting playing with them.

The first thing Chefu wanted to do was to calculate the result of his homework — the sum of $A$ and $B$, and write it using matches. Help Chefu and tell him the number of matches needed to write the result.

Digits are formed using matches in the following way:
![](https://codechef_shared.s3.amazonaws.com/download/Images/COOK110/MATCHES/97JCfQw.gif)

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $A$ and $B$.

**Output**
For each test case, print a single line containing one integer — the number of matches needed to write the result ($A+B$).

**Constraints**
- $1 \le T \le 1,000$
- $1 \le A, B \le 10^6$

## Constraints

- $1 \le T \le 1,000$
- $1 \le A, B \le 10^6$

## Sample

**Sample input**

```
3
123 234
10101 1010
4 4
```

**Sample output**

```
13
10
7
```

<details><summary>Explanation</summary>

**Example case 1:** The result is $357$. We need $5$ matches to write the digit $3$, $5$ matches to write the digit $5$ and $3$ matches to write the digit $7$.

**Example case 2:** The result is $11111$. We need $2$ matches to write each digit $1$, which is $2 \cdot 5 = 10$ matches in total.

</details>

## Approach

Compute $A + B$ first, then count the matchsticks its decimal representation needs. Each digit has a fixed cost on a seven-segment display:

| digit | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| matches | 6 | 2 | 5 | 5 | 4 | 5 | 6 | 3 | 7 | 6 |

so the answer is the sum of those costs over the digits of the sum. Holding the table as a tuple indexed by digit turns it into a one-line sum over the string form of $A + B$.

The ordering is what matters: the matches count the **result**, not the operands. Counting the digits of $A$ and $B$ separately would answer a different question entirely — sample case 3 makes this unmissable, where $4 + 4 = 8$ costs $7$ matches, far more than the $4 + 4 = 8$ matches the inputs would suggest.

The table itself is worth memorising, or at least deriving from the seven-segment shapes: $1$ is cheapest at $2$, $7$ next at $3$, and $8$ is the most expensive at $7$ since it lights every segment.

Sample case 2 shows the digit count shrinking: $10101 + 1010 = 11111$, five `1`s at $2$ each for $10$ matches, where the operands have nine digits between them.

Working on the string form of the sum avoids a manual digit-extraction loop and its $0$ edge case — though with $A, B \geq 1$ the sum is at least $2$ and never zero anyway.

## Solution (Python)

```python
import sys

# Seven-segment cost of each digit, indexed 0..9.
COST = (6, 2, 5, 5, 4, 5, 6, 3, 7, 6)


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # The matches spell out the result, not the operands.
        out.append(str(sum(COST[int(ch)] for ch in str(a + b))))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(d)$ per test case
- **Space:** $O(1)$

## Edge cases

- **The matches spell out the *result*, not the operands.** Summing the segment costs of $A$ and $B$ themselves gives a completely different answer — the first row would then cost $2{+}5{+}5 + 5{+}5{+}4 = 26$ rather than $13$.
- **A carry changes the digit count**: $999 + 1 = 1000$ grows from three digits to four, so the sum must be formed before any counting.
- **The costs are not monotone in the digit's value**: $1$ is cheapest at two segments and $8$ dearest at seven, so a larger sum can cost fewer matches.
- **Largest input** ($A = B = 10^6$): the sum has seven digits.

## Dry run

Segment costs: $0{\to}6$, $1{\to}2$, $2{\to}5$, $3{\to}5$, $4{\to}4$, $5{\to}5$, $6{\to}6$, $7{\to}3$, $8{\to}7$, $9{\to}6$.

| $A$ | $B$ | $A+B$ | per digit | total | output |
|---:|---:|---:|---|---:|---|
| 123 | 234 | 357 | $5 + 5 + 3$ | 13 | `13` |
| 10101 | 1010 | 11111 | $2 \times 5$ | 10 | `10` |
| 4 | 4 | 8 | $7$ | 7 | `7` |

Row 3 is the dearest single digit.

---

Same problem in rating order (#161 of 486): [../../by-rating/161-MATCHES.md](../../by-rating/161-MATCHES.md)
